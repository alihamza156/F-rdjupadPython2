# data_handler.py
import pandas as pd

def read_data(file_path):
    """Läser in data från en CSV-fil."""
    return pd.read_csv(file_path)

def process_data(data):
    """Bearbetar datan (t.ex. filtrering av personer över 30 år)."""
    return data[data['age'] >= 30]
