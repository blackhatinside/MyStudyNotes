# Define a base for your image
FROM python:3.8

# Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, ADD instructions that follow in the Dockerfile
WORKDIR /app

# COPY files from source (in host system) to destination (in the docker's file system)
COPY requirements.txt .

# Executes commands in current image
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# service listening on which port
EXPOSE 8000

# Define the default program that is run once you start the container based on this image
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
