from celery import Celery
import config 

def make_celery():
    celery = Celery(__name__, broker=config.CELERY_BROKER)
    celery.conf.update(config.as_dict())
    return celery

celery = make_celery()
