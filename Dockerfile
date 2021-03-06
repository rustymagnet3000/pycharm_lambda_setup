# Define global args
ARG RUNTIME_VERSION="3.7"
ARG FUNCTION_DIR="/home/app/"

# Pull base image. Purposely removed #amazon/aws-lambda-python:3.7
FROM python:${RUNTIME_VERSION}-slim

# Set up ( and activate ) virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN echo $PATH
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Extend preferred base images to be Lambda compatible.
RUN pip install awslambdaric --target "${PWD}"

# Copy source code to working directory
COPY ./src .

# Run lambda
WORKDIR /var/task/
RUN echo "$PWD"
RUN ls -l
CMD [ "app.handler" ]