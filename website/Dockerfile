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

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get update
RUN apt install ./google-chrome-stable_current_amd64.deb -y

RUN chrome_version="$(google-chrome-stable --version)"
RUN echo "$chrome_version"

# RUN chrome_driver=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE") && echo "$chrome_driver"
# RUN curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/${chrome_driver}/chromedriver_linux64.zip"
# RUN apt install unzip
# RUN mkdir -p "chromedriver/stable"
# RUN dir -s
# RUN unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable" 
# RUN chmod +x "chromedriver/stable/chromedriver"

# Set up Chromedriver Environment variables
# ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/103.0.5060.134/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
RUN apt update
RUN apt-get install libgconf-2-4 -y

# copy project
COPY . .

EXPOSE 8000 

CMD python manage.py runserver 0.0.0.0:8000