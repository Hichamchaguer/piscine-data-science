import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


train = pd.read_csv('../csv/Train_knight.csv')
test = pd.read_csv('../csv/Test_knight.csv')

def normalization(df):
    df = df.copy()
    for column in df.columns:
        if column != 'knight':
            df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df


def scaler(df):
    numerical_columns = [col for col in df.columns if col != 'knight']

    scaler = MinMaxScaler()

    scaled = scaler.fit_transform(df[numerical_columns])

    scaled_df = pd.DataFrame(scaled, columns=numerical_columns)

    print(scaled_df.head())


def visualize(df):
    normalization(df)
    # jedi = df[df['knight'] == 'Jedi']
    # sith = df[df['knight'] == 'Sith']

    plt.figure(figsize=(10, 5))
    # plt.scatter(jedi['Push'], jedi['Deflection'], label='Jedi', color='blue', alpha=0.5)
    # plt.scatter(sith['Push'], sith['Deflection'], label='Sith', color='red', alpha=0.5)
    # plt.xlabel('Push')
    # plt.ylabel('Deflection')
    # plt.legend()
    # plt.show()
    # plt.close()


    # print("--------------------------------------------------")
    # print("testing visualization")
    # print("--------------------------------------------------")

    plt.scatter(test['Empowered'], test['Stims'], 
                label='knights', color='green', alpha=0.5)
    plt.xlabel('Empowered')
    plt.ylabel('Stims')
    plt.title('3. Empowered vs Stims (Test Data)')
    plt.legend()
    plt.grid(True, alpha=0.9)
    plt.show()
    plt.close()


def main(df):
    df = normalization(df)
    print(df.head())
    print("=" * 50)
    print("normalization")
    print("=" * 50)
    scaler(df)
    visualize(df)

if __name__ == '__main__':
    main(train)