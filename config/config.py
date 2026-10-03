import yaml



class Config():

    def __init__(self):

        with open(file_path, "r", encoding="utf-8") as f: 
            config_data = yaml.safe_load(f)

        self.BUCKET_NAME = config_data["cloud"]["bucket_name"]
        
    def validate(self):
        ...


file_path = 
config = Config()