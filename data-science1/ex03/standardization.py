import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


train = pd.read_csv('Train_Knight.csv')
test = pd.read_csv('Test_Knight.csv')

def standarization(df):
    for column in df.columns:
        if column != 'knight':
            df[column] = (df[column] - df[column].mean()) / df[column].std()

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


if __name__ == '__main__':
    visualize(train)