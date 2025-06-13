import sys
from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.exception import CustomException
from insurance_fraud_detection.components.data_ingestion import DataIngestion
from insurance_fraud_detection.entity.config_entity import DataIngestionConfig

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self, return_artifact: bool = False):
        try:
            data_ingestion_config = DataIngestionConfig()
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

            if return_artifact:
                return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys) from e


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
