FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /my-library
WORKDIR /my-library
ADD requirements.txt /my-library/
RUN pip install -r requirements.txt
ADD . /my-library/
RUN apt-get update && apt-get -y install postgresql
