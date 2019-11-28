FROM python:3.7.4
LABEL maintainer="halvong@yahoo.com"

#avoids buffered
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

#creates user for running appl.
RUN useradd -ms /bin/bash mike
