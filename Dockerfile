FROM python:3.7-slim-buster
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]