FROM python:3.6-stretch

ADD requirements*.txt /

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade -r /requirements.txt && \
    pip install --upgrade -r /requirements-test.txt && \
    pip install --upgrade -r /requirements-dev.txt

VOLUME /src
WORKDIR /src
