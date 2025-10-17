import os, time
from gpiozero import Button
import paho.mqtt.client as mqtt

PIN = int(os.getenv("GPIO_PIN", "17"))
HOST = os.getenv("MQTT_HOST", "core-mosquitto")
TOPIC = "pccc/emergency"

btn = Button(PIN, pull_up=True, bounce_time=0.05)

client = mqtt.Client(client_id="addon-gpio-emergency")
client.will_set(f"{TOPIC}/status", "OFFLINE", qos=1, retain=True)

# Kết nối MQTT có retry
while True:
    try:
        client.connect(HOST, 1883, 60)
        client.publish(f"{TOPIC}/status", "ONLINE", qos=1, retain=True)
        break
    except Exception:
        time.sleep(2)

# Publish trạng thái hiện tại lúc khởi động
def publish_state():
    client.publish(TOPIC, "PRESSED" if btn.is_pressed else "RELEASED", qos=1)

btn.when_pressed  = lambda: client.publish(TOPIC, "PRESSED", qos=1)
btn.when_released = lambda: client.publish(TOPIC, "RELEASED", qos=1)

publish_state()

client.loop_start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    client.publish(f"{TOPIC}/status", "OFFLINE", qos=1, retain=True)
    client.loop_stop()
    client.disconnect()
