import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')
df.describe()
df.info()

sns.countplot(df.target,hue=df.sex, palette="Set3")
plt.title("Count of Diseases and not")
plt.xlabel("target")
plt.ylabel("Count")
plt.show()

conditions=[(df.chol<200),
            (df.chol<239),
            (df.chol<1000)]
choices=['low','natural','High']

df.chol=np.select(conditions, choices)
df.chol.tail(5)

sns.stripplot(x="chol", y="age",order=["low","natural","High"],data=df)
plt.ylabel("age")
plt.xlabel("levels of cholesterol")
plt.title('relation between age and type of cholesterol')
plt.show()
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

#Max heart rate achieved by age and sex
g = sns.lmplot(x="age", y="thalach", hue="sex", data=df)
sns.despine(left=True, bottom=True)
plt.show()

#Max heart rate achieved by age and kind
df.plot(x="age",y="thalach",kind="scatter", c="black", marker='^',alpha= 0.9)
plt.show()

#regression for all types of cholesterol
sns.lmplot(x="age", y="thalach", hue="sex", col="chol",data=df, height=6, aspect=.4, x_jitter=.1)
plt.show()