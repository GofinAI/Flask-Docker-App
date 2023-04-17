# syntax=docker/dockerfile:1

#FROM python:3.11-slim-buster
FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
