from TomatoDisease.pipeline.data_ingestion_pipeline import DataIngestionTraningPipeline
from src.TomatoDisease import logger


logger.info("Welcome to tomato disease delection app")


STAGE_NAME = "Data Ingestion"


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} has started")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} has finished")
    except Exception as e:
        logger.exception(e)
        raise e