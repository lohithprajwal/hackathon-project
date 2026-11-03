import os
import sys
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

# Add Model folder to path
model_path = os.path.abspath(os.path.join('phase2_pkg', 'Model') if os.path.exists('phase2_pkg') else 'Model')
sys.path.append(model_path)

try:
    import inference
except ImportError:
    print("Error: inference.py not found in Model path. Please ensure phase2_pkg/Model is present.")
    sys.exit(1)

def run_evaluation(samples_dir, labels_csv_path):
    if not os.path.exists(labels_csv_path):
        print(f"Error: Labels file not found at {labels_csv_path}")
        return

    df = pd.read_csv(labels_csv_path)
    y_true = []
    y_pred = []
    failed = 0

    print("Running evaluation across sample set...")
    for idx, row in df.iterrows():
        img_path = os.path.join(samples_dir, row['relative_path'])
        if not os.path.exists(img_path):
            continue
        try:
            pred = inference.predict(img_path)
            pred_str = 'Defective' if pred else 'Normal'
            y_true.append(row['label'])
            y_pred.append(pred_str)
        except Exception as e:
            failed += 1

    cm = confusion_matrix(y_true, y_pred, labels=['Defective', 'Normal'])
    report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)
    recall = report.get('Defective', {}).get('recall', 0.0) * 100

    print("\n================ EVALUATION RESULTS ================")
    print(f"Total Evaluated : {len(y_true)}")
    print(f"Failed Inferences: {failed}")
    print("\nConfusion Matrix:")
    print(cm)
    print(f"\nDefect Recall (Defective Class): {recall:.2f}%")
    print("=====================================================")

if __name__ == '__main__':
    # Change 'phase2_pkg/Samples' to 'Samples'
    run_evaluation('Samples', 'Samples/labels.csv')
