import psycopg2
import sys

DB_HOST = "postgres"
DB_NAME = "piscineds"
DB_USER =   "hchaguer"
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
        print(f"An error occurred while connecting to the database: {error}", flush=True, file=sys.stderr)
        return None


def load():
    try:
        # read the sql file
        print("Reading SQL file...", flush=True)
        with open("fusion.sql", 'r') as file:
            sql_commands = file.read()
        print("SQL file read successfully", flush=True)
        
        # call connect function
        cnx = connect()
        if cnx is None:
            print("Connection to the database failed", flush=True, file=sys.stderr)
            sys.exit(1)
        
        # execute the sql commands
        print("Executing SQL commands...", flush=True)
        cursor = cnx.cursor()
        cursor.execute(sql_commands)

        # commit changes
        cnx.commit()
        print("Data fusion completed successfully.", flush=True)
        # close the cnx and cursor
        cursor.close()
        cnx.close()
    except FileNotFoundError as error:
        print(f"File not found error: {error}", flush=True, file=sys.stderr)
        sys.exit(1)
    except psycopg2.Error as error:
        print(f"PostgreSQL error: {error}", flush=True, file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"An error occurred: {error}", flush=True, file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    load()