from typing import ClassVar
class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True