import time
from utils.mqtt_simple_client import MqttClient

COOLDOWN = 120

if __name__ == '__main__':
    client = MqttClient().connect()

    while True:  # fps._numFrames < 120
        client.publish()
        time.sleep(COOLDOWN)

