import paho.mqtt.client as mqtt
import time
import random
import threading


class MqttClient:
    def __init__(self):
        self.defaultCoolDown = 20
        self.lastTime = time.time()
        self.client = mqtt.Client()

    def on_connect(self, client, userdata, rc, *extra_params):
        print('Connected with result code ' + str(rc))
        # print('***' + str(r))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe('v1/devices/me/attributes')
        self.client.subscribe('v1/devices/me/attributes/response/+')
        self.client.subscribe('v1/devices/me/rpc/request/+')

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print ('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))
        if msg.topic.startswith('v1/devices/me/rpc/request/'):
            requestId = msg.topic[len('v1/devices/me/rpc/request/'):len(msg.topic)]
            print ('RPC call. RequestID: ' + requestId)
            self.client.publish('v1/devices/me/rpc/response/' + requestId, "{\"Response\":\"cool\"}", 1)

            # if "false" in str(msg.payload) and "turnOnDevice" in str(msg.payload):
            #    sys.exit(0)

    def on_disconnect(self, client, userdata, rc=0):
        print ("DisConnected result code " + str(rc))
        self.client.connect('39.108.164.189', 1883, 60)

    def on_log(self, client, userdata, level, buf):
        print("log: ", buf)

    def publish(self):
        if time.time() - self.lastTime > self.defaultCoolDown:
            self.lastTime = time.time()

            percentage = random.uniform(0.0, 1.0)
            speed = random.uniform(0.0, 21.0)
            latitude = 33.97541;
            longitude = -118.37996;
            temperature = random.uniform(22.0, 27.0)

            self.client.publish('v1/devices/me/telemetry',
                                "{\"Times\":\"" + str(percentage) +
                                "\", "
                                "\"speed\":\"" + str(speed) +
                                "\", "
                                "\"temperature\":\"" + str(temperature) +
                                "\", "
                                "\"latitude\":\"" + str(latitude) +
                                "\", "
                                "\"longitude\":\"" + str(longitude) + "\"}",
                                0)

    def connect(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log

        # Random simulate bedroom or livingroom
        if random.uniform(0.0, 1.0) >= 0.5:
            self.client.username_pw_set("ZrDIXzTD8hMD2gakwzaV")
        else:
            self.client.username_pw_set("zXi6mGM4GBmj75Bvl5sk")

        self.client.connect('39.108.164.189', 1883, 0)

        thread = threading.Thread(target=self.listen, args=())
        thread.setDaemon(True)

        thread.start()
        return self

    def listen(self):
        self.client.loop_misc()
