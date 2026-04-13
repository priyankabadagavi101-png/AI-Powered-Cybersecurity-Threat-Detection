import joblib
import pandas as pd
from src.preprocessing import preprocess_data

# load trained model
model = joblib.load("models/intrusion_model.pkl")

# load dataset
df = pd.read_csv("data/network_traffic.csv", header=None)

# keep original labels
labels = df.iloc[:, -1].unique()

# preprocess data
X, y = preprocess_data(df)

# take one sample
sample = X.iloc[[0]]

# predict
prediction = model.predict(sample)

# convert prediction to readable label
attack_type = labels[prediction[0]]

print("⚠ Detected Traffic Type:", attack_type)