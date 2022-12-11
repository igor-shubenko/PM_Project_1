"""Kafka-consumer, that reads messages from bets.state topic and
    pushes them to data-writer for further updating records in database"""
import os

from kafka import KafkaConsumer
import uvicorn

from postgres_workers.bets_worker import BetsDataWorker

consumer = KafkaConsumer('bets.state',
                         bootstrap_servers=['kafka:9092'],
                         client_id='bet_writer_consumer',
                         group_id='bet_writer_consumer')

connection_string = os.environ.get("DATABASE_LINK")

data_writer = BetsDataWorker(connection_string=connection_string)


def main():
    for message in consumer:
        data_writer.update_record(message)


if __name__ == '__main__':
    uvicorn.run('main:main', host='0.0.0.0', port=8762, workers=1, reload=True)
