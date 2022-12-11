from kafka import KafkaProducer
from json import dumps


class EventProducer:
    """Kafka-producer for sending messages to events.taxonomy"""
    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                       client_id='event_kafka_producer')

    def send(self, value: str | dict, idn: int = None):
        """Checks if event updating or creating(if creating - no id) and
            pushes event info to kafka"""
        if idn:
            value['id'] = idn
            value = dumps(value)
            response = self._producer.send('events.taxonomy', value=value.encode('utf-8'))
        else:
            response = self._producer.send('events.taxonomy', value=value.encode('utf-8'))
        return response.get(timeout=10)
