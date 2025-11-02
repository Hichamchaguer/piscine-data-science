# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy Python script
COPY script.py .

# Copy customer CSV folder
COPY customer/ ./customer/

# Install dependencies
RUN pip install --no-cache-dir psycopg2-binary pandas

# Run script
CMD ["python", "script.py"]
