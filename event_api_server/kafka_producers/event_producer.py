from kafka import KafkaProducer


class EventProducer:
    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                                       client_id='event_kafka_producer')

    def send(self, value):
        response = self._producer.send('events.taxonomy', value=value.encode('utf-8'))
        return response.get(timeout=10)
