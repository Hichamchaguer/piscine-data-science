# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy Python script and SQL file
COPY ./data-warehouse/ex01/customers_table.py .
COPY ./data-warehouse/ex01/customers_table.sql .

# Copy customer CSV folder
COPY ./customer ./customer/
COPY ./item ./item/

# Install dependencies
RUN pip install --no-cache-dir psycopg2-binary pandas

# Run script
CMD ["python", "customers_table.py"]
