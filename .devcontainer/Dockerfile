FROM python:3.8-buster

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    sqlite3 redis-tools
RUN pip3 install redis
ENV DEBIAN_FRONTEND=dialog
