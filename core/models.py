from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100)
    model_code = models.CharField(max_length=50, default="P-PLATE01")
    status = models.CharField(max_length=50, default="Active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Manual(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='manuals/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AuditLog(models.Model):
    action = models.CharField(max_length=255)
    performed_by = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.action} by {self.performed_by}"

class InspectionRecord(models.Model):
    image_name = models.CharField(max_length=255)
    prediction = models.CharField(max_length=50)
    confidence = models.FloatField()
    model_version = models.CharField(max_length=50, default="BIT-PLATE-CV-1.0")
    supervisor_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image_name} - {self.prediction} ({self.confidence}%)"

class InspectionResult(models.Model):
    batch_id = models.CharField(max_length=100)
    image_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50) # Defective or Normal
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image_name} - {self.status}"

class SupervisorReview(models.Model):
    inspection = models.ForeignKey(InspectionResult, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=150)
    override_status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer} on {self.inspection.image_name}"