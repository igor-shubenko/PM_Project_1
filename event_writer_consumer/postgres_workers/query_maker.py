from postgres_workers.main_worker import MainDatabaseWorker


class QueryMaker(MainDatabaseWorker):
    def __init__(self, connection_string: str = None,
                 table_name: str = None,
                 cols_names: tuple = None):
        self._connection_string = connection_string
        self._table_name = table_name
        self._cols_names = ', '.join(cols_names)
        self._cols_amount = len(cols_names)

    def create_record(self, data: dict) -> dict:
        query = f"INSERT INTO {self._table_name}({self._cols_names}) VALUES" \
                f"({', '.join(['%s'] * self._cols_amount)});"
        values = tuple(data.values())
        return self._create_record(query, values)

    def update_record(self, idn: int, data: dict) -> dict:
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

        return self._update_record(query)
