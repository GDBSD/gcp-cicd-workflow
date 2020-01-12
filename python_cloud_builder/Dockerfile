# This Dockerfile is used to build a custom cloud builder. It can be used for
# muliple projects so it should not include any project-specific components.
# It pulls the public Python 3 image from Dockerhub (https://hub.docker.com/python)
# To create the image first cd to this folder thrn from the command line:
#   gcloud builds submit --config=cloudbuild.yaml .

# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip

RUN pip install pytest

RUN pip install coverage

RUN pip install pytest-cov

#RUN pip install Flask gunicorn

# Run a web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
#CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 app:app



