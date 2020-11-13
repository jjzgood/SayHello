import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = '!@#$EFQE3kd_*3393'
    SESSION_COOKIE_NAME = 'jjzgood'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(BaseConfig):
    DEBUG = True
    # 加载本地bootstrap
    BOOTSTRAP_SERVE_LOCAL = True
    # 配置数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
