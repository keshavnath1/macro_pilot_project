
from pathlib import Path
import pandas as pd
from common import load_yaml, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    raw_path = Path(cfg["raw_path"])
    if not raw_path.exists():
        raise FileNotFoundError(f"Place the Kaggle CSV at {raw_path}")
    df = pd.read_csv(raw_path)
    Path(cfg["output_interim"]).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cfg["output_interim"], index=False)
    print(f"Wrote {cfg['output_interim']} with {len(df)} rows and {len(df.columns)} columns")

if __name__ == "__main__":
    main()
