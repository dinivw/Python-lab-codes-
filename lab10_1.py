#importing necessary packages
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#import iris dataset
iris = pd.read_csv('iris.csv')

iris_data = iris[['sepal.length','sepal.width','petal.length','petal.width']]
print(iris_data)

#preprocessing the data
scaler = StandardScaler().fit(iris_data)
sd_iris_data = scaler.transform(iris_data)

#getting the sepal data
sepaldata = sd_iris_data[:,[0,1]]

#Assigning the K value
kmeans_sepal = KMeans(n_clusters = 3).fit(sepaldata)

#Getting the centroids
centroids_sepal = kmeans_sepal.cluster_centers_
print('Centroids of sepal data:','\n',centroids_sepal)

#labels of the data
labels = kmeans_sepal.labels_


testdata_plantboth= [[4.6, 3.0, 1.5, 0.2],[6.2, 3.0,4.1,1.2]]
sdtestdata_plantboth = scaler.transform(testdata_plantboth)

#two unknown species-sepal data
new_data_sepal = sdtestdata_plantboth[:,[0,1]]


#predicting values using sepal data
predicted_values_sepal = kmeans_sepal.predict(new_data_sepal)
print('Predicted labels of unknown species when sepal data is used:','\n',predicted_values_sepal)

#plotting the sepal measurement data

plt.scatter(sepaldata[:,0],sepaldata[:,1],c=labels.astype(float),s=50,alpha=0.5)
plt.scatter(centroids_sepal[:,0],centroids_sepal[:,1],c='red',s=100)
plt.scatter(new_data_sepal[:,0],new_data_sepal[:,1],c='green',s=50)
#annotating labels
for i,txt in enumerate(labels):
    plt.annotate(txt,(sepaldata[:,0][i], sepaldata[:,1][i]))
species = np.array(iris['v_short'])
print(species)
#annotating species types
for i,txt in enumerate(species):
    plt.annotate(txt,(sepaldata[:,0][i], sepaldata[:,1][i]),xytext = (-20,20),textcoords = 'offset points',
                 arrowprops = dict(arrowstyle='->',connectionstyle ='arc3,rad=0',color='orange'),color ='brown')
#annotating predicted labels for new data
for i,txt in enumerate(predicted_values_sepal):
    plt.annotate(txt,(new_data_sepal[:,0][i],new_data_sepal[:,1][i]))
plt.title('Sepal measurement data')
plt.savefig('Sepal_measurement.jpg')
plt.show()

#getting the petal data
petaldata = sd_iris_data[:,[2,3]]


#Assigning the K value
kmeans_petal = KMeans(n_clusters = 3).fit(petaldata)

#Getting the centroids
centroids_petal = kmeans_petal.cluster_centers_

#getting the labels
labels_petal = kmeans_petal.labels_

#two unknown species-petal data
new_data_petal = sdtestdata_plantboth[:,[2,3]]


#predicting values using petal data
predicted_values_petal = kmeans_petal.predict(new_data_petal)
print('Predicted labels of unknown species when petal data is used:','\n',predicted_values_petal)

#plotting the petal measurement data
plt.scatter(petaldata[:,0 ],petaldata[:,1],c=labels.astype(float),s=50,alpha=0.5)
plt.scatter(centroids_petal[:,0],centroids_petal[:,1],c='red',s=100)
plt.scatter(new_data_petal[:,0],new_data_petal[:,1],c='green',s=50)
#annotating labels
for i,txt in enumerate(labels_petal):
    plt.annotate(txt,(petaldata[:,0][i], petaldata[:,1][i]) )
#annotating species types
for i,txt in enumerate(species):
    plt.annotate(txt,(petaldata[:,0][i], petaldata[:,1][i]) ,xytext = (-20,20),textcoords = 'offset points',
                 arrowprops = dict(arrowstyle='->',connectionstyle ='arc3,rad=0',color='orange'),color ='brown')
#annotating predicted labels for petal data
for i,txt in enumerate(predicted_values_petal):
    plt.annotate(txt,(new_data_petal[:,0][i],new_data_petal[:,1][i]))
plt.title('Petal measurement data')
plt.savefig('petal_measurement.jpg')
plt.show()