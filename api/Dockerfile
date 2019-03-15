FROM python:3.7.2

USER root

RUN mkdir /webapp

COPY . /webapp

WORKDIR /webapp

RUN pip install -r requirements.txt

RUN rm -rf celerybeat.pid

EXPOSE 80

CMD ["python3","/webapp/run.py"]
