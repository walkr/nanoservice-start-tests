.PHONY: help

help:
	@echo "USAGE:"
	@echo
	@echo "1) Start nanoservices via 'make start'"
	@echo "2) In a different shell execute 'make test' to call them"
	@echo

start:
	@honcho start &

test:
	@python test.py