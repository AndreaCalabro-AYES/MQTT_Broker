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
               "greetings/face_removed"]


mqtt_handler_client = AyesMqttClient(
    broker= MQTT_BROKER_HOST,
    port= MQTT_BROKER_PORT,
    topics_list= MQTT_TOPICS,
    client_id= "Handler"
)

mqtt_handler_client.connect()

mqtt_handler_client.on_message 

while True:
    

    # print("\nDad Joke\n", flush=True)
    # SentenceAPI.import_dad_joke()
    # print("\n", flush=True)
    # time.sleep(5)
    # print("\nFact\n", flush=True)
    # SentenceAPI.import_fact()
    # print("\n", flush=True)
    # time.sleep(5)
    # print("\nJoke\n", flush=True)
    # SentenceAPI.import_joke()
    # print("\n", flush=True)
    # time.sleep(5)
    # print("\nquote\n", flush=True)
    # SentenceAPI.import_quote()
    # print("\n", flush=True)
    # time.sleep(5)
    # print("\nriddle\n", flush=True)
    # SentenceAPI.import_riddle()
    # print("\n", flush=True)
    time.sleep(5)
    # print("\ntrivia\n", flush=True)
    # SentenceAPI.import_trivia()
    # print("\n", flush=True)
    SentenceAPI.get_historical_event_for_today()
    pass
    # msg_body = json.dumps({"names": ["Margot"]})
    
    # time.sleep(30)
    
    # mqtt_handler_client.publish_message(
    #     topic= "greetings/face_added",
    #     payload= msg_body
    # )
