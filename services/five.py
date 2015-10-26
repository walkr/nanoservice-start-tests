import sys
import logging
from nanoservice import Service


def test():
    return 'Hello from five'


def main():
    logging.basicConfig(level=logging.DEBUG)

    address = sys.argv[1]
    service = Service(address)

    service.register('test', test)
    service.start()

if __name__ == '__main__':
    main()
