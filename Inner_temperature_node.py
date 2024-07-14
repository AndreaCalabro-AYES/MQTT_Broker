from mqtt_client_ayes import AyesMqttClient
import os
import time
import json

MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="localhost")
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))

inner_temp_list = [17.2, 18.9, 12.4, 14.4, 16.4, 17.1, 18.0, 22.1, 33.9]

inner_temp_client = AyesMqttClient(
    broker= MQTT_BROKER_HOST,
    port= MQTT_BROKER_PORT,
    topics_list= ["temperature/internal", "greetings/face_removed", "greetings/face_added"],
    client_id= "internal_temperature"
)


inner_temp_client.connect()


for temp in inner_temp_list:
    
    msg_body = json.dumps({"temperature": temp})
    
    time.sleep(10)
    
    inner_temp_client.publish_message(
        topic= "temperature/internal",
        payload= msg_body
    )
    
