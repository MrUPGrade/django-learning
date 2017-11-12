SHELL::=/bin/bash
RM=rm -Rfv

PYTHON=python
PIP=pip
MPY=$(PYTHON) mysite/manage.py

DC=docker-compose --no-ansi
D=docker

clean-pyc:
	find . -name '*.pyc' -exec rm -fv {} +
	find . -name '*.pyo' -exec rm -fv {} +

clean-test:
	$(RM) .cache
	$(RM) .coverage

clean-build:
	$(RM) *.egg-info
	$(RM) graph_output
	$(RM) artifacts
	$(RM) build/
	$(RM) dist/

clean-log:
	$(RM) *.log

clean: clean-pyc clean-test clean-build clean-log


pip-install-app:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
	$(PIP) install --upgrade -r requirements.txt

pip-install-dev:
	$(PIP) install --upgrade -r requirements-dev.txt

pip-install-test:
	$(PIP) install --upgrade -r requirements-test.txt

pip-install: pip-install-app pip-install-test pip-install-dev


test:
	pytest

dj-migrate:
	$(MPY) migrate

dj-makemigrations:
	$(MPY) makemigrations

dj-shell:
	$(MPY) shell

dj-clean-media:
	$(RM) mysite/media/

sleep:
	sleep 5

dc-ps:
	$(DC) ps

dc-up:
	$(DC) up -d

dc-down:
	$(DC) down -v

dc-stop:
	$(DC) stop

dc-tail:
	$(DC) logs -f

dc-logs:
	$(DC) logs --tail=60

mys-initusers:
	$(MPY) initusers

mys-populatedb:
	$(MPY) populatedb

perf-simple-test:
	locust -f perftest/locustfile.py --host=http://localhost:8000 --no-web -c 20 -r 4 -t 2m


CELERY_HOSTNAME=$(shell hostname)-$(shell echo $$PPID)
celery-run:
	echo $(HOSTNAME)
	celery worker  --workdir mysite/ -A mysite.celery -E -l info -n worker@$(CELERY_HOSTNAME) -Q celery,slow

celery-events:
	celery events --workdir mysite/ -A mysite.celery

DOCKERFILES_DIR=ops/docker
DOCKER_REPO_TAG=mrupgrade
BASE_IMG=$(DOCKER_REPO_TAG)/djl-base
BASE_IMG_TAG=$(BASE_IMG):1

SRC_ROOT=$(shell pwd)
export USER_ID=$(shell id -u)

ci-build-image-base:
	$(D) build -t $(BASE_IMG_TAG) -f $(DOCKERFILES_DIR)/base.Dockerfile .
	$(D) tag $(BASE_IMG_TAG) $(BASE_IMG):latest


DJL_CI_ENV_NAME?=djltest
DCP=$(DC) -p $(DJL_CI_ENV_NAME) -f ops/docker/test.docker-compose.yaml

ci-env-prep:
	$(DCP) up --no-start
	$(DCP) start db
	$(DCP) start cache

ci-run-tests:
	$(DCP) run tests

ci-env-clean:
	$(DCP) down -v


tg-ci-run: ci-env-prep sleep ci-run-tests ci-env-clean

tg-env-reset: dc-down clean dj-clean-media dc-up sleep dj-migrate mys-populatedb
