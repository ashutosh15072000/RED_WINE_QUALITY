from Red_Wine_Quality.config.configuration import ConfigurationManager
from Red_Wine_Quality.components.data_validation import DataValidation
from Red_Wine_Quality.logging.logger import logger


STAGE_NAME="Data Validation Stage"

class DataValidationTrainingPipeline():
    def __init(self):
        pass


    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        data_validation.validate_all_data_types()



if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started <<<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

