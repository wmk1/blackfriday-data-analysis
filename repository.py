import sqlite3
import pandas as pd

from util import DataTranslators, DataTableElements


class HeartDiseasesRepository(object):

    connectionString = ""
    tableName = "disseases"

    def __init__(self, connectionString):
        self.connectionString = connectionString

    def createDbEntry(self):

        connection = sqlite3.connect(self.connectionString)

        with connection:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE " + self.tableName + "(id INTEGER PRIMARY KEY," +
                           DataTableElements.age.name + " INT, " +
                           DataTableElements.sex.name + " INT, " +
                           DataTableElements.cp.name + " INT, " +
                           DataTableElements.trestbps.name + " INT, " +
                           DataTableElements.chol.name + " INT, " +
                           DataTableElements.fbs.name + " INT, " +
                           DataTableElements.restecg.name + " INT, " +
                           DataTableElements.thalach.name + " INT, " +
                           DataTableElements.exang.name + " INT, " +
                           DataTableElements.oldpeak.name + " REAL, " +
                           DataTableElements.slope.name + " INT, " +
                           DataTableElements.ca.name + " INT," +
                           DataTableElements.thal.name + " INT," +
                           DataTableElements.target.name + " INT)")
            cursor.close()

    def inserData(self, df):

        connection = sqlite3.connect(self.connectionString)
        cursor = connection.cursor()

        with connection:
            for index, row in df.iterrows():

                ageValue = int(row[DataTableElements.age.name])
                sexValue = int(row[DataTableElements.sex.name])
                cpValue = int(row[DataTableElements.cp.name])
                trestbpsValue = int(row[DataTableElements.trestbps.name])
                cholValue = int(row[DataTableElements.chol.name])
                fbsValue = int(row[DataTableElements.fbs.name])
                restecgValue = int(row[DataTableElements.restecg.name])
                thalachValue = int(row[DataTableElements.thalach.name])
                exangValue = int(row[DataTableElements.exang.name])
                oldpeakValue = row[DataTableElements.oldpeak.name]
                slopeValue = int(row[DataTableElements.slope.name])
                caValue = int(row[DataTableElements.ca.name])
                thalValue = int(row[DataTableElements.thal.name])
                targetValue = int(row[DataTableElements.target.name])

                cursor.execute("INSERT INTO " + self.tableName + " VALUES(NULL, " +
                                str(ageValue) + "," +
                                str(sexValue) + "," +
                                str(cpValue) + "," +
                                str(trestbpsValue) + "," +
                                str(cholValue) + "," +
                                str(fbsValue) + "," +
                                str(restecgValue) + "," +
                                str(thalachValue) + "," +
                                str(exangValue) + "," +
                                str(oldpeakValue) + "," +
                                str(slopeValue) + "," +
                                str(caValue) + "," +
                                str(thalValue) + "," +
                                str(targetValue) + ")")

            cursor.close()


    def loadDbEntrys(self):

        connection = sqlite3.connect(self.connectionString)
        df = pd.read_sql_query('select * from ' + self.tableName, connection)

        return df
