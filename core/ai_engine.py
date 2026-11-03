import subprocess
import json

def run_plate_inference(image_path):
    """
    Invokes the BIT-PLATE-CV-1.0 inference script and parses results.
    """
    # Example subprocess call to the provided inference script
    cmd = ['python', 'inference.py', '--model', 'BIT-PLATE-CV-1.0', '--image', image_path]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Inference Engine Error: {result.stderr.strip()}")

    # Parse JSON output returned by inference.py
    output_data = json.loads(result.stdout)
    return {
        'confidence': output_data.get('confidence', 0.0),
        'defect_detected': output_data.get('defect_detected', False),
        'details': output_data.get('details', {})
    }