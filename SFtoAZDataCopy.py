from DbConnection import getSnowFlakeConnectionSRC
from DbConnection import getAzureConnection

def SnowflakeToAzureDataCopy():
    try:              
        # SQL Database table name
        cursor_snowflake = getSnowFlakeConnectionSRC()
        cursor_azure = getAzureConnection()
        _table_name = "TESTCUSTOMER"
        _SQLQuery = "select * from OCA." + _table_name
        # Execute the SELECT query on Snowflake
        snowflake_rows= cursor_snowflake.execute(_SQLQuery).fetchall()
        # Execute the INSERT statements in Azure SQL Database
        for row in snowflake_rows:
            # Construct the INSERT statement dynamically based on the table structure
            values = ",".join([f"'{value}'" for value in row])
            insert_statement = f"INSERT INTO OCA.{_table_name} VALUES ({values})"
            #insert_statement.replace('None', '')
            print(insert_statement)
            try:
                cursor_azure.execute(insert_statement)
            except TabError as err:
                print(str(err))
        # Commit the changes in Azure SQL Database
        getAzureConnection.commit()
        cursor_azure.close()
        cursor_snowflake.close()
        return 1
    except:
        print("exiting...")


if __name__ == "__main__":
    SnowflakeToAzureDataCopy()
