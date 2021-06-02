FROM python:3.7-slim-buster
WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV PORT 8000
ENV STATIC_ROOT /static
ENV MEDIA_ROOT /media
RUN python manage.py collectstatic --noinput

CMD ["/docker-entrypoint.sh"]
