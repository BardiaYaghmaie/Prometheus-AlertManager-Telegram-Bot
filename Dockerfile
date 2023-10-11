# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 8776

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8776"]