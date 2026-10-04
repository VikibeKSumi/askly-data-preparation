import yaml
from pathlib import Path

class Config():

    def __init__(self, file_path: Path):

        with open(file_path, "r", encoding="utf-8") as f: 
            config_data = yaml.safe_load(f)
        self.BUCKET_NAME = config_data["cloud"]["bucket_name"]
        self.RAW_PREFIX = config_data["cloud"]["raw_prefix"]
        self.CLEAN_PREFIX = config_data["cloud"]["clean_prefix"]
        
    def validate(self):
        ...


file_path = Path(__file__).parent/"config.yaml"
config = Config(file_path)