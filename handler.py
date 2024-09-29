# Full paho mqtt doc: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html
# Example: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import os
import time
import json
from mqtt_client_ayes import AyesMqttClient
import SentenceAPI

# MQTT Config
MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="mqtt_broker")
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))
MQTT_TOPICS = ["temperature/internal",
               "general",
               "greetings/face_added",
               "greetings/face_removed",
               "sentence/single_sentence"]


mqtt_handler_client = AyesMqttClient(
    broker= MQTT_BROKER_HOST,
    port= MQTT_BROKER_PORT,
    topics_list= MQTT_TOPICS,
    client_id= "Handler"
)

mqtt_handler_client.connect()

mqtt_handler_client.on_message 



# Get the joke from the SentenceAPI
joke_data = SentenceAPI.import_dad_joke()

decoded_joke = json.loads(joke_data)

joke = decoded_joke[0]["joke"]


while True:
    
    time.sleep(15)
    
    msg_body = json.dumps({"temperature": 22})
    
    
    mqtt_handler_client.publish_message(
        topic= "temperature/internal",
        payload= msg_body
    )
    
    # time.sleep(15)

    # msg_body = json.dumps({"names": "Lorella"})
    
    # mqtt_handler_client.publish_message(
    #     topic= "greetings/face_added",
    #     payload= msg_body
    # )
    
    # time.sleep(15)
    time.sleep(10)
    
    # msg_body = json.dumps(joke)
    msg_body = json.dumps({"sentence": joke})
    mqtt_handler_client.publish_message(
        topic= "sentence/single_sentence",
        payload= msg_body
    )
    
    time.sleep(300)
    

    pass
