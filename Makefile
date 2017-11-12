SHELL::=/bin/bash
RM=rm -Rfv

PYTHON=python
PIP=pip
MPY=$(PYTHON) mysite/manage.py

DC=docker-compose --no-ansi
DOCKER=docker

clean-pyc:
	find . -name '*.pyc' -exec rm -fv {} +
	find . -name '*.pyo' -exec rm -fv {} +

clean-test:
	$(RM) .cache
	$(RM) .coverage

clean: clean-pyc clean-test
	$(RM) *.log
	$(RM) *.egg-info
	$(RM) graph_output
	$(RM) artifacts
	$(RM) build/
	$(RM) dist/


pip-install-app:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
	$(PIP) install --upgrade -r requirements.txt

pip-install-dev:
	$(PIP) install --upgrade -r requirements-dev.txt

pip-install-test:
	$(PIP) install --upgrade -r requirements-test.txt

pip-install: pip-install-app pip-install-test pip-install-dev

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




env-reset: dc-down clean dj-clean-media dc-up sleep dj-migrate mys-populatedb
