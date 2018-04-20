#!python3
# MQTT Publish Demo
# Publish two messages, to two differnt topics

import paho.mqtt.publish as publish
import time

publish.single('CoreElectronics/test', 'Hello', hostname='test.mosquitto.org')
time.sleep(4)
publish.single('CoreElectronics/topic', 'World!', hostname='test.mosquitto.org')

print('Done')
