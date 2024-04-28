import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load data using pandas
data = pd.read_csv('WineQTCali.csv')

#X = data[["density", "chlorides"]]
X = data.drop("quality", axis=1)

silhouetteAvgDict = {}

nClustersArray = []

for i in range(2,8,1):
    nClustersArray.append(i)

print(nClustersArray)

numCols = 3
numRows = 2

figs, axs = plt.subplots(numRows, numCols, figsize=(30,10))

xFeature = 'alcohol'
yFeature = 'density'

# Apply K-means clustering
for i, nClusters in enumerate(nClustersArray):

    kmeans = KMeans(n_clusters=nClusters)
    kmeans.fit(X)
    yKmeans = kmeans.predict(X)
    centers = kmeans.cluster_centers_

    silhouetteAvg = silhouette_score(X, yKmeans)
    silhouetteAvgDict[nClusters] = silhouetteAvg
        
    row = i // numCols
    col = i % numCols
                
    axs[row][col].scatter(X[xFeature], X[yFeature], c=yKmeans, s=50, cmap='viridis')
    axs[row][col].set_xlabel(xFeature)
    axs[row][col].set_ylabel(yFeature)
    label = "K-means Clustering with K-value: " + str(nClusters)
    axs[row][col].set_title(label)


    for clusterLabel in range(nClusters):
        cluster_mean = X.iloc[yKmeans == clusterLabel].mean()
        axs[row][col].scatter(cluster_mean[xFeature], cluster_mean[yFeature], c='red', marker='o', s=200, label=f'Centroid {clusterLabel+1}')

    unique_labels = np.unique(yKmeans)
    legend_handles = []
    for label_value in unique_labels:
        color = plt.cm.viridis(label_value / nClusters)
        legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label_value))
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor="red", markersize=10, label='Centroids'))
    axs[row][col].legend(handles=legend_handles, title='Cluster Labels', loc='upper right')

              

print(silhouetteAvgDict)

plt.tight_layout()
plt.subplots_adjust(wspace=0.4, hspace=0.4)
handles, labels = axs[0][0].get_legend_handles_labels()
figs.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=5)
figs.show()  
plt.show()

df2 = pd.DataFrame(list(silhouetteAvgDict.items()), columns=['clusters', 'silScore'])

df2.to_csv("silhouetteScores.csv", index=False)

fig, ax = plt.subplots()
ax.plot(df2['clusters'],df2['silScore'])
ax.set_xlabel('Cluster Count')
ax.set_ylabel('Silhouette Score')
ax.set_title("Silhouette Score vs Cluster Count")
ax.grid()

plt.show()