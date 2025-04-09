# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the X display
ENV DISPLAY=host.docker.internal:0.0

# Expose the port (if required)
EXPOSE 5000

# Command to run the app
CMD ["python", "app/gui.py"]
