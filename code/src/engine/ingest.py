import os
import pandas as pd
from sqlalchemy import create_engine

def read_input(path: str, table: str = None):
    """Read CSV or SQLAlchemy URL (requires table name for SQL reads)."""
    if os.path.exists(path) and path.lower().endswith('.csv'):
        return pd.read_csv(path, parse_dates=True)
    # try sqlalchemy URL
    if '://' in path:
        if not table:
            raise ValueError('For SQL inputs, provide a table name via function param.')
        engine = create_engine(path)
        with engine.connect() as conn:
            df = pd.read_sql_table(table, conn)
        return df
    raise ValueError('Unsupported input path. Provide a CSV path or SQLAlchemy URL.')
