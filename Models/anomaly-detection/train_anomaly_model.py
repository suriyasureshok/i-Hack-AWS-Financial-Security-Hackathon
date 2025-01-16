import boto3
from sagemaker import get_execution_role
from sagemaker.sklearn import SKLearnModel
import pandas as pd

def load_transaction_data(file_path):
    return pd.read_csv(file_path)

def train_anomaly_model(data):
    pass

def save_anomaly_model(model, model_path):
    pass

def train_and_save_anomaly_model(file_path, model_path):
    data = load_transaction_data(file_path)
    model = train_anomaly_model(data)
    save_anomaly_model(model, model_path)
