import psycopg
from psycopg.rows import dict_row


class MainDatabaseWorker:
    """Class implements methods for executing queries, prepared by child class"""
    def __init__(self, connection_string: str = None):
        self._connection_string = connection_string

    def _execute_query(self, query: str, values: tuple = None) -> list:
        """Executes queries to database"""
        with psycopg.connect(self._connection_string, row_factory=dict_row) as conn:
            with conn.cursor() as curr:
                return curr.execute(query, values).fetchall()

    def _read_record(self, query: str) -> list | dict:
        """Reads data from database"""
        try:
            result = self._execute_query(query)
        except Exception as e:
            print("Exeption: ", e)
        else:
            return result
