from utils.mqtt_simple_client import MqttClient
from utils.object_detect import ObjectDetect


if __name__ == '__main__':
    # Init Mqtt client and object detection
    client = MqttClient().connect()
    objectDetect = ObjectDetect().init()
    objectDetect.eventSystem.on(objectDetect.EVENT_COCO, client.publish)

    # Register Events
    client.eventSystem.on(client.EVENT_TURNOFF, objectDetect.stop)
    # TODO make this work! seems tensorflow can only runs on main thread.
    # client.eventSystem.on(client.EVENT_TURNON, objectDetect.start)

    objectDetect.start()
