# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy Python script and SQL file
# COPY ./data-analytics/ex00/pie.py .
# COPY ./data-analytics/ex00/pie.sql .
COPY ./data-analytics/ex01/chart.sql .
COPY ./data-analytics/ex01/chart.py .


# Install dependencies
RUN pip install --no-cache-dir psycopg2-binary matplotlib

# Run script
CMD ["python", "chart.py"]