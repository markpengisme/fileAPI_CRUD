FROM python:3.8.12

WORKDIR /usr/src/fileAPI

COPY fileAPI /usr/src/fileAPI

RUN apt update
RUN pip install -r requirements.txt
RUN mkdir /file

CMD python manage.py runserver 0.0.0.0:8000

