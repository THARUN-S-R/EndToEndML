from EndToEndProject import logger
from EndToEndProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from EndToEndProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from EndToEndProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from EndToEndProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Data_Ingestion  = DataIngestionTrainingPipeline()
    Data_Ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e                                     

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Data_Validation  = DataValidationTrainingPipeline()
    Data_Validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e                                     

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Data_Transformation  = DataTransformationTrainingPipeline()
    Data_Transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Model_Trainer  = ModelTrainerTrainingPipeline()
    Model_Trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e  
