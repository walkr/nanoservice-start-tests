nanoservice-start-tests
========================

Test if a collection of nanoservices start properly


## Usage


### Install

```shell
$ make install
```


### Start services

```shell
$ make start

13:36:34 one.1   | INFO:root:Service started on tcp://127.0.0.1:5001
13:36:34 four.1  | INFO:root:Service started on tcp://127.0.0.1:5004
13:36:34 seven.1 | INFO:root:Service started on tcp://127.0.0.1:5007
13:36:34 three.1 | INFO:root:Service started on tcp://127.0.0.1:5003
13:36:34 five.1  | INFO:root:Service started on tcp://127.0.0.1:5005
13:36:34 six.1   | INFO:root:Service started on tcp://127.0.0.1:5006
13:36:34 two.1   | INFO:root:Service started on tcp://127.0.0.1:5002
```


### Then in a different shell

```shell
$ make test

Hello from one     - 1.09 ms
Hello from two     - 1.10 ms
Hello from three   - 1.54 ms
Hello from four    - 0.64 ms
Hello from five    - 0.55 ms
Hello from six     - 0.55 ms
Hello from seven   - 0.48 ms
```
