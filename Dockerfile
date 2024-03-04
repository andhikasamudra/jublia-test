FROM python:3.12.2-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install python-dotenv gunicorn

EXPOSE 8080

ENV FLASK_APP manage.py

CMD ["gunicorn", "manage:app", "-b", "0.0.0.0:8080", "--log-level", "debug"]