import redis

# Connect to the Redis server
redis_host = 'redis'
redis_port = 6379
redis_db = 0

# Create a Redis client

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
