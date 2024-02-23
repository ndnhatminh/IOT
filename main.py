import sys

from Adafruit_IO import Client
import time
import random
from dotenv import dotenv_values
from simple_ai import image_detector
from uart import *

env_config = dotenv_values('.env')

AIO_FEED_IDs = ['nutnhan1','nutnhan2']
AIO_USERNAME = env_config['AIO_USERNAME']
AIO_KEY = env_config['AIO_KEY']


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = Client(AIO_USERNAME , AIO_KEY)

counter = 10
counter_ai = 5
while True:
    # counter = counter - 1
    # sensor_type = 0

    # if counter <= 0:
    #     #TODO
    #     print("Random data is publish")

    #     if sensor_type==0:
    #         temp = random.randint(10, 20)
    #         client.send_data("cambien1", temp)
    #         sensor_type = 1
    #     elif sensor_type==1:
    #         humi = random.randint(50, 70)
    #         client.send_data("cambien2", humi)
    #         sensor_type = 2
    #     elif sensor_type==2:
    #         light = random.randint(100, 500)
    #         client.send_data("cambien3", light)
    #         sensor_type = 0

    # counter_ai = counter_ai - 1
    # if counter_ai <= 0:
    #     counter_ai = 5
    #     ai_result = image_detector()
    #     client.send_data("ai", ai_result)

    readSerial(client)
    time.sleep(1)
    pass