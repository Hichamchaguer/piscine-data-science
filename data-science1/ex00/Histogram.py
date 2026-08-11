import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_test = pd.read_csv('../csv/Test_knight.csv')
df_train = pd.read_csv('../csv/Train_knight.csv')

# --------------- Test_Knight -----------------


df_test.hist(figsize=(15, 13), color='green', label='knight')
plt.legend()
plt.tight_layout()
plt.show()
plt.close()

# --------------- Train_Knight -----------------

numeric_columns = df_train.select_dtypes(include=['number']).columns

jedi = df_train[df_train['knight'] == 'Jedi']
sith = df_train[df_train['knight'] == 'Sith']

# Create histogram for Jedi first and capture the axes
axes = jedi.hist(figsize=(15, 13), color='blue', alpha=0.6, bins=20, label='Jedi')

# Then pass the same axes to Sith's histogram
sith.hist(ax=axes, color='red', alpha=0.6, bins=20, label='Sith')

for ax in axes.flatten():
    ax.legend(['Jedi', 'Sith'])

plt.tight_layout()
plt.show()
plt.close()