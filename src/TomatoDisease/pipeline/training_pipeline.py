from TomatoDisease import logger
from TomatoDisease.components.prepare_callbacks import PrepareCallback
from TomatoDisease.components.training import Training
from TomatoDisease.config.configuration import ConfigurationManager


STAGE_NAME = "Model Training"

class ModelTrainingPipeline:

    def main(self):
        try:
            # Callback pipeline
            config = ConfigurationManager()
            prepare_callback_config = config.get_prepare_callback_config()
            prepare_callback = PrepareCallback(config=prepare_callback_config)
            callback_list = prepare_callback.get_tb_ckpt_callbacks()

            # Training pipeline
            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list=callback_list)
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} has started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} has finished")
    except Exception as e:
        logger.exception(e)
        raise e
