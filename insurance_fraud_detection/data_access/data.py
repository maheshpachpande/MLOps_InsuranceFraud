import sys
import pandas as pd
import numpy as np
from typing import Optional
from insurance_fraud_detection.configuration.mysql_conn import MySQLClient
from insurance_fraud_detection.exception import CustomException
from insurance_fraud_detection.logger import logging


class InsuranceData:
    """
    This class helps export the entire MySQL table as a pandas DataFrame.
    """
    logging.info("Initializing MySQLClient for InsuranceData...")
    def __init__(self):
        """
        Initialize MySQLClient to interact with the MySQL database.
        """
        try:
            
            # Initialize MySQLClient to establish a connection
            self.mysql_client = MySQLClient()
        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(self, table_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Export entire MySQL table as a pandas DataFrame.
        """
        try:
            logging.info(f"Exporting table '{table_name}' from database '{database_name}' as DataFrame...")
            
            # Determine the database to use
            db_name = database_name if database_name else self.mysql_client.database_name

            # FIXED QUERY
            query = f"SELECT * FROM {db_name}.{table_name};"

            # Execute and load data
            df = pd.read_sql_query(query, self.mysql_client.client)
            logging.info(f"Data exported successfully from table '{table_name}'.")
            logging.info(f"DataFrame shape: {df.shape}")

            # Clean up invalid values
            df.replace({"?": np.nan}, inplace=True)
            logging.info("Replaced '?' with NaN in DataFrame.")
            logging.info(f"DataFrame after cleaning: {df.head()}")

            return df

        except Exception as e:
            raise CustomException(e, sys)


# if __name__ == "__main__":
#     try:
#         # Example usage
#         insurance_data = InsuranceData()
#         df = insurance_data.export_collection_as_dataframe("insurancefraud_dataset")
#         print(df.head())  # Display the first few rows of the DataFrame
#     except Exception as e:
#         print(f"Error: {str(e)}")