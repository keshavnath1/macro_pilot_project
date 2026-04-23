# Building a Reproducible Macroeconomic Analytics Framework with Git, DVC, and Machine Learning

## Subtitle
Using anomaly detection, latent factor modeling, dimensionality reduction, and regime-shift analysis to support structured macroeconomic simulation workflows

## 1. Introduction
Macroeconomic forecasting and simulation workflows often rely on structured economic indicators, predefined formulas, and Monte Carlo simulation to estimate future outcomes. These approaches are useful because they preserve interpretability, but the surrounding workflow is often fragmented: data quality issues are hard to detect, experiments are not always reproducible, and teams may lack a structured way to compare analytical methods. The goal of this project is to design a repeatable framework where Git tracks code and experiment intent, DVC tracks datasets and metrics, and machine learning methods help identify anomalies, latent drivers, dimensionality-reduction opportunities, and regime changes in macroeconomic data.

## 2. Problem Statement
Data scientists currently work with macroeconomic data and formula-driven simulation models, but the process lacks a structured experimentation framework for data quality analysis, feature discovery, anomaly detection, and versioned collaboration. Because macroeconomic data can be noisy, correlated, incomplete, and time-sensitive, the team needs a reproducible workflow that supports interpretable analysis while preserving the logic of existing Monte Carlo simulation processes.

### One-line version
How might we build a reproducible and interpretable macroeconomic analytics workflow that helps teams detect anomalies, uncover latent drivers, reduce dimensionality, and monitor regime shifts before using data in Monte Carlo simulation?

## 3. Requirements
- **Interpretability**: The workflow must support methods that economists and data scientists can explain, especially when results affect assumptions used in simulation.
- **Reproducibility**: Every experiment should be tied to a Git commit, config version, DVC data version, and metrics output.
- **Scalability**: The framework should handle large tabular macroeconomic datasets without requiring expensive full-memory workflows.
- **Time-awareness**: Because macroeconomic data evolves over time, the workflow must support time-based analysis such as regime change detection and rolling comparisons.
- **Transparency**: The output should include visuals, metrics, and method-specific diagnostics so the team can understand why a method flagged something.
- **Extensibility**: The framework should allow additional methods later without redesigning the whole pipeline.

## 4. Nonrequirements
- The project is **not** intended to replace existing Monte Carlo simulation formulas.
- It is **not** intended to label every individual record as correct or incorrect.
- It is **not** trying to prove that one model should replace all statistical methods.
- It is **not** intended to be a real-time streaming system in phase 1.
- It is **not** a black-box-only workflow; methods should remain explainable.

## 5. Analytical Questions We Want to Answer
1. Are there unusual periods or observations in the macroeconomic dataset that should be investigated before simulation?
2. Can we identify a smaller set of interpretable latent macro drivers?
3. Can we reduce dimensionality while preserving useful signal?
4. Are there structural breaks or regime shifts in the time series?
5. Can these analyses be run in a repeatable Git + DVC workflow for team use?

## 6. Method Selection Framework
### 6.1 Anomaly detection on large tabular macro data
**Method:** Isolation Forest  
**Purpose:** Find unusual macroeconomic periods or feature combinations.

### 6.2 Interpretable latent macro drivers
**Method:** Factor Analysis  
**Later extension:** Dynamic Factor Models  
**Purpose:** Discover common hidden drivers behind correlated macro variables.

### 6.3 Nonlinear anomaly detection
**Method:** Autoencoder  
**Purpose:** Detect complex nonlinear deviations not well captured by linear methods.

### 6.4 Large-scale dimensionality reduction
**Method:** Incremental PCA or Random Projection  
**Purpose:** Compress correlated inputs into a smaller representation efficiently.

### 6.5 Time-based regime and trend changes
**Method:** Change Point Detection or State Space Models  
**Purpose:** Identify structural breaks, trend shifts, or volatility regime changes.

## 7. Dataset Selection
A Kaggle macroeconomic dataset will be used as the initial pilot dataset because it provides a convenient, shareable, and reproducible starting point for building the workflow. The selected dataset should be large enough to support anomaly detection, factor modeling, and time-based comparisons, while still being manageable for a first Git + DVC implementation.

### Recommended pilot dataset
- **Dataset**: US Economic Indicators (1991–2023)
- **Why**: tabular, time-based, broad enough for anomaly/factor/regime analyses, simple enough for a first Git + DVC pilot
- **Use**: baseline dataset for preprocessing, exploratory plots, anomaly detection, factor analysis, dimensionality reduction, and change-point analysis

## 8. Workflow Architecture: Git + DVC
### Git responsibilities
Git will track:
- code
- configs
- experiment logic
- notebooks/scripts
- tags and releases
- documentation

### DVC responsibilities
DVC will track:
- raw dataset versions
- processed datasets
- metrics files
- plots
- model artifacts
- experiment outputs

### Common experiment metadata
Every run should record:
- git commit
- git branch
- git tag
- dvc data revision
- config name
- method name
- timestamp
- dataset fingerprint
- output metrics path

## 9. Repo Structure
```text
macro-analytics-pilot/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── src/
│   ├── ingest.py
│   ├── validate.py
│   ├── features.py
│   ├── run_isolation_forest.py
│   ├── run_factor_analysis.py
│   ├── run_autoencoder.py
│   ├── run_incremental_pca.py
│   ├── run_changepoint.py
│   └── summarize_results.py
├── configs/
│   ├── base.yaml
│   ├── isolation_forest.yaml
│   ├── factor_analysis.yaml
│   ├── autoencoder.yaml
│   ├── incremental_pca.yaml
│   └── changepoint.yaml
├── metrics/
├── plots/
├── models/
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```

## 10. Pipeline Stages
1. Ingest
2. Validate
3. Clean
4. Feature engineer
5. Run Isolation Forest
6. Run Factor Analysis
7. Run Autoencoder
8. Run Incremental PCA
9. Run Change Point Detection
10. Summarize and compare

## 11. Data Preparation and Feature Engineering
Because macroeconomic variables are often correlated and measured on different scales, preprocessing will include normalization, missing-value handling, and time-aware feature construction such as lags and rolling statistics. These engineered views help support both interpretability-focused models and anomaly-detection methods.

## 12. Method Sections
### 12.1 Isolation Forest
- **Purpose**: Detect anomalous time periods or feature combinations in macro data.
- **Outputs**: anomaly scores, flags, ranked anomalous periods.
- **Plots**: anomaly score distribution, anomaly timeline, top anomalous periods table.
- **Business interpretation**: Highlights dates or windows where the macro profile differs significantly from typical history.

### 12.2 Factor Analysis
- **Purpose**: Identify interpretable latent macro drivers.
- **Outputs**: factor loadings, factor scores, communalities.
- **Plots**: loading heatmap, factor importance plot, factor score timeline.
- **Interpretation**: Shows which observed variables move together and what latent economic dimensions may exist.

### 12.3 Autoencoder
- **Purpose**: Capture nonlinear anomaly structure.
- **Outputs**: reconstruction loss, anomaly ranking, thresholded anomalies.
- **Plots**: train vs validation loss, reconstruction error histogram, high-error timeline.
- **Interpretation**: Identifies periods poorly reconstructed by the learned nonlinear pattern.

### 12.4 Incremental PCA / Random Projection
- **Purpose**: Provide scalable dimensionality reduction.
- **Outputs**: reduced components, explained variance, transformed dataset.
- **Plots**: cumulative explained variance, first-component scatter, dimensionality vs retained signal chart.
- **Interpretation**: Supports compression of macro features before simulation or downstream analysis.

### 12.5 Change Point Detection / State Space
- **Purpose**: Detect structural breaks and shifts over time.
- **Outputs**: detected change dates, segment summaries, trend/state estimates.
- **Plots**: time series with marked change points, regime segmentation chart, trend and residual chart.
- **Interpretation**: Helps identify when the macro environment moved into a new regime.

## 13. Experiment Tracking Design
Each experiment produces:
- config file
- metrics JSON
- plots
- optional model file
- run summary JSON

### Example run summary
```json
{
  "method": "isolation_forest",
  "git_commit": "abc123",
  "git_branch": "feature/iforest-baseline",
  "git_tag": "v0.2-iforest",
  "dvc_data_rev": "def456",
  "config_file": "configs/isolation_forest.yaml",
  "metrics_file": "metrics/isolation_forest_metrics.json",
  "plots": [
    "plots/iforest_score_distribution.png",
    "plots/iforest_timeline.png"
  ],
  "timestamp": "2026-04-19T10:45:00"
}
```

## 14. Evaluation Framework
Suggested comparison dimensions:
- interpretability
- scalability
- sensitivity to anomalies
- usefulness for trend structure
- usefulness for simulation prep
- computational cost
- ease of explanation

## 15. Visual Storytelling Section
Recommended plots:
1. Data coverage and timeline
2. Missingness heatmap
3. Correlation heatmap
4. Factor loading heatmap
5. Isolation Forest anomaly timeline
6. Autoencoder reconstruction error plot
7. Explained variance curve
8. Change point timeline
9. Experiment comparison summary chart
10. Git + DVC lineage diagram

## 16. Pseudocode Section
```python
def run_macro_experiment(dataset_path, config):
    data = load_data(dataset_path)
    data_clean = preprocess(data, config["preprocessing"])
    features = engineer_features(data_clean, config["features"])

    results = {}

    if config["run_isolation_forest"]:
        results["isolation_forest"] = run_isolation_forest(features)

    if config["run_factor_analysis"]:
        results["factor_analysis"] = run_factor_analysis(features)

    if config["run_autoencoder"]:
        results["autoencoder"] = run_autoencoder(features)

    if config["run_incremental_pca"]:
        results["incremental_pca"] = run_incremental_pca(features)

    if config["run_changepoint"]:
        results["changepoint"] = run_changepoint_analysis(features)

    save_metrics(results)
    save_plots(results)
    save_run_metadata(results, git_info(), dvc_info(), config)

    return results
```

## 17. Risks and Practical Considerations
- macroeconomic data may have strong correlation and seasonality
- anomaly does not always mean error
- latent factors may be statistically useful but hard to name
- change-point methods may overreact without smoothing
- autoencoders may reduce interpretability
- dataset choice may limit generalization
- Git + DVC adoption requires team discipline

## 18. Final Outcome
The outcome of this project is not just a set of model results, but a repeatable analytical framework. By combining Git for experiment logic and DVC for data and artifact versioning, the team can compare methods, preserve reproducibility, and build a structured foundation for macroeconomic analytics that supports, rather than replaces, existing Monte Carlo simulation workflows.

## 19. Deliverables
- 1 notebook for exploration
- 1 structured repo with Git + DVC
- 1 experiment comparison report
- 1 slide deck
- 1 README with reproducibility steps
- 1 metrics summary table
- 1 visual appendix
