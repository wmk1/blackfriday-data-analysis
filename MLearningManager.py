from sklearn import tree
import numpy as np
import pandas as pd
from random import randint

from util import DataTableElements


class MLearningManager(object):

    def learnOnDiseaseData(self, dataFrameSql):

        dataArray = np.empty((0, 13), float)
        predicates = []
        for index, row in dataFrameSql.iterrows():
            dataArray = np.append(dataArray, np.array(
                [[row[DataTableElements.age.name],
                  row[DataTableElements.sex.name],
                  row[DataTableElements.cp.name],
                  row[DataTableElements.trestbps.name],
                  row[DataTableElements.chol.name],
                  row[DataTableElements.fbs.name],
                  row[DataTableElements.restecg.name],
                  row[DataTableElements.thalach.name],
                  row[DataTableElements.exang.name],
                  row[DataTableElements.oldpeak.name],
                  row[DataTableElements.slope.name],
                  row[DataTableElements.ca.name],
                  row[DataTableElements.thal.name]]]), axis=0)
            predicates.append(row[DataTableElements.target.name])

        clf = tree.DecisionTreeClassifier()
        clf.fit(dataArray, predicates)
        return clf

    def loadPredictateData(self):

        dataArray = np.empty((0, 13), float)
        for x in range(10000):
            dataArray = np.append(dataArray, np.array(
                [[randint(30, 70), randint(0, 1), randint(0, 3), randint(100 , 200), randint(177, 500),
                  randint(0, 1), randint(0, 1), randint(0, 1), randint(90, 187), randint(0, 1), randint(0, 3), randint(0, 2), randint(0,3)]]), axis=0)

        return dataArray

    def predictData(self, sqlData):
        clf = self.learnOnDiseaseData(sqlData)
        predicateData = self.loadPredictateData()
        predicateResult = clf.predict(predicateData)

        dataOnDeepLearning = self.setDataElements(predicateData, predicateResult)
        return dataOnDeepLearning

    def setDataElements(self, predicateData, predicateResult):

        dataElements = pd.DataFrame({'age': [], 'sex': [], 'cp': [], 'trestbps': [],'chol': [], 'fbs': [],'restecg': [],
                                     'thalach': [],'exang': [], 'oldpeak': [],'slope': [], 'ca': [], 'thal': [], 'target': []})

        for i in range(len(predicateData)):
            dataElements = dataElements.append({'age': predicateData[i][0],
                                                'sex': predicateData[i][1],
                                                'cp': predicateData[i][2],
                                                'trestbps': predicateData[i][3],
                                                'chol': predicateData[i][4],
                                                'fbs': predicateData[i][5],
                                                'restecg': predicateData[i][6],
                                                'thalach': predicateData[i][7],
                                                'exang': predicateData[i][8],
                                                'oldpeak': predicateData[i][9],
                                                'slope': predicateData[i][10],
                                                'ca': predicateData[i][11],
                                                'thal': predicateData[i][12],
                                                'target': predicateResult[i],
                                                }, ignore_index=True)

        return dataElements
