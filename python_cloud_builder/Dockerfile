# This Dockerfile is used to build a custom cloud builder. It can be used for
# muliple projects so it should not include any project-specific components.
# It pulls the public Python 3 image from Dockerhub (https://hub.docker.com/python)
# To create the image first cd to this folder thrn from the command line:
#   gcloud builds submit --config=cloudbuild.yaml .

FROM python:3

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip


