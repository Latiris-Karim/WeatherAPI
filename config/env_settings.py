from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
        if os.environ['ENVIRONMENT'] == 'production':
                REDISHOST = os.environ.get("REDISHOST")
                REDISPORT = int(os.environ.get("REDISPORT"))
        else:
                REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
        

   

settings = Settings()
