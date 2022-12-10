from json import loads

from postgres_workers.query_maker import QueryMaker


class KafkaEventsDataWorker(QueryMaker):
    def __init__(self, connection_string: str = None,
                 table_name='Events',
                 cols_names=('type',
                             'name',
                             'event_date',
                             'score',
                             'state')):
        super().__init__(connection_string=connection_string,
                         table_name=table_name, cols_names=cols_names)

    def write_or_update_data(self, message):
        values = loads(message.value.decode('utf-8'))
        if 'id' in values:
            idn = values.pop('id')
            self.update_record(idn, values)
        else:
            self.create_record(values)
