import os
import pandas as pd


# Split the filename on the '-' character
def extract_numerical_values(filename):
    filename = filename.strip(".wav")
    parts = filename.split('-')
    return [int(part) for part in parts]


# Extract the features from the filename
folder_path = "data"
numerical_data = []
for folder in os.listdir(folder_path):
    print(folder)
    if os.path.isdir(folder_path + "/" + folder):
        for filename in os.listdir(folder_path + "/" + folder):
            print(filename)
            if filename.endswith(".wav"):
                numerical_values = extract_numerical_values(filename)
                numerical_data.append([filename] + numerical_values)

# Create DataFrame
columns = ['Filename', 'Modality', 'Vocal Channel', 'Emotion', 'Emotional Intensity', 'Statement', 'Repetition', 'Actor']
df = pd.DataFrame(numerical_data, columns=columns)
df = df[['Filename', 'Modality', 'Vocal Channel', 'Statement', 'Repetition', 'Actor', 'Emotion', 'Emotional Intensity']]

# Display DataFrame
print(df.head())

# Save DataFrame to CSV
df.to_csv("data/filename_features.csv", index=False)

