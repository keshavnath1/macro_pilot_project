
import json
from pathlib import Path
import pandas as pd

def main() -> None:
    metric_files = sorted(Path("metrics").glob("*.json"))
    rows = []
    for fp in metric_files:
        with open(fp, "r") as f:
            obj = json.load(f)
        obj["file"] = str(fp)
        rows.append(obj)
    if rows:
        pd.DataFrame(rows).to_csv("metrics/metrics_summary_generated.csv", index=False)
        print("Wrote metrics/metrics_summary_generated.csv")
    else:
        print("No metrics JSON files found.")

if __name__ == "__main__":
    main()
