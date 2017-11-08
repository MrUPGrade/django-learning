SHELL::=/bin/bash
RM=rm -Rfv

PYTHON=python
PIP=pip

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

pip-install:
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
	$(PIP) install --upgrade -r requirements.txt
	$(PIP) install --upgrade -r requirements-dev.txt
