from utils.cnx import connect
import numpy as np
from matplotlib import pyplot as plt

# mean, median, min, max, first, second and third quartile


def load():
    try:
        with open("mustache.sql", 'r') as file:
            request = file.read()
        cnx = connect()
        if cnx is None:
            return
        cursor = cnx.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        # price = zip(*data) # price data

        price, event_time = zip(*data)
        count = len(data)
        mean = np.mean(price)
        median = np.median(price)
        min = np.min(price)
        max = np.max(price)
        q1 = np.percentile(price, 25)
        q2 = np.percentile(price, 50)
        q3 = np.percentile(price, 75)

        print(f"Count: {count}", flush=True)
        print(f"Mean: {mean}", flush=True)
        print(f"Median: {median}", flush=True)
        print(f"Min: {min}", flush=True)
        print(f"Max: {max}", flush=True)
        print(f"25%: {q1}", flush=True)
        print(f"50%: {q2}", flush=True)
        print(f"75%: {q3}", flush=True)

        plt.figure(figsize=(6, 6))
        plt.boxplot(price, vert=False, patch_artist=True)
        plt.title("Boxplot of Mustache Prices")
        plt.xlabel("Price")
        plt.ylabel("")
        plt.savefig("script/boxplot.png", format="png")
        plt.close()

        plt.figure(figsize=(6, 6))
        boxprops = dict(facecolor='green', edgecolor='black')
        medianprops = dict(linestyle='-', linewidth=2, color='black')
        plt.boxplot(
            price,
            vert=False,              # horizontal boxplot
            patch_artist=True,       # allow box fill color
            showfliers=False,        # hide outlier dots (matches image)

            boxprops=dict(
                facecolor="#7fbf7f", # green box
                edgecolor="black",
                linewidth=1.5
            ),
            medianprops=dict(
                color="black",
                linewidth=2
            ),
            whiskerprops=dict(
                color="black",
                linewidth=1.5
            ),
            capprops=dict(
                color="black",
                linewidth=1.5
            )
        )
        plt.yticks([])
        plt.xlabel("Price")
        plt.title("Interquartile range (IQR)")
        plt.savefig("script/boxplot1.png", format="png")
        plt.close()


    except Exception as error:
        print(f"An error occurred while loading data: {error}", flush=True)


def  average_basket_price():
    try:
        with open("mustache2.sql", 'r') as file:
            request = file.read()
        cnx = connect()
        if cnx is None:
            return

        print("Executing SQL query for average basket price...", flush=True)
        cursor = cnx.cursor()
        cursor.execute(request)
        data = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()

        user_id, average = zip(*data)
        plt.figure(figsize=(10, 6))
        plt.boxplot(average, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                flierprops=dict(marker='D', markersize=8, markerfacecolor='lightgray', markeredgecolor='none'),
                patch_artist=True, whis=0.2)
        plt.xlabel("User ID")
        plt.ylabel("Average Basket Price")
        plt.title("Average Basket Price per User")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("script/average_basket_price.png", format="png")
        plt.close()

    except Exception as error:
         print(f"An error occurred while loading data: {error}", flush=True)

if __name__ == "__main__":
    load()
    average_basket_price()