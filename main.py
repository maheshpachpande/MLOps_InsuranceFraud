from insurance_fraud_detection.logger import logging
from insurance_fraud_detection.pipeline.prediction_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e
