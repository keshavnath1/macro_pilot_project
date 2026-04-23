
import pandas as pd
import yaml
from sklearn.decomposition import IncrementalPCA
from sklearn.preprocessing import StandardScaler
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    df = pd.read_csv(cfg["input_path"])
    date_col = cfg["date_column"]
    X = df.drop(columns=[date_col], errors="ignore").select_dtypes(include=["number"]).fillna(0)
    Xs = StandardScaler().fit_transform(X)
    model = IncrementalPCA(
        n_components=params["incremental_pca"]["n_components"],
        batch_size=params["incremental_pca"]["batch_size"],
    )
    comps = model.fit_transform(Xs)
    pd.DataFrame(comps, columns=[f"pc_{i+1}" for i in range(comps.shape[1])]).to_csv("artifacts/incremental_pca_components.csv", index=False)
    metrics = {
        "method": "incremental_pca",
        "n_components": int(model.n_components),
        "explained_variance_ratio": [float(x) for x in model.explained_variance_ratio_],
        "cumulative_explained_variance": float(model.explained_variance_ratio_.sum()),
        "artifact": "artifacts/incremental_pca_components.csv",
    }
    save_json(metrics, cfg["score_output"])
    print(f"Saved {cfg['score_output']}")

if __name__ == "__main__":
    main()
