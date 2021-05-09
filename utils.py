from dotenv import load_dotenv
from os.path import join, dirname
import os


class EnvVars():
    def __init__(self):
        self.ACCESS_TOKEN = ''
        self.REFRESH_TOKEN = ''
        self.CLIENT_ID = ''

        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        self.ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
        self.REFRESH_TOKEN = os.environ.get("REFRESH_TOKEN")
        self.CLIENT_ID = os.environ.get("CLIENT_ID")

