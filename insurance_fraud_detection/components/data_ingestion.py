import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from insurance_fraud_detection.entity.config_entity import DataIngestionConfig
from insurance_fraud_detection.entity.artifact_entity import DataIngestionArtifact
from insurance_fraud_detection.exception import CustomException
from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.data_access.data import InsuranceData



class DataIngestion:
    
    logging.info("Data Ingestion started")
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            logging.info(f"Data Ingestion Config: {data_ingestion_config}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_into_feature_store(self)->DataFrame:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports data from MySQL to csv file
        
        Output      :   data is returned as artifact of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info(f"Exporting data from MySQL")
            usvisa_data = InsuranceData()
            dataframe = usvisa_data.export_collection_as_dataframe(table_name=
                                                                   self.data_ingestion_config.table_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise CustomException(e,sys)
        
    
    def split_data_as_train_test(self,dataframe: DataFrame) ->None:
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the dataframe into train set and test set based on split ratio 
        
        Output      :   Folder is created in ingested directory and train and test files are exported
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered split_data_as_train_test method of Data_Ingestion class")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test file path.")
            logging.info(f"Shape of train set: {train_set.shape}, Shape of test set: {test_set.shape}") 
        except Exception as e:
            raise CustomException(e, sys) from e
        
        
    def initiate_data_ingestion(self) ->DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()

            logging.info("Got the data from MySQL and exported it into feature store")
            if dataframe.empty:
                raise CustomException("Dataframe is empty. No data to process.", sys)

            self.split_data_as_train_test(dataframe)

            logging.info("Performed train test split on the dataset")

            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                            test_file_path=self.data_ingestion_config.testing_file_path)
            
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
# if __name__ == "__main__":
#     data_ingestion = DataIngestion()
#     data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
#     logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
#     logging.info("Data Ingestion completed successfully")