# import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

DB_HOST = "postgres"
DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "mysecretpassword"
DB_PORT = 5432

# connection function 

def connectToDB():
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


def load():
    try:
        with open("chart.sql", 'r') as file:
            request = file.read()
        cnx = connectToDB()
        if cnx is None:
            return
        # read the sql file
        cursor = cnx.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        event_time, event_type, purchase_count = zip(*data)

        plt.figure(figsize=(12, 8))
        plt.plot(event_time, purchase_count, linestyle='-')
        plt.ylabel("Number of customers")
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x / 10)}'))
        tick_positions = [0, len(event_time) // 4, 2 * len(event_time) // 4, 3 * len(event_time) // 4]
        tick_labels = ["Oct", "Nov", "Dec", "Jan"]
        plt.xticks(tick_positions, tick_labels)
        plt.xlim(event_time[0], event_time[-1])
        plt.savefig("script/line_chart.png", format="png")
        plt.close()
    except Exception as e:
        print(f"An error occurred: {e}", flush=True)
        return None


if __name__ == '__main__':
    load()
