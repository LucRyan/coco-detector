from utils.mqtt_simple_client import MqttClient
from utils.object_detect import ObjectDetect
from threading import Event

kill = Event()


def main():
    while not kill.is_set():
        if kill.is_set():
            break

    print("All done!")
    # perform any cleanup here


def stop():
    kill.set()


if __name__ == '__main__':
    # Init Mqtt client and object detection
    client = MqttClient().connect()
    objectDetect = ObjectDetect().init()
    objectDetect.eventSystem.on(objectDetect.EVENT_COCO, client.publish)

    # Register Events
    client.eventSystem.on(client.EVENT_TURNOFF, objectDetect.stop)

    # TODO make this work! seems tensorflow can only runs on main thread.
    # TODO *** Terminating app due to uncaught exception 'NSInternalInconsistencyException', reason: '
    # TODO [NSUndoManager(NSInternal) _endTopLevelGroupings] is only safe to invoke on the main thread.'
    # client.eventSystem.on(client.EVENT_TURNOFF, stop)
    # client.eventSystem.on(client.EVENT_TURNON, objectDetect.start)
    # main()

    objectDetect.start()
