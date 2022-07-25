# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --default-timeout=100 -r requirements.txt

# copy project
COPY . .

EXPOSE 8000 

CMD python manage.py runserver 0.0.0.0:8000