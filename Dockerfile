# Dockerfile
FROM python:3.9

WORKDIR /app

# Copy the semantic.py file into the image
COPY semantic.py .

# Install the project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Other instructions to run your application
