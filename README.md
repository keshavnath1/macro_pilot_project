# Macro Analytics Pilot

A reproducible starter project for macroeconomic analytics using **Git + DVC** and a method portfolio that supports:

- anomaly detection on large tabular macro data with **Isolation Forest**
- interpretable latent macro drivers with **Factor Analysis**
- nonlinear anomaly detection with **Autoencoders**
- scalable dimensionality reduction with **Incremental PCA**
- time-based regime and trend change detection with **Change Point Detection / State Space models**

## Recommended pilot dataset
**US Economic Indicators (1991–2023)** from Kaggle.

Place the downloaded dataset in `data/raw/` and update the file path in `configs/base.yaml`.

## Deliverables in this package
- `notebooks/macro_exploration_starter.ipynb` — starter exploration notebook
- `reports/experiment_comparison_report.md` — comparison report template
- `metrics/metrics_summary.csv` — starter evaluation matrix
- `docs/visual_appendix.md` — plot and visual guidance
- `src/` — starter scripts for pipeline stages
- `dvc.yaml` and `params.yaml` — reproducible pipeline skeleton

## Reproducibility steps

### 1. Create environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Initialize Git and DVC
```bash
git init
dvc init
git add .
git commit -m "Initial macro analytics pilot scaffold"
```

### 3. Add the dataset
Download the Kaggle dataset and place it under:
```bash
data/raw/us_economic_indicators.csv
```

Then track the raw file with DVC:
```bash
dvc add data/raw/us_economic_indicators.csv
git add data/raw/us_economic_indicators.csv.dvc .gitignore
git commit -m "Track raw macro dataset with DVC"
```

### 4. Run the baseline stages
```bash
python src/ingest.py --config configs/base.yaml
python src/validate.py --config configs/base.yaml
python src/features.py --config configs/base.yaml
python src/run_isolation_forest.py --config configs/isolation_forest.yaml
python src/run_factor_analysis.py --config configs/factor_analysis.yaml
python src/run_incremental_pca.py --config configs/incremental_pca.yaml
python src/run_changepoint.py --config configs/changepoint.yaml
```

Or run through DVC:
```bash
dvc repro
```

### 5. Compare experiments
```bash
dvc metrics show
dvc plots show
git log --oneline --decorate --graph
```

## Suggested Git tags
- `v0.1-data-baseline`
- `v0.2-iforest-baseline`
- `v0.3-factor-analysis`
- `v0.4-dimensionality-reduction`
- `v0.5-regime-analysis`

## Suggested experiment metadata
Each run should capture:
- `git_commit`
- `git_branch`
- `git_tag`
- `dvc_data_rev`
- `dataset_fingerprint`
- `config_name`
- `method_name`
- `timestamp`
- `metrics_path`
- `plots`

## Repo layout
```text
macro_pilot_project/
├── configs/
├── data/
├── docs/
├── metrics/
├── models/
├── notebooks/
├── plots/
├── reports/
├── src/
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```
