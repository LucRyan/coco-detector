import time
import sys
from utils.mqtt_simple_client import MqttClient

COOL_DOWN = 120


def stop():
    sys.exit()


if __name__ == '__main__':
    client = MqttClient().connect()
    client.eventSystem.on(client.EVENT_TURNOFF, stop)

    while True:
        client.publish()
        time.sleep(COOL_DOWN)
