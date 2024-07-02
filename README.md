Will be written ;) 


This folder will be used as a mqtt broker for all the applications. To use it you need to 
1. create the docker network --> docker network -d bridge mqtt_network
2. launch the container
3. connect the other applications to ensure they can correctly communicate

Thanks to the custom bridge network , the containers will talk using the broker. 

As you can see, there is an handler that connects to all the topics, and (sends/)recieves all the messages. In the future this will be further developed.
