import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv('Train_Knight.csv')

def normalization(df):
    for column in df.columns:
        if column != 'knight':
            df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())

def visualize(df):
    normalization(df)
    jedi = df[df['knight'] == 'Jedi']
    sith = df[df['knight'] == 'Sith']

    plt.figure(figsize=(10, 5))
    plt.scatter(jedi['Push'], jedi['Deflection'], label='Jedi', color='blue', alpha=0.5)
    plt.scatter(sith['Push'], sith['Deflection'], label='Sith', color='red', alpha=0.5)
    plt.xlabel('Push')
    plt.ylabel('Deflection')
    plt.legend()
    plt.show()
    plt.close()

if __name__ == '__main__':
    visualize(train)