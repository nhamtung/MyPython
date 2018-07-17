
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json

AllowedActions = ['both', 'publish', 'subscribe']

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

# rootCAPath = "D:\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\rootCA.pem"
# certificatePath = "D:\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\44432477c8-certificate.pem.crt"
# privateKeyPath = "D:\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\44432477c8-private.pem.key"
rootCAPath = "D:\MyFolder\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\rootCA.pem"
certificatePath = "D:\MyFolder\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\44432477c8-certificate.pem.crt"
privateKeyPath = "D:\MyFolder\TUNG\MyPython\AWSIoTPythonSDK\TungNV\Certificate\BasicPubSubPython\\44432477c8-private.pem.key"

host = "avt6g3kvwjn2o.iot.ap-southeast-1.amazonaws.com"
useWebsocket = False
port = 443
clientId = "AKIAIEV6W7J3Y5ESXFWA"
keyId = "52htv/HbGkwaPof93UaPRDOqtWNjjHEHsyTMZH9s"
topic = "$aws/things/BasicPubSubPython/shadow/update"
mode = "both"
message = "Hello"

if mode not in AllowedActions:
    print("Unknown --mode option %s. Must be one of %s" % (mode, str(AllowedActions)))
    exit(2)
if useWebsocket and certificatePath and privateKeyPath:
    print("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
    exit(2)
if not useWebsocket and (not certificatePath or not privateKeyPath):
    print("Missing credentials for authentication.")
    exit(2)

# # Configure logging
# logger = logging.getLogger("AWSIoTPythonSDK.core")
# logger.setLevel(logging.DEBUG)
# streamHandler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)


# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
    myAWSIoTMQTTClient.configureIAMCredentials(clientId, keyId)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
if mode == 'both' or mode == 'subscribe':
    myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)

# Publish to the same topic in a loop forever
loopCount = 0
while True:
    if mode == 'both' or mode == 'publish':
        message = {}
        message['message'] = message
        message['sequence'] = loopCount
        messageJson = json.dumps(message)
        myAWSIoTMQTTClient.publish(topic, messageJson, 0)
        if mode == 'publish':
            print('Published topic %s: %s\n' % (topic, messageJson))
        loopCount += 1
    time.sleep(1)
