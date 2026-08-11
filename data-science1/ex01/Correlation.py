import pandas as pd


df = pd.read_csv('../csv/Train_knight.csv')

# encoding non-numeric data

df['Knight_encoded'] = df['knight'].map({

        'Jedi': 1,
        'Sith': 0,
})

correlation = df.corr(numeric_only=True)['Knight_encoded'] # compute correlation with the encoded 'knight' column
 
print(correlation.sort_values(ascending=False))  