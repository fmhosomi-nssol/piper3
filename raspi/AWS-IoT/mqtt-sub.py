#!/usr/bin/env python3

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os
import json
import time
import subprocess

# 初期化
myMQTTClient = AWSIoTMQTTClient("raspi-zero")
DIRNAME = os.path.dirname(__file__)
ROOT_CA = DIRNAME + "/cert/rootCA.pem"
PRIVATE_KEY = DIRNAME + "/cert/30e70e79ca-private.pem.key"
CERTIFICATE = DIRNAME + "/cert/30e70e79ca-certificate.pem.crt"

# MQTTクライアントの設定
myMQTTClient.configureEndpoint("a2sgqkstlitver-ats.iot.ap-northeast-1.amazonaws.com", 443)
myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)

# Connect to AWS IoT endpoint and publish a message
myMQTTClient.connect()
print ("Connected to AWS IoT")

Topic = "dht11-service"

def mycallback(client, userdata, message):
    topic = message.topic
    payload = str(message.payload.decode("utf-8"))
    print("Recieved message: " + topic + " " + payload)
    if payload in ["start", "stop"]:
        subprocess.run(["systemctl", payload, "dht11.service"])

def loop():
    while True:
        myMQTTClient.subscribe(Topic, 1, mycallback)
        time.sleep(2)

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        print("Clenaup")
        myMQTTClient.disconnect()
