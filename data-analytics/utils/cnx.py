import psycopg2

DB_HOST = "postgres"
DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "mysecretpassword"
DB_PORT = 5432


def connect():
    try:
        cnx = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connection to the database was successful", flush=True)
        return cnx
    except Exception as error:
        print(f"An error occurred while connecting to the database: {error}", flush=True)
        return None
