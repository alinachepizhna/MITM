FROM python:3.9-slim

WORKDIR /app

# Copy the client.py script into the container
COPY client.py /app/

# Install dependencies
RUN pip install requests

# Run the client script
CMD ["python", "client.py"]
