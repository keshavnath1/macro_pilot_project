# Visual Appendix

## Recommended visuals
1. **Dataset timeline**
   - show historical coverage and data frequency
2. **Missingness heatmap**
   - display missing value concentration by variable and time
3. **Correlation heatmap**
   - show macro variable clusters before factor modeling
4. **Isolation Forest anomaly timeline**
   - anomaly score by date, with top flagged periods annotated
5. **Factor loadings heatmap**
   - variables by factor
6. **Explained variance curve**
   - cumulative variance retained by Incremental PCA
7. **Change point timeline**
   - primary series with break dates
8. **Git + DVC lineage diagram**
   - Git commit + config + DVC data rev + metrics + plots
9. **Pipeline architecture diagram**
   - ingest → validate → features → method stages → summarize
10. **Experiment comparison matrix**
   - compare method tradeoffs

## Plot naming convention
- `plots/data_timeline.png`
- `plots/missingness_heatmap.png`
- `plots/correlation_heatmap.png`
- `plots/iforest_timeline.png`
- `plots/factor_loadings_heatmap.png`
- `plots/ipca_explained_variance.png`
- `plots/changepoint_timeline.png`
- `plots/git_dvc_lineage.png`
- `plots/pipeline_architecture.png`
- `plots/experiment_matrix.png`

## Annotation guidance
- annotate severe anomalies
- label factor groups in plain business language
- keep legends minimal
- prefer clear date windows over dense tick marks
