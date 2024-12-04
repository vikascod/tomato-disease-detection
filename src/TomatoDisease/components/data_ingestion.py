import os
from pathlib import Path
import zipfile
import opendatasets as op

from TomatoDisease.entity.config_entity import DataIngestionConfig
from TomatoDisease import logger
from TomatoDisease.utils.helper import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self)-> str:
        '''
        Download data from the kaggle
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            op.download(dataset_url, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e

