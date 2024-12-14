import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config/config.ini'))


class ConfigUtility:
    groq_api_key = config.get('GROQ', 'groq_api_key')