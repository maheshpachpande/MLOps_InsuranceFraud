import sys
from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.exception import CustomException
from insurance_fraud_detection.components.data_ingestion import DataIngestion
from insurance_fraud_detection.components.data_validation import DataValidation
from insurance_fraud_detection.entity.config_entity import (DataIngestionConfig, DataValidationConfig)

from insurance_fraud_detection.entity.artifact_entity import (DataIngestionArtifact, DataValidationArtifact)


class TrainPipeline:
    def __init__(self):
        logging.info("Initializing TrainPipeline class")
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from MySQL database")
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys) from e

    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")
            

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys) from e
        
        

    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            if not data_validation_artifact.validation_status:
                raise Exception(f"Data validation failed with message: {data_validation_artifact.message}")
            

        except Exception as e:
            raise CustomException(e, sys)
        
