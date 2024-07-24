# syntax=docker/dockerfile:1

# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app
RUN pip3 install pandas==2.2.2
RUN pip3 install pytest==7.4.2
VOLUME ./:/app/


# Set the default command to run when the container starts
CMD ["bash"]
