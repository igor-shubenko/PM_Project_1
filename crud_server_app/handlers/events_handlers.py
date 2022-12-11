import os

from fastapi import FastAPI
from psycopg_pool import AsyncConnectionPool

from postgres_workers.users_worker import UserDataWorker
from postgres_workers.bets_worker import BetsDataWorker
from postgres_workers.events_worker import EventsDataWorker

connection_string = os.environ.get("DATABASE_LINK")
pool = AsyncConnectionPool(connection_string, open=False)


def startup_event_handler(app: FastAPI):
    async def wrapper():
        app.user_data_worker = UserDataWorker(pool=pool)
        app.bet_data_worker = BetsDataWorker(pool=pool)
        app.event_data_worker = EventsDataWorker(pool=pool)     # leave it here, because it required for checking event
        await pool.open(wait=True)                              # status, before creating bet
    return wrapper


def shutdown_event_handler(app: FastAPI):
    async def wrapper():
        await pool.close()
    return wrapper
