from kafka import KafkaConsumer
import uvicorn


from bet_updater import BetUpdater


consumer = KafkaConsumer('events.taxonomy',
                         bootstrap_servers=['kafka:9092'],
                         client_id='bet_scorer_consumer',
                         group_id='bet_scorer_consumer')


bet_updater = BetUpdater()


def main():
    for message in consumer:
        bet_updater.update_bet(message)


if __name__ == '__main__':
    uvicorn.run('main:main', host='0.0.0.0', port=8763, workers=1, reload=True)
