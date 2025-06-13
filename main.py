from insurance_fraud_detection.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from insurance_fraud_detection.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from insurance_fraud_detection.logger import logging

STAGE_NAME = "Data Ingestion Stage"

try:
    logging.info(">>>>> Starting Full Pipeline <<<<<")

    # Stage 01: Ingestion
    ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_artifact = ingestion_pipeline.main(return_artifact=True)
    
except Exception as e:
    logging.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    # Stage 02: Validation
    validation_pipeline = DataValidationTrainingPipeline()
    validation_pipeline.main(data_ingestion_artifact=data_ingestion_artifact)

    logging.info(">>>>> Pipeline Finished Successfully <<<<<")
except Exception as e:
    logging.exception(e)
    raise e
