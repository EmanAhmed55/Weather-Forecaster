from kafka import KafkaProducer
import json 
import time
import random  
producer = KafkaProducer(bootstrap_servers='localhost:9092')

WEATHER_STATES = ['Sunny', 'Rainy', 'Windy', 'Cloudy', 'Snowy']

while True:
    weather = random.choice(WEATHER_STATES)
    temperature = random.randint(-5, 35)  # temperatures from -5°C to 35°C
    humidity = random.randint(10, 90)  # humidity percentage

    message = f"Weather: {weather}, Temperature: {temperature}°C, Humidity: {humidity}%"
    producer.send('weather_forecasts', value=message.encode('utf-8'))
    time.sleep(2)  # Send every 2 seconds