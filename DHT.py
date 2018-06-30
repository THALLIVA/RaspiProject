import Adafruit_DHT
import RPi.GPIO as GPIO

import time


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
