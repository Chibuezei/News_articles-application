# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY requirement.txt /code/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . //home/muy/Desktop/me_write/pythian/trydjango/code