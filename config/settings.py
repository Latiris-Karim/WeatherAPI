from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    ENVIRONMENT = os.getenv("ENVIRONMENT")

    if ENVIRONMENT == "development":
        REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
        

    elif ENVIRONMENT == "production":
         ...#GCP MEMORYSTORE

settings = Settings()
