import pandas as pd

def load_transaction_data(file_path):
    return pd.read_csv(file_path)

def clean_transaction_data(data):
    data.dropna(inplace=True)
    data = data[data['amount'] > 0]
    return data

def preprocess_transactions(file_path):
    data = load_transaction_data(file_path)
    cleaned_data = clean_transaction_data(data)
    return cleaned_data
