from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# Assuming you have your data loaded into a variable named 'X'
df = pd.read_csv("WineQTCali.csv")

X = df.drop("quality", axis=1)
X = X.drop("dataCount", axis=1)

# Step 1: Preprocess the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Perform DBSCAN clustering
eps = 0.5  # epsilon neighborhood radius
min_samples = 5  # minimum number of samples in a neighborhood to consider as a core point
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
clusters = dbscan.fit_predict(X_scaled)

# Step 3: Analyze the clusters
# -1 indicates noise points that were not assigned to any cluster
n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
n_noise = list(clusters).count(-1)

print('Number of clusters:', n_clusters)
print('Number of noise points:', n_noise)