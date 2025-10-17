import json, os, time
from gpiozero import Button
import paho.mqtt.client as mqtt
from signal import pause

DEFAULTS = {"gpio_pin": 17, "mqtt_host": "core-mosquitto"}
opts_path = "/data/options.json"
try:
    with open(opts_path) as f:
        opts = json.load(f)
except Exception:
    opts = {}
PIN  = int(opts.get("gpio_pin", DEFAULTS["gpio_pin"]))
HOST = opts.get("mqtt_host", DEFAULTS["mqtt_host"])
TOPIC = "pccc/emergency"

btn = Button(PIN, pull_up=True, bounce_time=0.05)
mq  = mqtt.Client("addon-gpio-emergency")
mq.will_set(f"{TOPIC}/status", "OFFLINE", qos=1, retain=True)

while True:
    try:
        mq.connect(HOST, 1883, 60)
        mq.publish(f"{TOPIC}/status", "ONLINE", qos=1, retain=True)
        break
    except Exception:
        time.sleep(2)

mq.publish(TOPIC, "PRESSED" if btn.is_pressed else "RELEASED", qos=1)
btn.when_pressed  = lambda: mq.publish(TOPIC, "PRESSED", qos=1)
btn.when_released = lambda: mq.publish(TOPIC, "RELEASED", qos=1)

pause()


