import time
import random
import paho.mqtt.client as mqtt
import json

#from w1thermsensor import W1ThermSensor
#sensor = W1ThermSensor()
#def Temp():
    #return temperature = sensor.get_temperature()

#The above lines of code would be used when getting temperature data from a DS18B20 sensor.
#Due to hardware limitations we are simulating values using random function.

def prodTemp():
    l = [40,40,39,39,39,38,38,37,37,37,41,42,44,41,42,42,43]
    return random.choice(l)

def assemTemp():
    l = [40,40,39,39,39,38,38,37,37,37,41,42,41,42,42,43,69,69,69]
    return random.choice(l)

def transTemp():
    l = [30,30,30,29,29,27,28,27,26,31,31,31,32,35,35,34,30,29,27]
    return random.choice(l)

#Due to hardware limitations we are simulating values for different areas using random function.

ORG = "csgusn"
DEVICE_TYPE = "RPI"
TOKEN = "1123581321"
DEVICE_ID = "3c7c3f5b666d"

#Credentials of device as per created on IBM IoT platform.

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";

#Event named status1 sending data in json format.

authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

#Connecting via MQTT.

while True:

    tempDict = { "d": {"temperature1": prodTemp(),"temperature2": prodTemp(),"temperature3": prodTemp(),"temperature4": assemTemp(),"temperature5": assemTemp(),"temperature6": transTemp(),"temperature7": transTemp(),} };

    tempJson = json.dumps(tempDict);

    mqttc.publish(pubTopic1, tempJson)
    print("Reading Taken");

    time.sleep(5);