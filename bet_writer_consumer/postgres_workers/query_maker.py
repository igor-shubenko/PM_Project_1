from json import loads

from postgres_workers.main_worker import MainDatabaseWorker


class QueryMaker(MainDatabaseWorker):
    """Class prepare queries for different tables of database according to a template.
            Takes a table name and names of table cols and connection_string
            for connection to database"""
    def __init__(self, connection_string: str = None,
                 table_name: str = None,
                 cols_names: tuple = None):
        self._connection_string = connection_string
        self._table_name = table_name
        self._cols_names = ', '.join(cols_names)
        self._cols_amount = len(cols_names)

    def update_record(self, data) -> None:
        """Prepare update query and transfer it for further execution"""
        data = loads(data.value.decode('utf-8'))    # dict after this operation
        idn = data.pop('id')                        # taking id of record in database
        data = {k: v for k, v in data.items() if v is not None}
        query_start = f"UPDATE {self._table_name} SET "
        temp_strings = []

        for k, v in data.items():
            if type(v) is str:
                temp_string = f"{k}='{v}'"
            else:
                temp_string = f"{k}={v}"
            temp_strings.append(temp_string)
        query = query_start + ', '.join(temp_strings) + f' WHERE id={idn};'

        self._update_record(query)
