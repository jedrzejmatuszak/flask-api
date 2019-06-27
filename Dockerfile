FROM python:3.6-alpine

RUN adduser -D task

WORKDIR /home/task

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY task.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP task.py

RUN chown -R task:task ./
USER task

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]