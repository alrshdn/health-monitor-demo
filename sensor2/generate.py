import os
import random
import requests
from time import time, sleep
import datetime
import pytz


def generate_data():
    while True:
        current_time = datetime.datetime.now(pytz.timezone(os.environ["TZ"]))
        temparature = generate_temperature(current_time)
        stress_level = generate_stress_level(current_time)
        sensor_name = os.environ["SENSORNAME"]
        timestamp = current_time.strftime("%m/%d/%Y, %H:%M:%S")

        # Send data to server
        response = requests.post(f'http://{os.environ["STORAGEIP"]}:5000/send_data',
                                 params={"temparature": temparature,
                                         "sensor_name": sensor_name,
                                         "stress_level": stress_level,
                                         "timestamp": timestamp,
                                         "timezone": os.environ["TZ"], 
                                         })

        sleep(5)

def generate_temperature(current_time):
    if current_time.hour >= 23 or current_time.hour < 8:
        return round(random.uniform(36.1, 38.8), 2)
    else:
        return round(random.uniform(35.5, 38.0), 2)

def generate_stress_level(current_time):
    if current_time.strftime("%A") in ["Wednesday", "Thursday"]:
        return random.randint(100, 1000)
    else:
        return random.randint(0, 100)

generate_data()

