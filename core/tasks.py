from celery import shared_task
from .models import PlateInspection, InspectionResult
import os

@shared_task(bind=True)
def process_plate_batch_task(self, batch_item_ids):
    """
    Processes a list of PlateInspection IDs asynchronously with fail-safe isolation.
    """
    for inspection_id in batch_item_ids:
        inspection = PlateInspection.objects.get(id=inspection_id)
        try:
            # Step status: Processing
            inspection.status = 'PROCESSING'
            inspection.save(update_fields=['status'])

            # Run model inference wrapper
            image_path = inspection.image_file.path
            inference_output = run_plate_inference(image_path)

            # Save successful result
            InspectionResult.objects.create(
                inspection=inspection,
                confidence=inference_output['confidence'],
                defect_detected=inference_output['defect_detected'],
                details=inference_output['details']
            )

            inspection.status = 'COMPLETED'
            inspection.save(update_fields=['status'])

        except Exception as e:
            # FAIL-SAFE ISOLATION: Catch individual errors so batch doesn't halt
            inspection.status = 'FAILED'
            inspection.error_message = str(e)
            inspection.save(update_fields=['status', 'error_message'])