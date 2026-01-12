import json
import subprocess
from pathlib import Path


METRICS_PATH = Path("reports/metrics.json")
MIN_TEST_MACRO_F1 = 0.70


def test_training_produces_metrics_and_meets_threshold():
    # Run training end-to-end
    result = subprocess.run(
        ["python", "src/train.py"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        "Training script failed.\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}\n"
    )

    # Confirm metrics file exists
    assert METRICS_PATH.exists(), "Expected reports/metrics.json to be created."

    # Load and check macro-F1 threshold on TEST split
    payload = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    test_report = payload["metrics"]["test"]
    test_macro_f1 = float(test_report["macro avg"]["f1-score"])

    assert test_macro_f1 >= MIN_TEST_MACRO_F1, (
        f"Test macro-F1 too low: {test_macro_f1:.3f} < {MIN_TEST_MACRO_F1:.2f}\n"
        "If this fails unexpectedly, check for data/code changes or update the threshold intentionally."
    )
