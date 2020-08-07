#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import models

broker_address = "test.mosquitto.org"
Topic = "hosomi-piper3/+"

r = models.redis()

def on_message(client, userdata, message):
    k = message.topic.split("/")[-1]
    v = str(message.payload.decode("utf-8"))
    print("message received: " + k + v)
    r.set(k, v, ex=60)


print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

try:
    while True:
        client.subscribe(Topic)
        time.sleep(2) # wait
except KeyboardInterrupt:
    client.loop_stop() #stop the loop
