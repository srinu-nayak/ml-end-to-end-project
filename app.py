from sklearn.model_selection import train_test_split

from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from  src.mlproject.components.data_ingestion import  DataIngestion
from  src.mlproject.components.data_ingestion import  DataIngestionConfig

if __name__ == "__main__":
    logging.info('project has started')

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()


    except Exception as e:
        logging.error('custom exception occured')
        raise CustomException(e, sys)