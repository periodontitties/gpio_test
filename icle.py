#!/usr/bin/env python
# This test is for reading
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
while True:
    val = GPIO.input(4)
    if val == 0:
        print("000000000000000000000000000000000")
    else:
        print("111111111111111111111111111111111")

    time.sleep(0.25)
GPIO.cleanup()

