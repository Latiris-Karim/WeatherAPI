import redis
from settings import settings



redis_url = settings.REDIS_URL
r = redis.Redis.from_url(redis_url, decode_responses=True)
       