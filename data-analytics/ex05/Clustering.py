from utils.cnx import connect
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
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

        X = df[['frequency', 'monetary', 'recency']]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        kmeans = KMeans(n_clusters=5, random_state=42)
        df['cluster'] = kmeans.fit_predict(X_scaled)
        summary = df.groupby('cluster')[['frequency', 'monetary', 'recency']].mean()

        clusters_names = {
            0: 'Inactive',
            1: 'Silver',
            2: 'Gold',
            3: 'New',
            4: 'Platinum'
        }

        df['customers_groups'] = df['cluster'].map(clusters_names)
        counts = df['customers_groups'].value_counts().sort_values()
        colors = ['#d6d6d6', '#f5f200', 'red', '#f2eaa5', 'green']

        plt.figure(figsize=(10,6))
        plt.barh(counts.index, counts.values, color=colors)
        plt.xlabel('Number of customers')
        plt.title('customers segmentation')
        plt.savefig('script/customer_segment.png', format='png')
        print('segmentation saved as scriptcustomer_segment.png', flush=True)
        plt.close()

        # Bubble chart
        plt.figure(figsize=(10,6))
        colors = {
            "Inactive": "green",
            "Silver": "blue",
            "Gold": "orange",
            "New": "purple",
            "Platinum": "red"
        }
        segment_groups = df.groupby('customers_groups').agg({
            'recency': 'mean',
            'frequency': 'mean',
            'monetary': 'mean'
        }).reset_index()

        print(segment_groups, flush=True)
        for _, row in segment_groups.iterrows():
            plt.scatter(
                row["recency"],
                row["frequency"],
                s=row['monetary'] * 3,
                alpha=0.6,
                c=colors[row["customers_groups"]],
                label=row["customers_groups"]
            )
            plt.text(
                row["recency"],
                row["frequency"],
                f"Average {row['customers_groups']}: {row['monetary']:.1f}\n",
                fontsize=9
            )
        plt.xlabel("Median Recency (Months)")
        plt.ylabel("Median Frequency")
        plt.title("Customer Segmentation Bubble Chart")
        plt.savefig('script/bubble_chart.png', format='png')
        print('saving bubble chart.png', flush=True)
        plt.close()

    except Exception as e:
        print(f"An error occurred: {e}", flush=True)


if __name__ == "__main__":
    clustering()