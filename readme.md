## Jublia Test

## Run Application

1. non docker compose run

setup virtual environment

```shell
python3 -m venv .venv
```

copy the `env.example.sh` to `env.sh`
```shell
cp .env.example env
```

install the requirements

```shell
pip install -r requirements.txt
```

setup Flask App
```shell
export FLASK_APP="manage.py"
```

run Migration

```shell
flask db upgrade
```

run Flask

```shell
gunicorn manage:app -b 0.0.0.0:8080
```

run celery worker on different terminal tab
```shell
celery -A celery_config beat -l info
celery -A celery_config worker -l info
```

2. using docker compose

copy `.env.example` to `.env`

```shell
cp .env.example .env
```

run docker compose
```shell
docker-compose up -d
```

access it with curl
```shell
curl --location 'http://127.0.0.1:8080/save_emails' \
--header 'Content-Type: application/json' \
--data '{
    "event_id" : 123,
    "subject" : "testing",
    "content": "testing",
    "sent_timestamp": "05 Mar 2024 11:31"
}'
```

or postman collection at
```shell
(project dir)/Jublia Test API.postman_collection.json
```
