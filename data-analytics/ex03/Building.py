import matplotlib.pyplot as plt
import psycopg2
from utils.cnx import connect


def freq():
    with (open('Building.sql', 'r')) as file:
        data = file.read()
    with (open('Building1.sql', 'r')) as file:
        data1 = file.read()
        print("SQL query loaded successfully.", flush=True)
    cnx = connect()
    if cnx is None:
        print("Failed to connect to the database.", flush=True)
        return
    print("Connected to the database successfully.", flush=True)
    cursor = cnx.cursor()
    cursor.execute(data)
    result = cursor.fetchall()
    cursor.execute(data1)
    result1 = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Extracting the data for plotting

    count = [row[1] for row in result if row[1] <= 40]
    plt.figure(figsize=(15, 6))
    plt.grid(True, zorder=-1)
    plt.hist(count, bins=5, edgecolor='k')
    plt.xlabel('frenquency')
    plt.ylabel('customers')
    plt.xticks(range(0, 40, 10))
    plt.savefig("script/building.png", format="png")
    print("Histogram saved successfully.", flush=True)
    plt.close()

    plt.figure(figsize=(15, 6))
    plt.grid(True, zorder=-1)
    count1 = [row[1] for row in result1]
    plt.hist(count1, bins=6, edgecolor='k')
    plt.xlabel('Monetory value in Dollars')
    plt.ylabel('customers')
    # plt.xticks(range(0, 200, 50))
    plt.savefig("script/building1.png", format="png")
    print("Histogram saved successfully.", flush=True)
    plt.close()




if __name__ == "__main__":
    freq()