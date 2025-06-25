# Use an official Python base image
FROM python:3.9-slim

# Copy the current directory contents into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Set the command to run the app
CMD ["python", "app.py"]
