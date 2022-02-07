FROM python:3.10-alpine

RUN mkdir /ssl

COPY ./ .

RUN rm -r venv

CMD [ "python", "main.py"]