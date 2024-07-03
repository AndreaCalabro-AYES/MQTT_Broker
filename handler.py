# Full paho mqtt doc: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html
# Example: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
import paho.mqtt.client as mqtt
import os
import time
import json

# MQTT Config
MQTT_BROKER_HOST = os.getenv(key="MQTT_BROKER_HOST", default="mqtt_broker")
MQTT_BROKER_PORT = int(os.getenv(key="MQTT_BROKER_PORT", default=1883))
MQTT_TOPICS = ["temperature/internal",
               "general",
               "greetings/face_added",
               "greetings/face_removed"]

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60
CLIENT_ID = "Handler"

def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f"Connected to broker at {MQTT_BROKER_HOST}: {MQTT_BROKER_PORT}", flush=True)
        for mqtt_topic in MQTT_TOPICS:
            client.subscribe(mqtt_topic)
    else:
        print("Failed to connect, return code %d", rc, flush=True)

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}", flush=True)
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}", flush=True)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}", flush=True)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: %s", rc, flush=True)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print("Reconnecting in %d seconds...", reconnect_delay, flush=True)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("Reconnected successfully!", flush=True)
            return
        except Exception as err:
            print("%s. Reconnect failed. Retrying...", err, flush=True)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    print("Reconnect failed after %s attempts. Exiting...", reconnect_count, flush=True)

# Set Connecting Client ID
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)

# client.username_pw_set(username, password)
mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_message = on_message
mqtt_client.on_disconnect = on_disconnect

def connect():
    mqtt_client.connect(
        host = MQTT_BROKER_HOST,
        port = MQTT_BROKER_PORT,
        keepalive = 60
    )
    print(f"Connected to broker at {MQTT_BROKER_HOST}: {MQTT_BROKER_PORT}", flush=True)

    mqtt_client.loop_start()

def publish(topic, message):
    result = mqtt_client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Send `{message}` to topic `{topic}`", flush=True)
    else:
        print(f"Failed to send message to topic {topic}", flush=True)

connect()

count = 0

while True:
    
    if (count % 5) == 0:
        msg_body = json.dumps({"names": ["Drake"]})
        mqtt_client.publish(
            topic = MQTT_TOPICS[2],
            payload= msg_body,
        )
        print(f"Published {msg_body}, to {MQTT_TOPICS[2]}", flush=True)
    
    if (count % 12) == 0:
        msg_body = json.dumps({"names": ["Lorellina del mio cuole"]})
        mqtt_client.publish(
            topic = MQTT_TOPICS[3],
            payload= msg_body,
        )
        print(f"Published {msg_body}, to {MQTT_TOPICS[3]}", flush=True)
    
    count += 1
    time.sleep(3)
    
    

