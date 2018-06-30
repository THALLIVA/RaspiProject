import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


#Connected = False  # global variable for the state of the connection

def mqtt(value):
    broker_address = "192.168.43.229"
    port = 1883
    # user = "crmqdcnd"
    # password = "D1e5i21JMT2l"

    client = mqttClient.Client("Darsh")  # create new instance
    #client.username_pw_set(user, password=password)  # set username and password
    client.on_connect = on_connect  # attach function to callback
    client.connect(broker_address, port=port)  # connect to broker

    client.loop_start()
    n=0 # start the loop

    while Connected != True:  # Wait for connection
        time.sleep(0.1)

    while n<5:
            #value = input('Enter the message:')
        client.publish("test", value)
        n = n + 1

    client.disconnect()
    client.loop_stop()