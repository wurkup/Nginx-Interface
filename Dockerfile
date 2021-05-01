FROM python:3.8-slim

ADD static static
ADD templates templates
ADD *.py *.txt /

WORKDIR /

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python server.py