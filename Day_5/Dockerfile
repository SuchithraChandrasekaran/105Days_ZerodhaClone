# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Define the default command
CMD ["python", "-m", "py_compile", "app/SimulateBuySell.py"]
