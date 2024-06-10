from celery import Celery
from celery.schedules import crontab


app = Celery(
    'application',
    include=['application.tasks', ]
)

app.conf.task_routes = {
    'application.tasks.*': {
        'queue': 'tasks-queue'
    },
}

app.conf.beat_schedule = {
    'task-every-minute': {
        'task': 'application.tasks.my_task',
        'schedule': crontab(minute='*'),
    },
}

app.set_default()

app.conf.timezone = 'UTC'

app.conf.update(
    broker_connection_retry_on_startup=True,
    result_expires=3600,
    broker_transport_options={'max_retries': 5, 'interval_start': 0, 'interval_step': 2, 'interval_max': 30},
)

app.autodiscover_tasks()


if __name__ == '__main__':
    app.start()
