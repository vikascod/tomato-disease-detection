import os
import shutil
from TomatoDisease import logger

from TomatoDisease.components.data_ingestion import DataIngestion
from TomatoDisease.config.configuration import ConfigurationManager


STAGE_NAME = "Data Ingestion"

class DataIngestionTraningPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            shutil.move("artifacts/data_ingestion/data.zip/plant-village/PlantVillage", "artifacts/data_ingestion")
            shutil.rmtree("artifacts/data_ingestion/data.zip")
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} has started")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} has finished")
    except Exception as e:
        logger.exception(e)
        raise e
