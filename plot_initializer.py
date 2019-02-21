import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import util

class PlotInitializer():

   def generate_strip_plot(self, x_axis, y_axis, csv):
       sns.stripplot(x=x_axis, y=y_axis, order=["low", "natural", "High"], data=csv)
       plt.ylabel(util.Enum.value(y_axis))
       plt.xlabel("levels of cholesterol")
       plt.title('relation between age and type of cholesterol')
       plt.show()




