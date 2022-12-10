from postgres_workers.main_worker import MainDatabaseWorker


class QueryMaker(MainDatabaseWorker):
    def __init__(self, connection_string: str = None,
                 table_name: str = None,
                 cols_names: tuple = None):
        self._connection_string = connection_string
        self._table_name = table_name
        self._cols_names = ', '.join(cols_names)
        self._cols_amount = len(cols_names)

    def read_record(self, idn: str) -> list | dict:
        if idn.isdigit():
            query = f'SELECT * FROM {self._table_name} WHERE eventId={idn};'
            return self._read_record(query)

