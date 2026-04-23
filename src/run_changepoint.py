
import pandas as pd
import yaml
import ruptures as rpt
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    df = pd.read_csv(cfg["input_path"])
    date_col = cfg["date_column"]
    num_df = df.drop(columns=[date_col], errors="ignore").select_dtypes(include=["number"]).fillna(0)
    target_series = num_df.mean(axis=1).values
    algo = rpt.Pelt(model=params["changepoint"]["model"]).fit(target_series)
    breakpoints = algo.predict(pen=params["changepoint"]["penalty"])
    metrics = {
        "method": "changepoint",
        "rows_used": int(len(target_series)),
        "breakpoint_indices": [int(x) for x in breakpoints],
        "n_breaks": int(len(breakpoints)),
        "series_used": "row_mean_proxy",
    }
    save_json(metrics, cfg["score_output"])
    print(f"Saved {cfg['score_output']}")

if __name__ == "__main__":
    main()
