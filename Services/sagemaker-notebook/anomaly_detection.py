import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

data = pd.read_csv('path/to/transaction-data.csv')

data = data.dropna()

X = data[['amount']]

model = IsolationForest(contamination=0.05)
model.fit(X)

data['anomaly'] = model.predict(X)
data['anomaly'] = data['anomaly'].map({1: False, -1: True})

print(data[data['anomaly'] == True])

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data.index, y=data['amount'], hue=data['anomaly'], palette="coolwarm")
plt.title('Anomaly Detection in Transactions')
plt.xlabel('Transaction Index')
plt.ylabel('Transaction Amount')
plt.show()

data.to_csv('processed_transactions_with_anomalies.csv', index=False)
