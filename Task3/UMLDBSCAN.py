import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors 
import numpy as np

#Loading in Data file
df = pd.read_csv("WineQTCali.csv")
X = df.drop('quality', axis=1)

xFeature = 'alcohol'
yFeature = 'density'

#identifying the potential value of epsilon
neighbors = NearestNeighbors(n_neighbors=2) 
neighborModel=neighbors.fit(X) 
distances,indices=neighborModel.kneighbors(X)
distances = np.sort(distances, axis = 0) 
distances = distances[:, 1]
plt.rcParams['figure.figsize'] = (5,3)
plt.plot(distances) 
plt.xlabel("Data Objects Sorted by Distance")
plt.ylabel("Average Distance")
plt.title("K-Distance Graph")
plt.grid()
plt.show() 

epsilonArray = np.arange(2, 5, 0.5)
minSamplesArray = np.arange(3, 8,1)

epsilonArray = np.array([3.5, 4.0, 4.5])
minSamplesArray = np.array([4,6,8])

numRows = 3 
numCols = 3

figs, axs = plt.subplots(numRows, numCols, figsize=(30,10))

for row, min_samples in enumerate(minSamplesArray):
    for col, eps in enumerate(epsilonArray):

        dbscanClustering = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
        labels = dbscanClustering.labels_
        

        uniqueLabels = set(labels)

        clusters = dbscanClustering.fit_predict(X)
        n_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)
        n_noise = list(clusters).count(-1)

        print('Number of clusters:', n_clusters)
        print('Number of noise points:', n_noise)

        # Create scatter plot for each cluster
        for label in uniqueLabels:
            clusterMask = labels == label
            if label != -1:
                axs[row][col].scatter(X.loc[clusterMask, xFeature], X.loc[clusterMask, yFeature], label=f'Cluster {label}')
            else:
                pass
                axs[row][col].scatter(X.loc[clusterMask, xFeature], X.loc[clusterMask, yFeature], label='Outliers', color='black', alpha=0.25   )

        axs[row][col].set_xlabel(xFeature) # X-axis label
        axs[row][col].set_ylabel(yFeature) # Y-axis label
        label = f"DBSCAN with {min_samples=} and {eps=}"
        axs[row][col].set_title(label)
        axs[row][col].legend()
   
plt.tight_layout()
plt.show() 