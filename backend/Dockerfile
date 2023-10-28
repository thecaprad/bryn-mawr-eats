# pull official base image
FROM python:3.8.13-bullseye

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . .
