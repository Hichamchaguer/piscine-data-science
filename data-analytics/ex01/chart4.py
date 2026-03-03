# import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

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
        with open("chart4.sql", 'r') as file:
            request = file.read()
        cnx = connectToDB()
        if cnx is None:
            return
        cursor = cnx.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        day, average = zip(*data)
        # read the sql file
    
        print("average:", len(average), flush=True)
        print("day:", len(day), flush=True)
    
        plt.figure(figsize=(10, 6))
        plt.fill_between(day, average, alpha=0.4)
        plt.ylabel("Total Sales (in Altairian Dollars)")
        plt.xlabel("Months")
        position = [0, len(day) // 4, 2 * len(day) // 4, 3 * len(day) // 4]
        labels = ['Oct', 'Nov', 'Dec', 'Jan']
        plt.xticks(position, labels)
        plt.xlim(day[0], day[-1])
        plt.savefig("script/fill_chart.png", format="png")
        plt.close()
    except Exception as e:
        print(f"An error occurred: {e}", flush=True)
        return None


if __name__ == '__main__':
    load()
