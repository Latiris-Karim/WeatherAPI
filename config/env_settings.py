from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
        if os.environ['ENVIRONMENT'] == 'production':
                redis_host = os.environ.get("REDISHOST")
                redis_port = int(os.environ.get("REDISPORT"))
        else:
                REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
        

   

settings = Settings()
