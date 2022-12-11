from kafka import KafkaProducer
from json import dumps


class BetProducer:
    """Producer-class for pushing messages to kafka-service"""
    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                       client_id='bet_kafka_producer')

    def send(self, value: dict):
        response = self._producer.send('bets.state', value=dumps(value).encode('utf-8'))
        return response.get(timeout=10)
