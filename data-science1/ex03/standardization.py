import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


train = pd.read_csv('../csv/Train_knight.csv')
test = pd.read_csv('../csv/Test_knight.csv')

def standarization(df):
    df = df.copy()
    for column in df.columns:
        if column != 'knight':
            df[column] = (df[column] - df[column].mean()) / df[column].std(ddof=0)
    return df


def scaler(df):

    numerical_columns = [col for col in df.columns if col != 'knight']

    scaler = StandardScaler()

    scaled = scaler.fit_transform(df[numerical_columns])

    scaled_df = pd.DataFrame(scaled, columns=numerical_columns)

    print(scaled_df.head())

def visualize(df):

    standarization(df)
    # sith = df[df['knight'] == 'Jedi']
    # jedi = df[df['knight'] == 'Sith']

    plt.figure(figsize=(10, 5))
    # plt.scatter(jedi['Empowered'], jedi['Stims'], label='Jedi', color='blue', alpha=0.5)
    # plt.scatter(sith['Empowered'], sith['Stims'], label='Sith', color='red', alpha=0.5)
    # plt.xlabel('Empowered')
    # plt.ylabel('Stims')
    # plt.legend()
    # plt.show()
    # plt.close()


    #----------------------------------------------
    #         tresting visualization
    #----------------------------------------------

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
    df = standarization(df)
    print(df.head())
    print("=" * 50)
    print("standardization")
    print("=" * 50)
    scaler(df)
    visualize(df)

if __name__ == '__main__':
    main(train)