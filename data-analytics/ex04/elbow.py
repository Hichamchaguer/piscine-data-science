from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from utils.cnx import connect


def clustring():

    with open('elbow.sql', 'r') as f:
        data = f.read()

    cnx = connect()
    if cnx is None:
        print("Failed to connect to the database.", flush=True)
        return
    cursor  = cnx.cursor()
    cursor.execute(data)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()

    values = [row[1] for row in data]
    x = [[value] for value in values]
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    wcss = []

    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10).fit(x_scaled)
        wcss.append(kmeans.inertia_)

    print("WCSS values for k=1 to 9:", wcss, flush=True)
    plt.plot(range(1, 10), wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of clusters')
    plt.savefig('script/elbow_plot.png', format='png')
    plt.close()
    print("Elbow plot saved as 'script/elbow_plot.png'", flush=True)


if __name__ == "__main__":
    clustring()