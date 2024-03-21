
import os
# import urllib.request as request
# import zipfile
from mlProject import logger
from mlProject.utils.common import get_size, read_sql_data
from mlProject.config.configuration import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def get_data_from_sql(self):
        
        #df = pd.read_csv("notebook/data/EDA.csv")
        df = read_sql_data()
        logger.info("Read the data as DataFrame from MySQL.")


        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            
        df.to_csv(self.config.raw_data_path, index=False, header=True)
        logger.info("Reading Completed.")


    
    # def download_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         filename, headers = request.urlretrieve(
    #             url = self.config.source_URL,
    #             filename = self.config.local_data_file
    #         )
    #         logger.info(f"{filename} download! with following info: \n{headers}")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    
    # def extract_zip_file(self):
    #     """
    #     zip_file_path: str
    #     Extracts the zip file into the data directory
    #     Function returns None
    #     """
    #     unzip_path = self.config.unzip_dir
    #     os.makedirs(unzip_path, exist_ok=True)
    #     with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
    #         zip_ref.extractall(unzip_path)
