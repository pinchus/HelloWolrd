import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s', force=True)


def say_hello():
    logging.info('add cmd')


if __name__ == '__main__':
    say_hello()
