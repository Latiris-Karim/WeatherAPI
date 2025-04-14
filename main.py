from fastapi import FastAPI
from Weather_logic import location_time
import logging
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
import json
from config.redis_client import r
from config.secrets_manager import get_secrets
from dotenv import load_dotenv

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)
limiter = Limiter(key_func=get_remote_address, default_limits=["10/minute"])
 
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)
get_secrets()
load_dotenv()

@app.get("/weather/")
async def weathercall(city: str, timespan: str):
    weather = city + timespan
    cached = r.get(weather)
    if cached:
        weather_data = json.loads(cached)
        logger.debug("Weather_info_redis:", weather_data)
        return cached
    else:
        weather_data = await location_time.getinfo(city, timespan)
        r.set(weather, json.dumps(weather_data))
        logger.debug("Weather_info_no_redis:", weather_data)
        return weather_data

@app.get("/hello")
async def hello():
    return "Hello, CI/CD pipeline :)"
