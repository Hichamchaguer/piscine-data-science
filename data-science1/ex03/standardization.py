import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


train = pd.read_csv('../csv/Train_knight.csv')
test = pd.read_csv('../csv/Test_knight.csv')

def standarization(df):
    for column in df.columns:
        if column != 'knight':
            df[column] = (df[column] - df[column].mean()) / df[column].std()
            print(df[column])


def visualize(df):

    standarization(df)
    sith = df[df['knight'] == 'Jedi']
    jedi = df[df['knight'] == 'Sith']

    plt.figure(figsize=(10, 5))
    plt.scatter(jedi['Empowered'], jedi['Stims'], label='Jedi', color='blue', alpha=0.5)
    plt.scatter(sith['Empowered'], sith['Stims'], label='Sith', color='red', alpha=0.5)
    plt.xlabel('Empowered')
    plt.ylabel('Stims')
    plt.legend()
    plt.show()
    plt.close()

def print_data(df):
    print(df.head())
    print('=' *50)
    df = standarization(df)
    print(df.head())

if __name__ == '__main__':
    visualize(train)
    print_data(train)