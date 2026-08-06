import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

def compute_vif(X):
    vif_data = pd.DataFrame()
    vif_data["feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data


def main(X):
    X_current = X.copy()

    while True:
        vif = compute_vif(X_current)
        max_vif = vif["VIF"].max()
        
        if max_vif < 5:
            break
        
        # remove feature with highest VIF
        remove_feature = vif.sort_values("VIF", ascending=False)["feature"].iloc[0]
        print(f"Removing: {remove_feature} : {max_vif:.2f}")
        
        X_current = X_current.drop(columns=[remove_feature])

    return X_current


if __name__ == "__main__":
    df = pd.read_csv('../csv/Train_knight.csv')
    X = df.drop(columns=['knight'])
    df = main(X)
    print('='*50)
    vif = compute_vif(df)
    vif["Tolerance"] = 1 / vif["VIF"]
    print(vif)