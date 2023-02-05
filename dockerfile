FROM python:3.11.1-buster

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/YoutubeApi

COPY ./YoutubeApi .
COPY ./requirements.txt /usr/src/YoutubeApi

RUN pip install -r requirements.txt

# django-crontab logfile
RUN mkdir /log
RUN touch /debug.log

EXPOSE 8000

CMD service cron start && python manage.py runserver 0.0.0.0:8000