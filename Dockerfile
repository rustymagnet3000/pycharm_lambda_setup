# Reference: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
# Pull base image ( slim )
FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Create a User ( not a Group )
ENV USER=foobar
ENV UID=1001
ARG HOME=/home/$USER

# Add user, with no password
RUN adduser \
    --uid "$UID" \
    --home "$HOME" \
    --disabled-password \
    "$USER"

# Run Container as user
USER "$USER"
RUN whoami
WORKDIR "$HOME"

# Copy source code to working directory
COPY ./src .

# Container start
CMD [ "python", "./main.py" ]