import os
import time

import numpy as np
import pandas as pd

import audb
import audiofile
import opensmile



file = "data/Actor_01/03-01-01-01-01-01-01.wav"
signal, sampling_rate = audiofile.read(
    file,
    duration=4,
    always_2d=True,
)

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)
print(smile.feature_names)

signals = smile.process_signal(
    signal,
    sampling_rate
)

print(signals)








