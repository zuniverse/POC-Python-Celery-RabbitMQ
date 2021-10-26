FROM python:3.9.7-alpine3.14

# Add bash for alpine. --no-cache keeps size smaller.
RUN apk add --no-cache bash

# logs :
ENV PYTHONUNBUFFERED 1

# set up virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set working directory
RUN mkdir /app
WORKDIR /app/

# install required libraries
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy source code into working directory
COPY ./celery_app/ /app/

# sugar
RUN echo "alias ll='ls -alF'" >> ~/.bashrc

# Run the app
CMD ["python"]