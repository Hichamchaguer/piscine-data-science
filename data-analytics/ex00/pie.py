import psycopg2
import matplotlib.pyplot as plt

DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "password"
DB_HOST = "localhost"   
DB_PORT = "5432"

def connect():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def fetch_data():
    try:
        with open("pie.sql", "r") as file:
            request = file.read()
        print("SQL Request fetched successfully.")
        # cnx to db
        cnx = connect()
        if cnx is None:
            return None
        # call cursor
        cursor = cnx.cursor()
        # execute the request
        cursor.execute(request)
        print("SQL Request executed successfully.")
        # fetch the data
        data = cursor.fetchall()
        print("Data fetched successfully.")
        event, count = zip(*data)
        # put data in a pie chart
        plt.pie(count, labels=event, autopct='%1.1f%%', startangle=140, shadow=True)
        plt.show()

        cursor.close()
        cnx.close()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None