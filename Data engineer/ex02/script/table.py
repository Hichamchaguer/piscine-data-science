import psycopg2
import pandas as pd
from psycopg2 import sql

# Database connection parameters

DB_HOST = "postgres"
DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "mysecretpassword"
DB_PORT = 5432

def connectToDB():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connection to the database was successful")
        return conn
    except Exception as error:
        print(f"An error occurred while connecting to the database: {error}")
        return None

def ifTableExists(cursor, table_name):
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = %s
        );
    """, (table_name,))
    return cursor.fetchone()[0]

def create_table(path, table_name):
    try:
        # Connect to PostgreSQL
        cnx = connectToDB()
        if cnx is None:
            return
        cursor = cnx.cursor()

        if not ifTableExists(cursor, table_name):
            print(f"Creating table {table_name} if not exists...")

            # Use positional placeholder {} and format with sql.Identifier to avoid
            # KeyError from named placeholders like {table_name}.
            create_query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS {} (
                    event_time TIMESTAMP,
                    event_type VARCHAR(50),
                    product_id INTEGER,
                    price FLOAT,
                    user_id INTEGER,
                    user_session VARCHAR(100)
                )
            """).format(sql.Identifier(table_name))

            cursor.execute(create_query)
            cnx.commit()
            print(f"Table {table_name} created successfully or already exists.")
            print(f"Loading CSV data into {table_name}...")

            # Load CSV into the table using COPY. Ensure column names match the table
            # definition (event_type, not evnet_type).
            with open(path, 'r') as f:
                next(f)  # skip header
                cursor.copy_expert(sql.SQL("""
                    COPY {} (event_time, event_type, product_id, price, user_id, user_session)
                    FROM STDIN WITH CSV
                """).format(sql.Identifier(table_name)), f)
            cnx.commit()
            print(f"Data loaded into {table_name} successfully.")
        else:
            print(f"Table {table_name} already exists. Skipping creation and data load.")
        cursor.close()
        cnx.close()
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
        # Now proceed with table creation
    create_table("/app/customer/data_2023_jan.csv", "data_2023_jan")
