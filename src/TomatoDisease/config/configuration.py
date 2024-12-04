import os

from TomatoDisease.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TomatoDisease.entity.config_entity import DataIngestionConfig
from TomatoDisease.utils.helper import create_directories, read_yaml


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion
