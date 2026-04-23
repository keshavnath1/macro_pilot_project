# Experiment Comparison Report

## Objective
Establish a reproducible macroeconomic analytics workflow that supports exploratory analysis, anomaly detection, latent factor discovery, dimensionality reduction, and time-based regime detection before data is consumed by Monte Carlo simulation.

## Recommended pilot dataset
**US Economic Indicators (1991–2023)**

## Methods in scope
| Method | Primary role | Main output | Strength | Limitation |
|---|---|---|---|---|
| Isolation Forest | anomaly detection | anomaly scores, flagged windows | scales well on tabular data | less directly interpretable than factor methods |
| Factor Analysis | latent macro drivers | factor loadings and scores | interpretable and compact | linear assumption |
| Autoencoder | nonlinear anomaly detection | reconstruction error | captures nonlinear patterns | more complex and less explainable |
| Incremental PCA | large-scale dimensionality reduction | principal components | efficient for large numeric matrices | may miss nonlinear structure |
| Change Point Detection | regime / break analysis | break dates and segments | highly useful for time-aware diagnosis | sensitive to smoothing and penalty choice |

## Evaluation dimensions
- interpretability
- reproducibility
- scalability
- time-awareness
- ease of operationalization
- suitability for simulation input review

## Suggested findings template
### Isolation Forest
- Top anomalous periods:
- Potential macro events aligned:
- Follow-up needed:

### Factor Analysis
- Factor 1 interpretation:
- Factor 2 interpretation:
- Variables with strongest loadings:

### Incremental PCA
- Cumulative explained variance:
- Recommended retained dimension:
- Downstream use:

### Change Point Detection
- Major break dates:
- Segment interpretation:
- Business impact:

## Decision template
Proceed with:
- baseline production candidate:
- methods reserved for deeper analysis:
- additional data quality checks to add:
