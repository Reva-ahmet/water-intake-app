FROM python:3.11-slim

# Install minimal system dependencies
RUN apt-get update && apt-get install -y \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY main.py .

# Expose the port for the web interface
EXPOSE 8502

# Run the app in web mode
CMD ["python", "main.py", "--web", "--port", "8502"]