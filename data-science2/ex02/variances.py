import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('../csv/Train_knight.csv')
X = df.drop(columns=['knight'])

# Calculate variance for each skill
variances = X.var().sort_values(ascending=False)

print("Variance of each skill (sorted):")
# print(variances)

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA()
pca.fit(X_scaled)

# Explained variance (this matches your output)
explained_variance = pca.explained_variance_ratio_ * 100

# Cumulative
cumulative = explained_variance.cumsum()

print("Variance (Percentage):")
print(explained_variance)

print("\nCumulative Variance (Percentage):")
print(cumulative)

cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# Find number of components for 90%
n_components = np.argmax(cumulative_variance >= 0.90) + 1

# Plot
plt.figure()
plt.plot(range(1, len(cumulative_variance)+1), cumulative_variance * 100, marker='o')
# 90% threshold line
plt.axhline(y=90, linestyle='--')

# Vertical line for chosen components
plt.axvline(x=n_components, linestyle='--')

plt.xlabel("Number of Components")
plt.ylabel("Explained Variance (%)")
plt.title("Elbow Plot (PCA)")

plt.show()