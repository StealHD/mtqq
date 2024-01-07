import asyncio
import random
import time
import json
from paho.mqtt import client as mqtt_client
from bean.WebSeed import WebSeed
from data import GoldPrice,ExchangeRate
import threading

broker = '47.245.103.174'
port = 1883
goldTopic = "homeassistant/gold_price"
rateTopic = "homeassistant/exchange_rate"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = "admin"
password = "admin"

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
    client.username_pw_set(username, password=password)
    client.connect(broker, port)

    return client


def publish(client):
    """

    :param client:
    :return: topic to mqtt server
    """


    def goldPriceTask():
        drive = WebSeed().driver()
        while True:
            goldMsg = GoldPrice.GoldPrice().update(driver=drive, url='https://quote.cngold.org/gjs/swhj_zghj.html')
            result = client.publish(goldTopic, json.dumps(goldMsg, ensure_ascii=False))
            status = result[0]
            if status == 0:
                print(f"Send {goldMsg} to topic `{goldTopic}`")
            else:
                print(f"Failed to send message to topic {goldTopic}")
            time.sleep(10)

    def exchangeRateTask():
        drive = WebSeed().driver()
        while True:
            rateMsg = ExchangeRate.ExchangeRate().update(driver=drive, url='https://www.google.com/finance/quote/AUD-CNY')
            result = client.publish(rateTopic, json.dumps(rateMsg, ensure_ascii=False))
            status = result[0]
            if status == 0:
                print(f"Send {rateMsg} to topic `{rateTopic}`")
            else:
                print(f"Failed to send message to topic {goldTopic}")
            time.sleep(10)

    goldThread = threading.Thread(target=goldPriceTask)
    rateThread = threading.Thread(target=exchangeRateTask)
    goldThread.start()
    rateThread.start()

async def main():
    client = connect_mqtt()
    publish(client)
    # mqtt_client = AsyncMQTTClient(MQTT_BROKER, MQTT_PORT, MQTT_TOPIC)
    client.loop_start()
    client.loop_stop()

if __name__ == "__main__":
    asyncio.run(main())
