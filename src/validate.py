
from pathlib import Path
import pandas as pd
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    df = pd.read_csv(cfg["output_interim"])
    metrics = {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_rate_by_column": df.isna().mean().round(4).to_dict(),
    }
    save_json(metrics, cfg["metrics_path"])
    print(f"Saved validation metrics to {cfg['metrics_path']}")

if __name__ == "__main__":
    main()
