import boto3
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

def load_spam_data(file_path):
    return pd.read_csv(file_path)

def train_spam_model(data):
    X = data.drop('label', axis=1)
    y = data['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)

def train_and_save_spam_model(file_path, model_path):
    data = load_spam_data(file_path)
    model = train_spam_model(data)
    save_model(model, model_path)
