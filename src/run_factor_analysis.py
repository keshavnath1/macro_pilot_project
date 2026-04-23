
import pandas as pd
import yaml
from sklearn.decomposition import FactorAnalysis
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    df = pd.read_csv(cfg["input_path"])
    date_col = cfg["date_column"]
    X = df.drop(columns=[date_col], errors="ignore").select_dtypes(include=["number"]).fillna(0)
    model = FactorAnalysis(n_components=params["factor_analysis"]["n_factors"], random_state=42)
    scores = model.fit_transform(X)
    loadings = pd.DataFrame(model.components_.T, index=X.columns)
    loadings.columns = [f"factor_{i+1}" for i in range(loadings.shape[1])]
    loadings.to_csv("artifacts/factor_loadings.csv")
    pd.DataFrame(scores, columns=loadings.columns).to_csv("artifacts/factor_scores.csv", index=False)
    metrics = {
        "method": "factor_analysis",
        "rows_used": int(len(X)),
        "features_used": int(X.shape[1]),
        "n_factors": int(loadings.shape[1]),
        "top_features_factor_1": loadings["factor_1"].abs().sort_values(ascending=False).head(5).index.tolist(),
        "artifact_loadings": "artifacts/factor_loadings.csv",
    }
    save_json(metrics, cfg["score_output"])
    print(f"Saved {cfg['score_output']}")

if __name__ == "__main__":
    main()
