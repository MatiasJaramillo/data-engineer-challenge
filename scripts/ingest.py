import pandas as pd
import os

RAW_PATH = "data/raw"

def load_data():
    dataframes = {}

    for file in os.listdir(RAW_PATH):
        if file.endswith(".csv"):
            file_path = os.path.join(RAW_PATH, file)
            df = pd.read_csv(file_path)
            dataframes[file] = df
            print(f"Loaded {file} with shape {df.shape}")

    return dataframes


if __name__ == "__main__":
    data = load_data()