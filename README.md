# Piper Japan Wave3 Personal Project

Rasberry Pi、DHT11センサ、Pivotal Web Serviceを使ったアプリケーションです。

## Rasbery Pi

### DHT11 sensor (raspi/dht11-sensor)

`https://github.com/szazo/DHT11_Python` のモジュールをインストールして使用します。

### AWS IoT (raspi/AWS-IoT)

AWSIoTPythonSDK をインストールして使用します。

### systemd (raspi/systemd)

上記プログラムを systemd で呼び出すためのユニットファイルです。

## Pivotal Web Service

### MQTT subscriber (pivotal/mqtt-sub)

Rasberry Pi が publish したセンサデータを subscribe して Redis に格納するアプリケーションです。

### DHT11 sensor web application (pivotal/webapp)

Redis に格納したセンサデータを表示する Web アプリケーションです。
