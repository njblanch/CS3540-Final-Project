import pandas as pd
from sklearn.preprocessing import MinMaxScaler


if __name__ == "__main__":
    # Load data from csv
    data = pd.read_csv("data/processed_features.csv")
    data = data.drop(data.columns[0], axis=1)
    features = data.iloc[:, :-2]
    labels = data.iloc[:, -2:]


    # Normalize data
    # Initialize MinMaxScaler
    scaler = MinMaxScaler()

    # Fit and transform the data
    scaled_data = scaler.fit_transform(features)

    # Convert back to DataFrame
    scaled_df = pd.DataFrame(scaled_data, columns=features.columns)

    # Join data with labels
    joined_data = pd.concat([scaled_df, data.iloc[:, -2:]], axis=1)

    joined_data.to_csv("data/normalized_features.csv")

