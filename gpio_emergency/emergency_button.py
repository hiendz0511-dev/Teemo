#!/usr/bin/env python3
import os, time
from gpiozero import Button
from signal import pause
import paho.mqtt.client as mqtt

PIN   = int(os.getenv("GPIO_PIN", "17"))
HOST  = os.getenv("MQTT_HOST", "core-mosquitto")
TOPIC = "pccc/emergency"

btn = Button(PIN, pull_up=True, bounce_time=0.05)

mq = mqtt.Client("addon-gpio-emergency")
mq.will_set(f"{TOPIC}/status", "OFFLINE", qos=1, retain=True)

while True:
    try:
        mq.connect(HOST, 1883, 60)
        mq.publish(f"{TOPIC}/status", "ONLINE", qos=1, retain=True)
        break
    except Exception:
        time.sleep(2)

mq.loop_start()
mq.publish(TOPIC, "PRESSED" if btn.is_pressed else "RELEASED", qos=1)
btn.when_pressed  = lambda: mq.publish(TOPIC, "PRESSED",  qos=1)
btn.when_released = lambda: mq.publish(TOPIC, "RELEASED", qos=1)
pause()
