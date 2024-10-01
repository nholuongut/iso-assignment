FROM python:3.10.5-slim

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD [ "python", "src/api/main.py" ]
