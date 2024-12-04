from TomatoDisease import logger
from TomatoDisease.components.prepare_base_model import PrepareBaseModel
from TomatoDisease.config.configuration import ConfigurationManager


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTraningPipeline:

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} has started")
        obj = PrepareBaseModelTraningPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} has finished")
    except Exception as e:
        logger.exception(e)
        raise e
