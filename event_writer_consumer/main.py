from kafka import KafkaConsumer
import uvicorn
from postgres_workers.events_worker import EventsDataWorker
from json import loads
from psycopg_pool import AsyncConnectionPool
import psycopg

consumer = KafkaConsumer('events.taxonomy', bootstrap_servers=['kafka:9092'],
                         client_id='event_writer_consumer')

connection_string = "host=database port=5432 dbname=pm_db connect_timeout=10 user=pm_user password=12131415"
pool = AsyncConnectionPool(connection_string=connection_string)
data_writer = EventsDataWorker(pool=pool)


def write_data(message):
    values = tuple(message.decode('utf-8').loads().values())
    with psycopg.connect(connection_string) as conn:
        with conn.cursor() as curr:
            curr.execute("INSERT INTO Events(type, name, event_date) VALUES(%s, %s, %s)", values)
            conn.commit()


def main():
    for message in consumer:
        print(message, dir(message))
        # write_data(message)


if __name__ == '__main__':
    uvicorn.run('main:main', reload=True)
