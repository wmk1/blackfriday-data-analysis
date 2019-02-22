import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plot_initializer as plot
from MLearningManager import MLearningManager
from repository import HeartDiseasesRepository
from util import DataTranslators


plot = plot.PlotInitializer()

df = pd.read_csv('heart.csv')

for index, row in df.iterrows():
    print(row[DataTranslators.ca.name])

df.describe()
df.info()

#iniciazlia bazy
hdRepository = HeartDiseasesRepository()
hdRepository.createDbEntry()
hdRepository.inserData(df)
loadedData = hdRepository.loadDbEntrys();

#machine learning data generation,learning and prediction
mlLearning = MLearningManager()
clf = mlLearning.predictData(loadedData)

#predictate data insert to data base
hdRepository.inserData(clf)

#wyplute dane oraz tabele

sns.countplot(clf.target,hue=clf.sex, palette="Set3")
plt.title("Count of Diseases and not")
plt.xlabel("target")
plt.ylabel("Count")
plt.show()

conditions=[(loadedData.chol<200),
            (loadedData.chol<239),
            (loadedData.chol<1000)]
choices=['low','natural','High']

loadedData.chol=np.select(conditions, choices)
loadedData.chol.tail(5)

#with hue seperate famales=0 and males=1
sns.stripplot(x="age",y="chol",data=df,order=["High","natural","low"],hue='sex')
plt.ylabel('levels of cholesterol')
plt.xlabel("age")
plt.title("relation between age and type of chol by gender")
plt.show()

#Age for different types of chest pain
plt.figure(figsize = (10,5))
plot = sns.boxplot(x = "cp", y = "age", data = df)
plot.set_title("Age  for different types of chest pain")
plt.show()

#Max heart rate actihieved by age and sex
g = sns.lmplot(x="age", y="thalach", hue="sex", data=df)
sns.despine(left=True, bottom=True)
plt.show()

#Max heart rate achieved by age and kind
df.plot(x="age",y="thalach",kind="scatter", c="black", marker='^',alpha= 0.9)
plt.show()

#Regression for all types of cholesterol
sns.lmplot(x="age", y="thalach", hue="sex", col="chol",data=df, height=6, aspect=.4, x_jitter=.1)
plt.show()
