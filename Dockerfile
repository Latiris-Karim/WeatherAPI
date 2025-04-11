FROM python:3.9

WORKDIR /WeatherAPI

COPY ./requirements.txt /WeatherAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /WeatherAPI/requirements.txt

COPY . /WeatherAPI/

CMD ["fastapi", "run", "main.py", "--port", "80"]
