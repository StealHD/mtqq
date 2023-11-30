import asyncio
import random
import time
import json
from paho.mqtt import client as mqtt_client
from data.GoldPrice import GoldPrice

broker = '192.168.10.102'
port = 9042
topic = "homeassistant/goldprice"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    """

    :return: mqtt client
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    """

    :param client:
    :return: topic to mqtt server
    """
    while True:
        goldInfo = GoldPrice().update()
        msg = goldInfo
        result = client.publish(topic, json.dumps(msg, ensure_ascii=False))
        status = result[0]
        if status == 0:
            print(f"Send {msg} to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(3600)


async def main():
    client = connect_mqtt()
    publish(client)
    # mqtt_client = AsyncMQTTClient(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC)
    await client.loop_start()
    mqtt_client.stop()

if __name__ == "__main__":
    asyncio.run(main())
