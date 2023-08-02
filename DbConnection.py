import pyodbc
import snowflake.connector
import time
import sys

def getSnowFlakeConnectionSRC():
    try:
        connSF = snowflake.connector.connect(
            user="appseng",
            password="Magnitude123$",
            account="xw78863.ap-southeast-2",
            warehouse="COMPUTE_WH",
            database="SNFOCATESTDW",
            schema="OCA"
        )
        print("Snowflake Connection Status : Successful")
        return connSF.cursor()
    except snowflake.connector.Error as err:
        print("Error log :" + str(err))
        print("exiting...")
        time.sleep(5)
        sys.exit()

def getSnowFlakeConnectionTGT():
    try:
        connSF = snowflake.connector.connect(
            user="appseng",
            password="Magnitude123$",
            account="xw78863.ap-southeast-2",
            warehouse="COMPUTE_WH",
            database="SNFOCADEVDW",
            schema="OCA"
        )
        print("Snowflake Connection Status : Successful")
        return connSF.cursor()
    except snowflake.connector.Error as err:
        print("Error log :" + str(err))
        print("exiting...")
        time.sleep(5)
        sys.exit()


def getAzureConnection():
    try:
        server = 'ocapvo.database.windows.net'
        database = 'AZUREOCATESTDW'
        username = 'ocapvo'
        password = 'A40Dev123$'
        connAZ = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + server+ 
            ';PORT=1433;DATABASE=' + database + 
            ';UID=' + username + 
            ';PWD=' + password)
        print("Azure Connection Status : Successful")
        return connAZ.cursor()
    except pyodbc.Error as err:
        print("Error log :" + str(err))
        print("exiting...")
        time.sleep(5)
        sys.exit()
