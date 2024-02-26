import os
import time

import numpy as np
import pandas as pd

import audb
import audiofile
import opensmile


if __name__ == "__main__":
    start_time = time.time()
    # Load csv with filenames and features into a dataframe
    filename_df = pd.read_csv('data/filename_features.csv')

    # Select a target list
    label_list = filename_df["Emotion"]

    # Initialize Smile - change features as you want
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals,
    )

    # Iterate and create a new dataframe
    processed_features = []
    for file in filename_df["Filename"]:
        # Read in the file
        signal, sampling_rate = audiofile.read(
            file,
            duration=4,
            always_2d=True,
        )

        # Process file using smile
        signals = smile.process_signal(
            signal,
            sampling_rate
        )
        # Store to list
        processed_features.append(signals)

    # Create new dataframe to save
    # Concatenate the processed features into a single DataFrame
    processed_df = pd.concat([pd.DataFrame(features, columns=list(smile.feature_names)) for features in processed_features], ignore_index=True)

    # Add targets
    processed_df["target"] = label_list

    # Save to csv
    processed_df.to_csv("data/processed_features.csv")

    # total time
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time}")


