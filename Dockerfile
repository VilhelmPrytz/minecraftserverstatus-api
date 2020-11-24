FROM python:3.9-slim

WORKDIR /var/www/app

COPY . /var/www/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "app:app" ]
