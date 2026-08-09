FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN DEBUG=False python manage.py collectstatic --noinput

CMD exec gunicorn --bind :${PORT:-8080} --workers 1 --threads 8 --timeout 0 notes_project.wsgi:application