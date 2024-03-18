import pandas as pd
from sklearn.preprocessing import MinMaxScaler


if __name__ == "__main__":
    # Load data from csv
    data = pd.read_csv("data/processed_features.csv")
    data = data.drop(data.columns[0], axis=1)

    # Normalize data
    # Initialize MinMaxScaler
    scaler = MinMaxScaler()

    # Fit and transform the data
    scaled_data = scaler.fit_transform(data)

    # Convert back to DataFrame
    scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

    scaled_df.to_csv("data/normalized_features.csv")

