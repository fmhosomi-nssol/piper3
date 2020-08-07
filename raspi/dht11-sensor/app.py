#!/usr/bin/env python3

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

broker = "test.mosquitto.org"
topic = "hosomi-piper3"
client = mqtt.Client()
client.connect(broker)

def loop():
    while True:
        result = instance.read()
        #print(result.is_valid())
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            #print("Temperature: %-3.1f C" % result.temperature)
            #print("Humidity: %-3.1f %%" % result.humidity)
            client.publish(topic + "/temp", result.temperature)
            client.publish(topic + "/humid", result.humidity)
            client.publish(topic + "/timestamp", str(datetime.datetime.now()))
            time.sleep(5)
        time.sleep(1)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("Cleanup")
        GPIO.cleanup()
