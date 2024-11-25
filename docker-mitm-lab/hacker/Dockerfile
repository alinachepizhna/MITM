FROM python:3.9-slim

WORKDIR /app

# Copy the hacker.py script into the container
COPY hacker.py /app/

# Install necessary dependencies
RUN pip install flask requests

# Run the hacker Flask app
CMD ["python", "hacker.py"]
