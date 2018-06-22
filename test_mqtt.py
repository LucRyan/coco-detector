from threading import Event
from utils.mqtt_simple_client import MqttClient

# The cooldown in mqtt client is 30s
COOL_DOWN = 120.0
kill = Event()


def main():
    while not kill.is_set():
        client.publish()
        kill.wait(COOL_DOWN)

    print("All done!")
    # perform any cleanup here


def stop():
    kill.set()


if __name__ == '__main__':
    client = MqttClient().connect()
    client.eventSystem.on(client.EVENT_TURNOFF, stop)

    main()
