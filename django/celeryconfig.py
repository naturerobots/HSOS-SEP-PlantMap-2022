# https://docs.celeryq.dev/en/4.0/userguide/configuration.html

broker_url = 'pyamqp://rabbitmq'
result_backend = 'rpc://'

# https://docs.celeryq.dev/en/4.0/userguide/routing.html
task_routes = {
    'rest-api.tasks.dl_pcloud': 'celery',  # Example routing, 'celery' is the default queue
}
