import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sbn

import os

df = pd.read_csv('heart.csv')

df.sample(3)