
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  DEBUG = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
  DEBUG = True

class TestingConfig(Config):
  DEBUG = True
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
  PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
  Debug = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


config_by_name = dict(
  dev=DevelopmentConfig,
  test=TestingConfig,
  prod=ProductionConfig
)

key = Config.SECRET_KEY
