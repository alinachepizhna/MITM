FROM python:3.9-slim

WORKDIR /app

# Copy the server.py script into the container
COPY server.py /app/

# Install necessary dependencies
RUN pip install flask

# Run the server Flask app
CMD ["python", "server.py"]
