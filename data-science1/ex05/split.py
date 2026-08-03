import pandas as pd

df = pd.read_csv('Train_knight.csv')

df = df.sample(frac=1, random_state=42)

split = int(len(df) * 0.8)

train = df[:split]
test = df[split:]

train.to_csv('Training_knight.csv', index=False)
test.to_csv('Validation_knight.csv', index=False)

print("files saved sucessfuly")
        