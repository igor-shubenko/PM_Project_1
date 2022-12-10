import os

from kafka import KafkaConsumer
import uvicorn
from postgres_workers.events_worker import KafkaEventsDataWorker

consumer = KafkaConsumer('events.taxonomy',
                         bootstrap_servers=['kafka:9092'],
                         client_id='event_writer_consumer',
                         group_id='event_consumer')

connection_string = os.environ.get("DATABASE_LINK")

data_writer = KafkaEventsDataWorker(connection_string=connection_string)


def main():
    for message in consumer:
        data_writer.write_or_update_data(message)


if __name__ == '__main__':
    uvicorn.run('main:main', host='0.0.0.0', port=8764, reload=True)
