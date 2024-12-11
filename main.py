from TomatoDisease.components.prepare_base_model import PrepareBaseModel
from TomatoDisease.components.prepare_callbacks import PrepareCallback
from TomatoDisease.components.training import Training
from TomatoDisease.config.configuration import ConfigurationManager
from TomatoDisease.pipeline.data_ingestion_pipeline import DataIngestionTraningPipeline
from src.TomatoDisease import logger


logger.info("Welcome to tomato disease delection app")


STAGE_NAME = "Data Ingestion"


# if __name__ == "__main__":
#     try:
#         logger.info(f"Stage {STAGE_NAME} has started")
#         obj = DataIngestionTraningPipeline()
#         obj.main()
#         logger.info(f"Stage {STAGE_NAME} has finished")
#     except Exception as e:
#         logger.exception(e)
#         raise e


def main():
    config = ConfigurationManager()

    # Prepare Base Model
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.build_model()

    # Prepare Callbacks
    prepare_callbacks_config = config.get_prepare_base_model_config()
    prepare_callbacks = PrepareCallback(config=prepare_callbacks_config, tensorboard_log_dir="artifacts/tensorboard_log_dir")
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

    # Training
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list)

if __name__ == "__main__":
    main()
