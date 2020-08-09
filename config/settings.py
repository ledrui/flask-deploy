
class BaseConfig():
    API_PREFIX = 'api'
    TEST = False
    DEBUG = False


class DevConfig(BaseConfig):
    FLASK_ENV = 'developement'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
    CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
    CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'

class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
   CELERY_BROKER = 'pyamqp://rabbit_user:rabbit_password@broker-rabbitmq//'
   CELERY_RESULT_BACKEND = 'rpc://rabbit_user:rabbit_password@broker-rabbitmq//'


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
   # make celery execute tasks synchronously in the same process
   CELERY_ALWAYS_EAGER = True
