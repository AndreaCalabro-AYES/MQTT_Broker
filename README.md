# MQTT Project

This project has been developed for multiple reasons:
1. Containerize a MQTT broker (and implement a handler)
2. Emulate a communication node for any application

Let's get into it, then!

## Prerequisites
- Docker Desktop (ADD LINK TO THE INTERNAL DOCUMENTATION ABOUT IT)
- It would be beneficial to associate this repository to any other application, but it's not needed

## Docker Networking

As the scope of this application is communication, a good approach is to have a little knowledge of docker networking. To have more information, refer to the documentation that you will find linked along the way. 
"Container netwokring is the ability for container to connect and communicate among each other, or to non-Docker workloads", as it is stated on the official docker [networking overview](https://docs.docker.com/network/).
There are some default networks, that you can find 
- [bridge](https://docs.docker.com/network/drivers/bridge/), a software bridge that allows containers connected to it to communicate
- [host](https://docs.docker.com/network/drivers/host/), used when we want the container to share the host's networking namespace 
- none, where we connect containers that shall be isolated from the outside

On top of that, users can create their own network. 

As we are in POC, let's use the default host network...


## The MQTT Broker and Handler

**CLONE REPOSITORY**

As always , go into the folder where you want to create the project, open the terminal, and type the following command
```
git clone https://github.com/AndreaCalabro-AYES/MQTT_Broker.git
```

### MQTT Broker
Mosquitto (MQTT) is a lightweight publish/subscribe messaging transport that has been designed for IoT applications.
Here the link to the [official documentation](https://mqtt.org/). 
It's so effective, that it has been used in a lot of industries, and if you want to go even deeper: [download the pdf here](https://www.hivemq.com/info/mqtt-essentials/#essential-guide).

The idea is to use an image already containing a broker, the [eclipse-moquitto](https://hub.docker.com/_/eclipse-mosquitto).
This container running the broker (server) image has the task to manage the communication among all the clients (our other containerized applications). 
You will find loggings in the mosquitto_log folder (the mosquitto_data format is intended for internal MQTT use, so don't even bother looking into it). If you don't see these folders (mosquitto_log, mosquitto_data) in your local repository, please add them manually before building.

By default, inside each client, you will have the following settings (and do it for any new application you develop)
- MQTT_BROKER_HOST = *localhost*
- MQTT_BROKER_PORT = *1883*
- network (repetita iuvat) = *mqtt_network*
You can always change them in the docker compose file: it's a learning project, so break stuff! That's why everything runs on containers.

### Handler
As you can see, there is an handler script. This is needed for multiple reasons
- Connect to every topic that will be defined, in order to act as a read everything (will be further developed)
- By means of this connection to all the topics, it can be very useful to mock the communication node of any application
    * If you need a publisher, just publish a message in the correct topic
    * If you need a subscriber, use it to subscribe to the correct topic, and check that the application is correctly sending the message

### Client
In each application, you should implement an MQTT client node, as of now just copy the handler. 
A quite important setting is the CLIENT_ID, which will identify the node in the logs. 

## Future development
In the future we will have the handler acting almost as a state machine logic, based on the application results, and then 
1. A fake node script, where you will be able to set perform the necessary actions (as explained above) --> not hard
2. A custom AYES mqtt library, where you will retrieve all the functions that are needed to develop a proper MQTT Client --> done, and even found how to use it in other containers! To be worked from here


## MQTT AYES Client Class


## TODO FOR THE FUTURE
In our case, we will build our custom bridge network.
Why not use the default's one? Here the [full answer](https://docs.docker.com/network/drivers/bridge/#differences-between-user-defined-bridges-and-the-default-bridge), otherwise 
* Better isolation, as we will only connect the containers that we explicitly want to connect
* Freedom to connect, and freedom to deattach 
* Ease of connection, as the containers on a custom bridge network can resolve (find) each other by name/alias, and not IP address

**CREATE NETWORK**

You will need to create your own docker bridge network! Just type the following command in your terminal
```
docker network create -d bridge mqtt_network
```
The expected name in the containers is this, so feel free to play with it. 
