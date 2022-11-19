import time
import random
import paho.mqtt.client as mqtt
import json

from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
def Temp():
    return temperature = sensor.get_temperature()

#The above lines of code would be used when getting temperature data from a DS18B20 sensor.
#Due to hardware limitations we are simulating values using random function.

#def Temp():  
#    return random.randint(0,99);

ORG = "csgusn"
DEVICE_TYPE = "RPI"
TOKEN = "1123581321"
DEVICE_ID = "3c7c3f5b666d"  #Credentials of device as per created on IBM IoT platform.

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";   #event named status 1 in JSON format

authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)         #Connecting using MQ Telemetry Transport Protocol

while True:

    tempDict = { "d": {"temperature": Temp()} };    #Temporary storage in a dictionary

    tempJson = json.dumps(tempDict);    #Conversion from dictionary to JSON

    mqttc.publish(pubTopic1, tempJson)      #Publish payload
    print("Reading Taken");

    time.sleep(5);