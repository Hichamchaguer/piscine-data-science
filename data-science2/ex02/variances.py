import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def var(df):
    if 'knight' in df.columns:
        X = df.drop(columns=['knight'])
        x = StandardScaler().fit_transform(X)
    else:
        x = StandardScaler().fit_transform(df)

    pca = PCA()
    pca.fit(x)
    return pca

def variance(df):
    return df.var().sort_values(ascending=False)


if __name__ == '__main__':
    df = pd.read_csv('../csv/Test_knight.csv')
    pca = var(df)
    print(pca.explained_variance_ratio_)