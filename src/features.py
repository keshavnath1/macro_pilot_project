
from pathlib import Path
import pandas as pd
import numpy as np
import yaml
from common import load_yaml, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    df = pd.read_csv(cfg["output_interim"])
    date_col = cfg["date_column"]
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df.sort_values(date_col)
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    feature_df = df[[date_col]].copy() if date_col in df.columns else pd.DataFrame(index=df.index)
    for col in num_cols:
        feature_df[col] = df[col]
        for lag in params["features"]["lags"]:
            feature_df[f"{col}_lag_{lag}"] = df[col].shift(lag)
        for win in params["features"]["rolling_windows"]:
            feature_df[f"{col}_rollmean_{win}"] = df[col].rolling(win).mean()
        for p in params["features"]["pct_change_windows"]:
            feature_df[f"{col}_pctchg_{p}"] = df[col].pct_change(p)
    feature_df = feature_df.ffill().bfill()
    Path(cfg["output_processed"]).parent.mkdir(parents=True, exist_ok=True)
    feature_df.to_csv(cfg["output_processed"], index=False)
    print(f"Wrote engineered features to {cfg['output_processed']}")

if __name__ == "__main__":
    main()
