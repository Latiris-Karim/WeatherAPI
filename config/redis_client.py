import redis
from config.env_settings import settings



redis_host = settings.REDISHOST
redis_port = settings.REDISPORT


r = redis.StrictRedis(host=redis_host, port=redis_port)
