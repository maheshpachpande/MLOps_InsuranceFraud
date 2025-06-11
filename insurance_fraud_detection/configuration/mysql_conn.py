import sys
import os
import pymysql
import certifi
from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.exception import CustomException
# importing environment variables for MySQL connection
from insurance_fraud_detection.constants import (DATABASE_NAME,
                                                HOST,
                                                USER,    
                                                PASSWORD)

import warnings
warnings.filterwarnings("ignore")



# making a secure (SSL/TLS) connection to a MySQL server.
ca = certifi.where()

class MySQLClient:
    """
    Class Name :   MySQLClient
    Description :  This class establishes a connection to the MySQL database and can be used to export data 
                   from the MySQL feature store. # SELECT * FROM mlops.insurancefraud_dataset;
    """
    client = None

    def __init__(self) -> None:
        try:
            logging.info("Connecting to MySQL database...")
            # Check if the client is already initialized
            if MySQLClient.client is None:
                database_name = os.getenv(DATABASE_NAME)
                host = os.getenv(HOST)
                user = os.getenv(USER)
                password = os.getenv(PASSWORD)
                
                # Validate that all required environment variables are set
                if not all([host, user, password, database_name]):
                    raise ValueError("Missing required environment variables.")

                # Establishing the connection to the MySQL database
                # Using SSL/TLS for secure connection
                mydb = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    db=database_name
                )

                # Assigning the client to the class variable
                MySQLClient.client = mydb

            self.client = MySQLClient.client
            self.database_name = os.getenv(DATABASE_NAME)
            logging.info("MySQL database connection established successfully.")

            

        except Exception as e:
            raise CustomException(e, sys)


# if __name__ == "__main__":
#     try:
#         obj = MySQLClient()  # instantiate the class
#         print("Client object:", obj.client)  # verify connection object
#     except Exception as e:
#         print("Failed to connect:", str(e))