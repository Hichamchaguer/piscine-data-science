# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy Python script and SQL file
# COPY ./data-analytics/ex00/pie.py .
# COPY ./data-analytics/ex00/pie.sql .
COPY ./data-analytics/ex01/chart.sql .
COPY ./data-analytics/ex01/chart.py .
# COPY ./data-analytics/ex01/chart2.sql .
# COPY ./data-analytics/ex01/chart2.py .
# COPY ./data-analytics/ex01/chart4.sql .
# COPY ./data-analytics/ex01/chart4.py .
# COPY ./data-analytics/ex02/mustache.sql .
# COPY ./data-analytics/ex02/mustache.py .
# COPY ./data-analytics/ex02/mustache2.sql .
# COPY ./data-analytics/ex03/Building.py .
# COPY ./data-analytics/ex03/Building.sql .
# COPY ./data-analytics/ex03/Building1.sql .
COPY ./data-analytics/ex04/elbow.py .
COPY ./data-analytics/ex04/elbow.sql .
COPY ./data-analytics/ex05/Clustering.py .
COPY ./data-analytics/ex05/Clustering.sql .
COPY ./data-analytics/utils ./utils/


# Install dependencies
RUN pip install --no-cache-dir psycopg2-binary matplotlib scikit-learn numpy pandas

# Run script
CMD ["python", "Clustering.py"]