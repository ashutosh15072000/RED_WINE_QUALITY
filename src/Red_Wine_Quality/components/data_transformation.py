from Red_Wine_Quality.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from Red_Wine_Quality.logging.logger import logger
import os
import pandas as pd


class DataTransformation():
    def __init__(self,config: DataTransformationConfig):
        self.config=config
        

    def train_test_spliting(self):
        data=pd.read_csv(self.config.data_path)
        train,test=train_test_split(data)
        

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splited Data into Training and Test Sets")
        logger.info(train.shape)
        logger.info(test.shape)