import time
from nanoservice import Client


def main():
    clients = []
    for port in range(5001, 5008):
        clients.append(Client('tcp://127.0.0.1:{}'.format(port)))

    for c in clients:
        start = time.time()
        result, error = c.call('test')
        print('{:18} - {:.2f} ms'.format(result,
                                         (time.time() - start) * 1000))

if __name__ == '__main__':
    main()
