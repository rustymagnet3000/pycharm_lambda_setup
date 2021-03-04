# Define global args
ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.7"
ARG HOME="/home/"

# Pull base image. Purposely removed #amazon/aws-lambda-python:3.7
FROM python:${RUNTIME_VERSION}-slim

# setup virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependencies file
COPY requirements.txt .

# Extend preferred base images to be Lambda compatible.
RUN pip install awslambdaric --target "${FUNCTION_DIR}"

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code to working directory
ARG FUNCTION_DIR
ARG RUNTIME_VERSION
RUN mkdir -p ${FUNCTION_DIR}
COPY src/ ${FUNCTION_DIR

# run code
ENTRYPOINT [ "python", "-m", "awslambdaric" ]
CMD [ "demo_lambda.handler" ]