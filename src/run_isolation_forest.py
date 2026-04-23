
from pathlib import Path
import pandas as pd
import yaml
from sklearn.ensemble import IsolationForest
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    df = pd.read_csv(cfg["input_path"])
    date_col = cfg["date_column"]
    X = df.drop(columns=[date_col], errors="ignore").select_dtypes(include=["number"]).fillna(0)
    model = IsolationForest(
        n_estimators=params["isolation_forest"]["n_estimators"],
        contamination=params["isolation_forest"]["contamination"],
        random_state=params["isolation_forest"]["random_state"],
    )
    scores = -model.fit_predict(X)
    raw_scores = -model.score_samples(X)
    result = df[[date_col]].copy() if date_col in df.columns else pd.DataFrame(index=df.index)
    result["anomaly_score"] = raw_scores
    result["flag"] = scores
    result.to_csv("artifacts/iforest_scored.csv", index=False)
    metrics = {
        "method": "isolation_forest",
        "rows_scored": int(len(X)),
        "flagged_rows": int((result["flag"] > 0).sum()),
        "mean_score": float(result["anomaly_score"].mean()),
        "max_score": float(result["anomaly_score"].max()),
        "artifact": "artifacts/iforest_scored.csv",
    }
    save_json(metrics, cfg["score_output"])
    print(f"Saved {cfg['score_output']}")

if __name__ == "__main__":
    main()
