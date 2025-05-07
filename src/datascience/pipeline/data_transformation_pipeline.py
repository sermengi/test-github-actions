from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline():
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        check_status = []
        try:
            with open('artifacts/data_validation/status.txt') as f:
                for line in f:
                    check_status.append(line.strip().split("Validation status:")[1].strip())
            if check_status == ["True"] * len(check_status):
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.transform_data()
            else:
                raise Exception("Data schema is not valid!!")
        
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e