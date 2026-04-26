from utils.cnx import connect
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd



def clustering():

    try:
        with open('Clustering.sql', 'r') as f:
            data = f.read()

        cnx = connect()
        if cnx is None:
            print("Failed to connect to the database.", flush=True)
            return
        cursor  = cnx.cursor()
        cursor.execute(data)
        data = cursor.fetchall()
        cursor.close()

        df = pd.DataFrame(data, columns=['user_id', 'frequency', 'monetary', 'recency'])
        cnx.close()
        print(df.head(), flush=True)
    except Exception as e:
        print(f"An error occurred: {e}", flush=True)


if __name__ == "__main__":
    clustering()