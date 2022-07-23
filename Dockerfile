# Start point image: python 3.9.10 slim
# This image will be fetched from Docker Hub
FROM python:3.9.10-slim

# Allowed arguments while building Docker image
ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

# Create environment variables
ENV BASIC_AUTH_USERNAME=$BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD_ARG

# Copy the requirements.txt, 
# from the local file system into the Docker image
COPY ./requirements.txt /usr/requirements.txt

# Set the working folder 
WORKDIR /usr

# Since a container is already a virtual environment,
# we can install the required libs directly, without using a venv
RUN pip3 install -r requirements.txt

# Copy the remaining important folders to Docker image
COPY ./src /usr/src
COPY ./models /usr/models

# Define which command should be run
ENTRYPOINT [ "python3" ]

# Define which python script should be run
CMD [ "src/app/main.py" ]