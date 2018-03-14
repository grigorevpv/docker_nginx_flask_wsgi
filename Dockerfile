FROM ubuntu:16.04

MAINTAINER Grigoryev Pavel

COPY ./ .
COPY ./project.service /etc/systemd/system

RUN apt-get update
RUN apt-get install python-pip -y
RUN apt-get install python-dev -y
RUN apt-get install nginx -y

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN pip install uwsgi
RUN pip install flask

EXPOSE 80

USER root

CMD uwsgi --ini project.ini