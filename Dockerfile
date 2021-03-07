# Define global args
ARG RUNTIME_VERSION="3.7"

# Pull base image
FROM public.ecr.aws/lambda/python:${RUNTIME_VERSION}

# Set up ( and activate ) virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy source code to working directory
COPY ./src ${LAMBDA_TASK_ROOT}

# Run lambda
WORKDIR ${LAMBDA_TASK_ROOT}
CMD [ "app.handler" ]