from psycopg2 import sql

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
        print("Connection to the database was successful")
        return cnx
    except Exception as error:
        print(f"An error occurred while connecting to the database: {error}")
        return None


def load():
    try:
        # read the sql file
        with open("fusion.sql", 'r') as file:
            sql_commands = file.read()
        # call connect function
        cnx = connect()
        if cnx is None:
            return
        
        # execute the sql commands
        cursor = cnx.cursor()
        cursor.execute(sql_commands)

        # commit changes
        cnx.commit()
        print("Data fusion completed successfully.")
        # close the cnx and cursor
        cursor.close()
        cnx.close()
    except Exception as error:
        print(f"An error occurred: {error}")
        return None