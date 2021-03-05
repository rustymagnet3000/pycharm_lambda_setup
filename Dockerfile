# Pull base image. Purposely removed #amazon/aws-lambda-python:3.7
FROM amazon/aws-lambda-python:3.7

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

# Copy source code to working directory
COPY ./src .
RUN echo "$PWD"
# Run lambda
CMD [ "app.handler" ]