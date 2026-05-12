import pandas as pd


df = pd.read_csv('Train_Knight.csv')

# encoding non-numeric data

df['Knight_encoded'] = df['knight'].map({

        'Jedi': 1,
        'Sith': 0,
})

correlation = df.corr(numeric_only=True)['Knight_encoded']

print(correlation.sort_values(ascending=False))