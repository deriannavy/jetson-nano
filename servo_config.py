#!/bin/bash

sudo pip3 install adafruit-circuitpython-servokit
sudo usermod -aG i2c diex
sudo groupadd -f -r gpio
sudo usermod -a -G gpio diex
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo reboot now
sudo i2cdetect -y -r 1



# from adafruit_servokit import Servokit
# kit=Servokit(channels=16)
