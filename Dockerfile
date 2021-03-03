# Reference: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# Pull base image
FROM public.ecr.aws/lambda/python:3.8

# setup virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Create a User ( not a Group )
ARG HOME=/home/$USER
WORKDIR "$HOME"

RUN whoami

# Copy source code to working directory
COPY ./src .

# Run lambda
CMD ["demo_lambda.rm_handler"]