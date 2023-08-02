from dbm import error
import sys
import snowflake.connector

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
        print("Source Snowflake Connection Status : Successful")
        return connSF.cursor()
    except snowflake.connector.Error as err:
        print("Error log :" + str(err))
        print("exiting...")
        sys.exit()
def getSnowFlakeConnectionTGT():
    try:
        connSF = snowflake.connector.connect(
            user="demomaster",
            password="Magnitude123$",
            account="lq29514.east-us-2.azure",
            warehouse="COMPUTE_WH",
            database="DEMO_DB",
            schema="OCA"
        )
        print("Target Snowflake Connection Status : Successful")
        return connSF.cursor()
    except snowflake.connector.Error as err:
        print("Error log :" + str(err))
        print("exiting...")
        sys.exit()

def SnowflakeToSFDataCopy():
    try:              
        # SQL Database table name
        conn_source = getSnowFlakeConnectionSRC()
        conn_tgt = getSnowFlakeConnectionTGT()
        source_database = 'SNFOCATESTDW'
        query_tables = "SHOW TABLES IN DATABASE "+ source_database
        source_tables =conn_source.execute(query_tables).fetchall()
        # Execute the query
        for row in source_tables:
            _table = row[1]
            if _table == 'ABCASSIGNMENTPVO':
                copy_statement = f"CREATE TABLE DEMO_DB.OCA.TEST{_table} CLONE SNFOCATESTDW.OCA.{_table}"
                conn_tgt.execute(copy_statement)
                print(_table + " cloned sucessfully")

        conn_source.close()
        conn_tgt.close()
        return 1
    except error as err:
        print("Error log :" + str(err))
        print("exiting...")


if __name__ == "__main__":
    SnowflakeToSFDataCopy()
