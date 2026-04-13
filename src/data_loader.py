import pandas as pd

def load_data(path):

    df = pd.read_csv(path, header=None)

    print("Dataset loaded successfully")
    print("Shape:", df.shape)

    return df