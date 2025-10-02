import os
from settings.settings_conf import PATH_DOTENV
from dotenv import load_dotenv


## Carrega configuração da API
class API():
    load_dotenv(PATH_DOTENV)
    API_KEY = os.getenv('API_KEY')