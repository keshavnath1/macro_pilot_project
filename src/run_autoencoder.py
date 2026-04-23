
import pandas as pd
from common import load_yaml, save_json, cli

def main() -> None:
    args = cli()
    cfg = load_yaml(args.config)
    df = pd.read_csv(cfg["input_path"])
    metrics = {
        "method": "autoencoder",
        "status": "starter placeholder",
        "next_step": "replace with PyTorch or TensorFlow implementation if nonlinear anomaly detection becomes a priority",
        "rows_available": int(len(df)),
    }
    save_json(metrics, cfg["score_output"])
    print(f"Saved {cfg['score_output']}")

if __name__ == "__main__":
    main()
