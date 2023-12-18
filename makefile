THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build run stop restart  destroy log shell test

docker_file := docker-compose.yaml

help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null |	awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

build:
	docker-compose -f $(docker_file) build $(c)
run:
	docker-compose -f $(docker_file) up -d $(c)
stop:
	docker-compose -f $(docker_file) stop $(c)
restart:
	docker-compose -f $(docker_file) stop $(c)
	docker-compose -f $(docker_file) up -d $(c)
destroy:
	docker-compose -f $(docker_file) down -v $(c)
log:
	docker-compose -f $(docker_file) logs --tail=100 -f hml-app
shell:
	docker-compose -f $(docker_file) exec hml-app /bin/bash
test:
	docker-compose -f $(docker_file) exec hml-app python app.py test
