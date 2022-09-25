FROM python:3.10
WORKDIR /home/user/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
RUN apt-get update && apt-get -y install cron vim

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
