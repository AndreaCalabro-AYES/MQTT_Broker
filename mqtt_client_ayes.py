# Full paho mqtt doc: https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html
# Example: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
import paho.mqtt.client as mqtt
import os
import json
import time
import logging

log = logging.getLogger("AYES MQTT CLIENT")

# 
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

class AyesMqttClient:
    """
    This class is intended to give a quick way to users to define a MQTT node for their application.
    The default settings can be overwritten at 
    
    """
    
    def basic_callback(client, userdata, msg):
        print(f"This is the basic callback function, so the node received the message {msg.payload.decode()} on topic {msg.topic}\n Please update this function as you want to perform the needed action.")

    def __init__(self, broker= "mqtt_broker", port= 1883, topics_list= None, client_id= "test", on_message= basic_callback):

        self.broker = broker
        self.port = port
        self.topics = topics_list or ["test/general"]
        if self.topics == ["test/general"]:
            print("You are connected to the general test topic, you should define your topic", flush=True)
        self.client_id = client_id
        if self.client_id == "test":
            print("The node's client id is the default one", flush=True)
        self.on_message= on_message
        
        # Initialize the MQTT client 
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.client_id)
        
            
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_subscribe = self.on_subscribe
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.on_disconnect = self.on_disconnect
        
                
    def on_connect(self, client, userdata, flags, rc, properties):
        if rc == 0:
            print(f"Connected to broker at {self.broker}: {self.port}", flush=True)
            for mqtt_topic in self.topics:
                client.subscribe(mqtt_topic)
        else:
            print("Failed to connect, return code %d", rc)

    def on_subscribe(self, client, userdata, mid, reason_code_list, properties):
        if reason_code_list[0].is_failure:
            print(f"Broker rejected you subscription: {reason_code_list[0]}", flush=True)
        else:
            print(f"Broker granted the following QoS: {reason_code_list[0].value}", flush=True)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code: %s", rc)
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
        

    def connect(self):
        self.mqtt_client.connect(
            host = self.broker,
            port = self.port,
            keepalive = 60
        )
        print(f"Connected to broker at {self.broker}: {self.port}", flush=True)

        self.mqtt_client.loop_start()


    def publish_message(self, topic, message):
        result = self.mqtt_client.publish(topic, message)
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic}`", flush=True)
        else:
            print(f"Failed to send message to topic {topic}", flush=True)