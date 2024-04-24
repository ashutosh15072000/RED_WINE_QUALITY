from Red_Wine_Quality.entity.config_entity import DataTransformationConfig
from pathlib import Path
from Red_Wine_Quality.config.configuration import ConfigurationManager
from Red_Wine_Quality.components.data_transformation import DataTransformation
from Red_Wine_Quality.logging.logger import logger


STAGE_NAME="Data Transformation Stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\data_status.txt")) as f:
                data_status=f.read().split(" ")[-1]
            with open(Path("artifacts\data_validation\dtype_status.txt")) as f1:
                dtype_status=f1.read().split(" ")[-1]
                
            
            if (data_status=="True")  and (dtype_status=="True") :
                 config=ConfigurationManager()
                 data_transformation_config=config.get_data_transformation_config()
                 data_transformation=DataTransformation(config=data_transformation_config)
                 data_transformation.train_test_spliting()
            else:
                 raise Exception ("Your Data schema is not valid")
        except Exception as e:
            raise e
        

if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>  {STAGE_NAME} started <<<<<<<<")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>  {STAGE_NAME} Completed <<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


        
        