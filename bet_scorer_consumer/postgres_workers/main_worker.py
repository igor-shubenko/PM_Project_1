import psycopg
from psycopg.rows import dict_row


class MainDatabaseWorker:
    def __init__(self, connection_string: str = None):
        self._connection_string = connection_string

    def _execute_query(self, query: str, values: tuple = None):
        """Executes queries to database, returns Cursor object"""
        with psycopg.connect(self._connection_string, row_factory=dict_row) as conn:
            with conn.cursor() as curr:
                return curr.execute(query, values).fetchall()

    def _read_record(self, query: str) -> list | dict:
        try:
            result = self._execute_query(query)
        except Exception:
            pass
        else:
            return result


