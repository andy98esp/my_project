import redis

# Connect to the Redis server
redis_host = 'redis'
redis_port = 6379
redis_db = 0

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# Example 1: Save data in memory
redis_key = 'example_key'
redis_value = 'Hello, Redis!'

# Set a key-value pair in Redis
redis_client.set(redis_key, redis_value)

# Example 2: Get data from memory
# Retrieve the value for the specified key
retrieved_value = redis_client.get(redis_key)
print(f"Retrieved value: {retrieved_value.decode('utf-8')}")

# Example 3: More Redis functions
# Increment a numeric value stored at a key

# Return all variables redis
all_keys = redis_client.keys('*')
print(all_keys)

# Get the length of the value stored at a key
value_length = redis_client.strlen('example_key')

# Check if a key exists
key_exists = redis_client.exists('example_key')

# Delete a key
redis_client.delete('counter_key')

# Check again if the key exists after deletion
key_exists_after_deletion = redis_client.exists('example_key')

# Print the results
print(f"Updated value: {redis_client.get('example_key').decode('utf-8')}")
print(f"Value length: {value_length}")
print(f"Key exists before deletion: {key_exists}")
print(f"Key exists after deletion: {key_exists_after_deletion}")

print("Ahora vamos a hacer con hash")

redis_client_2 = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

redis_client_2.hset('my_hash', 'hola', 'adios')
redis_client_2.hset('my_hash', 'viva', 'españa')
redis_client_2.hset('my_hash', 'visca', 'catalunya')

get_redis_hash = redis_client_2.hgetall('my_hash')
for field, value in get_redis_hash.items():
    print((field.decode('utf-8'), value.decode('utf-8')))
