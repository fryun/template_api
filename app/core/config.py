import os
import multiprocessing
import pathlib

from pydantic import BaseSettings

from app.core.utils.logger import get_logger


logger = get_logger(__name__)

class Config(BaseSettings):
    ENV: str = ""
    DEBUG = False
    
    APP_HOST = "0.0.0.0"
    APP_PORT = "7000"
    TIMEOUT = 30
    LOGLEVEL = "INFO"
    
    ROOT_DIR       = str(pathlib.Path(__file__).parent.parent.parent.absolute())

    os.environ['PYTHONPATH'] = os.pathsep.join([ROOT_DIR])


class AppConfig:
    '''get env variable'''
    def __init__(self) -> None:
        var_config = vars(Config())
        for key, value in var_config.items():
            self.__setattr__(key, value)
            
        env_vars = os.environ
        for key, value in env_vars.items():
            self.__setattr__(key, value)


config = AppConfig()


class GunicornConfig(BaseSettings):

    total_cpu = multiprocessing.cpu_count() * 2 + 1
    workers = total_cpu if total_cpu > 4 else 4
    
    BIND     = f"{config.APP_HOST}: {config.APP_PORT}"
    TIMEOUT  = config.TIMEOUT
    LOGLEVEL = config.LOGLEVEL
    WORKERS  = workers


gunicorn_config = GunicornConfig()

