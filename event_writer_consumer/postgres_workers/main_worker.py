import psycopg


class MainDatabaseWorker:
    def __init__(self, connection_string: str):
        self._connection_string = connection_string

    def _execute_query(self, query: str, values: tuple = None):
        """Executes queries to database"""
        with psycopg.connect(self._connection_string) as conn:
            with conn.cursor() as curr:
                curr.execute(query, values)
                conn.commit()

    def _create_record(self, query: str, values: tuple) -> None:
        """Makes create query"""
        try:
            self._execute_query(query, values)
        except Exception as e:
            print("Exception:", e)

    def _update_record(self, query: str) -> None:
        """Makes update query"""
        try:
            self._execute_query(query)
        except Exception as e:
            print("Exception:", e)
