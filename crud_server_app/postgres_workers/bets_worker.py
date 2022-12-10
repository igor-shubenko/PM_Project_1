from postgres_workers.query_maker import QueryMaker
from psycopg_pool import AsyncConnectionPool
import asyncio
from fastapi import FastAPI


class BetsDataWorker(QueryMaker):
    def __init__(self, pool: AsyncConnectionPool = None,
                 table_name='Bets',
                 cols_names=('date_created',
                             'userId',
                             'eventId',
                             'market',
                             'state')):
        super().__init__(pool=pool, table_name=table_name, cols_names=cols_names)

    async def create_record_if_possible(self, data: dict, app: FastAPI) -> dict:
        event_id = data['eventId']
        event_info = await asyncio.create_task(app.event_data_worker.read_record(str(event_id)))
        if event_info[0]['state'] == 'created':
            data['state'] = "None"
            return await self.create_record(data)
        else:
            return {"Error": "Can't create bet"}


