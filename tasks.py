from .celery_app import celery_app

print(celery_app.conf)

@celery_app.task
def hello_world():
    return 'Hello, World!'

