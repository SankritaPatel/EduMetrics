import sys
from src.EduMetrics.logger import logging
from src.EduMetrics.exception import CustomException
from src.EduMetrics.components.data_ingestion import DataIngestion
from src.EduMetrics.components.data_transformation import DataTransformation

if __name__=="__main__":
    logging.info("The execution has started...")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)