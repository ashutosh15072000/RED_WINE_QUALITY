from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_data_file: str
    status_dtype_file: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path