import psycopg2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "mysecretpassword"
DB_HOST = "postgres"   
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
        print("Reading SQL file pie.sql ...", flush=True)
        with open("pie.sql", "r") as file:
            request = file.read()
        # cnx to db
        cnx = connect()
        if cnx is None:
            print("Connection to the database failed", flush=True)
            return None
        print("SQL Request fetched successfully.", flush=True)
        # call cursor
        cursor = cnx.cursor()
        # execute the request
        cursor.execute(request)
        print("SQL Request executed successfully.", flush=True)
        # fetch the data
        data = cursor.fetchall()
        print("Data fetched successfully.", flush=True)
        event, count = zip(*data)
        print(f"Event types: {event}", flush=True)
        print(f"Counts: {count}", flush=True)
        # put data in a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(count, labels=event, autopct='%1.1f%%', startangle=140, shadow=True)
        # Save into the mounted 'visualisation' folder so it's visible on the host
        plt.savefig("script/pie_chart.png", format="png")
        plt.close()

        cursor.close()
        cnx.close()
    except Exception as e:
        print(f"Error fetching data: {e}", flush=True)
        return None


if __name__ == "__main__":
    fetch_data()