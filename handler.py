# Full paho mqtt doc: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html
# Example: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import os
import time
import json
from mqtt_client_ayes import AyesMqttClient

# MQTT Config
MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="mqtt_broker")
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))
MQTT_TOPICS = ["temperature/internal",
               "general",
               "greetings/face_added",
               "greetings/face_removed"]


mqtt_handler_client = AyesMqttClient(
    broker= MQTT_BROKER_HOST,
    port= MQTT_BROKER_PORT,
    topics_list= MQTT_TOPICS,
    client_id= "Handler"
)

mqtt_handler_client.connect()

while True:
    
    msg_body = json.dumps({"temperature": 22})
    
    time.sleep(15)
    
    mqtt_handler_client.publish_message(
        topic= "temperature/internal",
        payload= msg_body
    )
