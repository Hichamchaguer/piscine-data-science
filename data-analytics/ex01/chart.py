import pandas as pd
# import matplotlib.pyplot as plt

DB_HOST = "postgres"
DB_NAME = "piscineds"
DB_USER = "hchaguer"
DB_PASSWORD = "mysecretpassword"
DB_PORT = 5432

# connection function 

# def connectToDB():
#     try:
#         cnx = psycopg2.connect(
#             host=DB_HOST,
#             database=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             port=DB_PORT
#         )
#         print("Connection to the database was successful")
#         return cnx
#     except Exception as error:
#         print(f"An error occurred while connecting to the database: {error}")
#         return None


def load():
    try:
        df = pd.read_csv('../../customer/data_2023_jan.csv')

        purchase_col = df[df['event_type'] == 'purchase']

        print(purchase_col.head(20))

    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == '__main__':
    load()
