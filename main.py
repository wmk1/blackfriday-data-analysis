import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sbn

import os

df = pd.read_csv('heart.csv')

df.sample(3)

temp_chest_pain = (df.groupby(['target']))['cp'].value_counts(normalize=True)\
.mul(100).reset_index(name = "percentage")
sbn.barplot(x = "target", y = "percentage", hue = "cp", data = temp_chest_pain)\
.set_title("Chest Pain vs Heart Disease")

temp_thal = (df.groupby(['target']))['thal'].value_counts(normalize=True)\
.mul(100).reset_index(name = "percentage")
sbn.barplot(x = "target", y = "percentage", hue = "thal", data = temp_thal)\
.set_title("thal vs Heart Disease")

"""
check attributes
"""
df.info()

sbn.heatmap(df.corr())
