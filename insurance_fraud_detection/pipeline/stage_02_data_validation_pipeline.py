import sys
from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.exception import CustomException
from insurance_fraud_detection.components.data_validation import DataValidation
from insurance_fraud_detection.entity.config_entity import DataValidationConfig
from insurance_fraud_detection.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self, data_ingestion_artifact):
        try:
            data_validation_config = DataValidationConfig()
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"Data Validation Artifact: {data_validation_artifact}")
        except Exception as e:
            raise CustomException(e, sys) from e


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_artifact = ingestion_pipeline.main(return_artifact=True)

        validation_pipeline = DataValidationTrainingPipeline()
        validation_pipeline.main(data_ingestion_artifact=data_ingestion_artifact)

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
