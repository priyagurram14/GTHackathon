import matplotlib.pyplot as plt
import pandas as pd
import os

def _chart_output_dir():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'outputs', 'charts'))
    os.makedirs(root, exist_ok=True)
    return root

def create_line_chart(df: pd.DataFrame, x_col: str, y_col: str, output_path: str):
    plt.figure(figsize=(8,4))
    try:
        series_x = pd.to_datetime(df[x_col])
    except Exception:
        series_x = df[x_col]
    plt.plot(series_x, df[y_col], marker='o')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} over {x_col}")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def create_bar_chart(df: pd.DataFrame, category: str, value: str, output_path: str):
    plt.figure(figsize=(8,4))
    grouped = df.groupby(category)[value].sum()
    grouped.plot(kind='bar')
    plt.xlabel(category)
    plt.ylabel(value)
    plt.title(f"{value} by {category}")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
