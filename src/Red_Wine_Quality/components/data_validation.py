import pandas as pd
from Red_Wine_Quality.entity.config_entity import DataValidationConfig
from Red_Wine_Quality.config.configuration import ConfigurationManager



class DataValidation():
    def __init__(self,config: DataValidationConfig):
        self.config=config

    def validate_all_columns(self)-> bool:
        try:
            validate_col_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()
            

            for col in all_cols:
                if col not in all_schema:
                    validate_col_status=False
                    
                    with open(self.config.status_data_file,'w') as f:
                        f.write(f"Validation Status: {validate_col_status}")
                else:
                    validate_col_status=True
                    with open(self.config.status_data_file,'w') as f:
                        f.write(f"Validation Status: {validate_col_status}")
            
        
            return validate_col_status
        except Exception as e:
            raise e

    def validate_all_data_types(self) -> bool:
        try:
            validate_dtype_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_dtpyes=list(data.dtypes)
            all_schema=self.config.all_schema

            
        
            for dtype in (all_dtpyes):
                
                if dtype not in all_schema.values():
                    validate_dtype_status=False
                    with open(self.config.status_dtype_file,'w') as f:
                        f.write(f"Validation Status: {validate_dtype_status}")
                else:
                    validate_dtype_status=True
                    with open(self.config.status_dtype_file,'w') as f:
                        f.write(f"Validation Status: {validate_dtype_status}")
                
            
            

            return validate_dtype_status
        except Exception as e:
            raise e









    