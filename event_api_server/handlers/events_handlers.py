import os

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from postgres_workers.events_worker import EventsDataWorker
from kafka_producers.event_producer import EventProducer

connection_string = os.environ.get("DATABASE_LINK")
pool = AsyncConnectionPool(connection_string, open=False)


def startup_event_handler(app: FastAPI):
    async def wrapper():
        app.event_data_worker = EventsDataWorker(pool=pool)
        app.producer = EventProducer()
        await pool.open(wait=True)
    return wrapper


def shutdown_event_handler(app: FastAPI):
    async def wrapper():
        await pool.close()
    return wrapper
