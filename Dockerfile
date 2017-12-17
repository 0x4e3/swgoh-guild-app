FROM python:3.6.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app

RUN pip install -r requirements/local.txt

CMD python manage.py runserver 0.0.0.0:8000
