from app import creat_app

app = creat_app()
app.app_context().push()

from tasks import celery