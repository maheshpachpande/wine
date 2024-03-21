# mentioning the path  (Enitity)

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)  # unable to take any other variable
class DataIngestionConfig:
    root_dir: Path
    raw_data_path: Path
    # source_URL: str
    # local_data_file: Path
    # unzip_dir: Path
    
