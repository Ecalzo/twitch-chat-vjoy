from configparser import ConfigParser

def get_config() -> ConfigParser:
    config = ConfigParser()
    config.read("config.ini")
    return config
