import redis
from config.env_settings import settings



redis_host = settings.redis_host
redis_port = settings.redis_port
#r = redis.Redis.from_url(redis_url, decode_responses=True)

r = redis.StrictRedis(host=redis_host, port=redis_port)
