from typing import Dict, Any
import pandas as pd

def summarize_data(df: pd.DataFrame) -> Dict[str, Any]:
    summary = {}
    summary['rows'] = int(df.shape[0])
    summary['cols'] = int(df.shape[1])
    summary['dtypes'] = df.dtypes.astype(str).to_dict()
    summary['missing'] = df.isnull().sum().to_dict()
    numeric = df.select_dtypes(include='number')
    if not numeric.empty:
        summary['numeric_stats'] = numeric.describe().to_dict()
    # try KPIs (case-insensitive)
    for candidate in ['impressions','clicks','spend','revenue']:
        matches = [c for c in df.columns if c.lower()==candidate]
        if matches:
            col = matches[0]
            summary[candidate] = {
                'sum': float(df[col].sum(skipna=True)),
                'mean': float(df[col].mean(skipna=True)),
                'max': float(df[col].max(skipna=True)),
            }
    return summary
