import os
import sys
from datetime import date

# Secrete Credentials
DATABASE_NAME = "DATABASE_NAME"
HOST = "HOST"
USER = "USER"
PASSWORD = "PASSWORD"
TABLE_NAME = "TABLE_NAME"


PIPELINE_NAME = "insuranceFraudDetection"
ARTIFACT_DIR = "artifacts"
FILE_NAME = "raw_data.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

TARGET_COLUMN = "fraud_reported"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_TABLE_NAME: str = "insurancefraud_dataset"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"