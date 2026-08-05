import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlation(df):
    df['knight'] = df['knight'].map({

        'Jedi':0,
        'Sith':1,
    })

    # df = df.drop(columns=['knight'])
    correlation = df.corr(numeric_only=True)
    return correlation


def heatmap(corr):
    plt.figure(figsize=(12,10))
    print(plt.colormaps())
    img = plt.imshow(corr, cmap="rocket", vmin=-0.6, vmax=1) # rocket (dark blue - red - orange - white)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar(img, label='correlation')
    plt.show()
    plt.close()




def main():
    df = pd.read_csv('../csv/Train_knight.csv')
    corr = correlation(df)
    heatmap(corr)

if __name__ == '__main__':
    main()

