.PHONY: help

help:
	@echo
	@echo "USAGE: make [option]"
	@echo
	@echo "make install - install"
	@echo "make start   - start nanoservices"
	@echo "make test    - run basic tests"
	@echo

install:
	@pip install -r requirements.txt

start:
	@honcho start

test:
	@python test.py