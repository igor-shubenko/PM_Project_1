from postgres_workers.query_maker import QueryMaker


class BetsDataWorker(QueryMaker):
    def __init__(self, connection_string=None,
                 table_name='Bets',
                 cols_names=('date_created',
                             'userId',
                             'eventId',
                             'market',
                             'state')):
        super().__init__(connection_string=connection_string, table_name=table_name, cols_names=cols_names)
