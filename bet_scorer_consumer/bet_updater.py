import os
from json import loads

from postgres_workers.bets_worker import BetsDataWorker
from kafka_producers.bet_scorer_producer import BetProducer

connection_string = os.environ.get("DATABASE_LINK")


class BetUpdater:
    def __init__(self):
        self._database_worker = BetsDataWorker(connection_string=connection_string)
        self._kafka_producer = BetProducer()

    def update_bet(self, message) -> None:
        event_info = loads(message.value.decode('utf-8'))
        if event_info['state'] == 'active':
            self._change_bet_active(event_info)
        elif event_info['state'] == 'finished':
            self._change_bet_finished(event_info)
        else:
            pass

    def _change_bet_active(self, event_info: dict) -> None:
        event_id = event_info['id']
        bets = self._database_worker.read_record(str(event_id))
        if bets:
            event_winner = self._get_event_winner(event_info)
            for bet in bets:
                if self._bet_market_success(bet['market'], event_winner):
                    bet['state'] = 'winning'
                else:
                    bet['state'] = 'losing'
                self._kafka_producer.send(bet)

    def _change_bet_finished(self, event_info: dict) -> None:
        event_id = event_info['id']
        bets = self._database_worker.read_record(str(event_id))
        if bets:
            event_winner = self._get_event_winner(event_info)
            for bet in bets:
                if self._bet_market_success(bet['market'], event_winner):
                    bet['state'] = 'win'
                else:
                    bet['state'] = 'lose'
                self._kafka_producer.send(bet)

    @staticmethod
    def _get_event_winner(event_info: dict) -> int:
        game_scores = list(map(int, event_info['score'].split('-')))
        if game_scores[0] == game_scores[1]:
            return 0
        elif game_scores[0] > game_scores[1]:
            return 1
        else:
            return 2

    @staticmethod
    def _bet_market_success(bet_market: str, winner: int) -> bool:
        if bet_market == 'team_1':
            market = 1
        elif bet_market == 'team_2':
            market = 2
        else:
            market = 0

        return market == winner
