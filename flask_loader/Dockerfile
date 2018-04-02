FROM ubuntu:16.04

MAINTAINER Grigoryev Pavel

COPY ./ .

RUN apt-get update
RUN apt-get install python-pip -y
RUN apt-get install python-dev -y

RUN pip install uwsgi
RUN pip install flask
RUN pip install statsd

USER root

CMD uwsgi --socket 0.0.0.0:80 --workers 4 --protocol=http -w main:application