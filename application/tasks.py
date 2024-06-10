import redis

from celery import shared_task, group

redis_host = 'redis'
redis_port = 6379
redis_db = 0
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)


@shared_task
def my_task():
    print("Task is running every minute!")
