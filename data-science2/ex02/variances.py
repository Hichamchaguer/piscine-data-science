import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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