FROM python:3.5
MAINTAINER raccoony <raccoonyy@gmail.com>

RUN \
    apt-get update &&\
    apt-get -y install \
        libpq-dev \
        python-dev

WORKDIR /app

ADD    ./manage.py                    /app/
ADD    ./start.sh       /start.sh
RUN    chmod +x /*.sh
CMD    ['supervisord', '-n']