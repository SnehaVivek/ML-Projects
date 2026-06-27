from source.components.data_ingestion import DataIngestion
from source.components.data_transformation import DataTransformation
from source.logger import logging

class TrainPipeline:
    def __init__(self):
        pass
    
    def initiate_train_pipeline(self):
        logging.info("Starting training pipeline")
        try:
            # Data Ingestion
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train data: {train_data_path}, Test data: {test_data_path}")
            
            # Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
            logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")
            
            # TODO: Add model training
            
        except Exception as e:
            logging.error(f"Error in train pipeline: {str(e)}")
            raise

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.initiate_train_pipeline()
