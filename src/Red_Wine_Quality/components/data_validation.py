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
                    
                    with open(self.config.status_file,'a') as f:
                        f.write(f"Validation(DATA) {col} Status: {validate_col_status}\n")
                else:
                    validate_col_status=True
                    with open(self.config.status_file,'a') as f:
                        f.write(f"Validation(DATA) {col} Status: {validate_col_status} \n")
            
        
            return validate_col_status
        except Exception as e:
            raise e

    def validate_all_data_types(self) -> bool:
        try:
            validate_dtype_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_dtpyes=list(data.dtypes)
            all_schema=self.config.all_schema

            list_schema_key=list(self.config.all_schema.keys())
            col=0
            for dtype in (all_dtpyes):
                
                if dtype not in all_schema.values():
                    validate_dtype_status=False
                    with open(self.config.status_file,'a') as f:
                        f.write(f"Validation(DTPYE) of {list_schema_key[col]} and dtpye {dtype} Status: {validate_dtype_status}\n")
                else:
                    validate_dtype_status=True
                    with open(self.config.status_file,'a') as f:
                        f.write(f"Validation(DTYPE) of {list_schema_key[col]} and dtpye {dtype} Status: {validate_dtype_status}\n")
                col=col+1
            
            

            return validate_dtype_status
        except Exception as e:
            raise e









    