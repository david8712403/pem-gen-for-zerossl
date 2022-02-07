FROM python:3.10-alpine

RUN mkdir /ssl

COPY ./ .

CMD [ "python", "main.py"]