from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://rabbitmq')


@app.task
def add(x, y):
    return x + y
