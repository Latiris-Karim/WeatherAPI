import os
from dotenv import load_dotenv
import logging
import httpx
import asyncio

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

async def getinfo(city, time):
    load_dotenv()
    weatherkey = os.getenv('weather_key')
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{time}?unitGroup=us&key={weatherkey}&contentType=json"
        )
        logger.debug(f"Response status code: {response.status_code}")

        if response.status_code == 401 or response.status_code == 403:
            return {"error": "Invalid or unauthorized API key."}
        
        elif response.status_code == 200:
            data = response.json()
            daily_temperatures = []
            daily_temperatures.append({'address': data['resolvedAddress']})
            for day in data['days']:
                daily_temperatures.append({
                    'date': day['datetime'],
                    'temperature': day['temp'],
                    'feels-like': day['feelslike'],
                    'windspeed': day['windspeed'],
                    'description': day['description'],
                    'uvIndex':day['uvindex']
                })
           
            return daily_temperatures
        else:
            return "invalid cit, or country"


if __name__ == "__main__":
    result = asyncio.run(getinfo("cologne", "next7days"))
    print(result)


