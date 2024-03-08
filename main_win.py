import sys
import time
import random
from dotenv import dotenv_values
# from simple_ai import image_detector
from uart_win import *
from adafruit_mqtt import Adafruit_MQTT

env_config = dotenv_values('.env')

AIO_FEED_IDs = ['nutnhan1','nutnhan2']
AIO_USERNAME = env_config['AIO_USERNAME']
AIO_KEY = env_config['AIO_KEY']

# FUNCTION DEFINITIONS
def callBackFunc_Message(feed_id, payload):
    print("Feed: " + feed_id + " - Value: " + payload)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData("1")
        else: 
            writeData("2")

# MAIN PROGRAM
# Create an instance of Adafruit_MQTT class
client = Adafruit_MQTT(AIO_USERNAME, AIO_KEY, AIO_FEED_IDs, callBackFunc_Message)
client.setup()
client.connect_and_loop()

while True:
    readSerial(client)
    time.sleep(1)