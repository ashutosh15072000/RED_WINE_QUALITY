from Red_Wine_Quality.logging.logger import logger
from Red_Wine_Quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Red_Wine_Quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Red_Wine_Quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Red_Wine_Quality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation Stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e