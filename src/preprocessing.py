import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):

    # separate features and label
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # encode categorical columns
    for col in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # encode target labels
    le_y = LabelEncoder()
    y = le_y.fit_transform(y)

    return X, y