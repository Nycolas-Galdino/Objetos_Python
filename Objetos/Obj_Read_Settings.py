import os
import yaml


class Read_Settings:
    def read_settings(file) -> dict:
        with open(os.path.abspath(file), 'r') as stream:
            return yaml.load(stream, yaml.FullLoader)
