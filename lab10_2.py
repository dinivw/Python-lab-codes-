#importing necessary packages
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

#loading the irisdata
iris = datasets.load_iris()

#extracting data
iris_data = iris.data
print('Iris data set:','\n',iris_data)

#extracting labels
labels = iris.target
print('Labels of iris data','\n',labels)

#standardize data

#standardized iris data
scaler = StandardScaler().fit(iris_data)
Standard_irisdata = scaler.transform(iris_data)
print(Standard_irisdata)

#standardized test data of plant 1
testdata_plant1 = [[4.6, 3.0, 1.5, 0.2]]
sdtestdata_plant1 = scaler.transform(testdata_plant1)

#standardized data of both plants
testdata_plantboth = [[4.6, 3.0, 1.5, 0.2],[6.2, 3.0,4.1,1.2]]
sdtestdata_plantboth = scaler.transform(testdata_plantboth)


#extracting standardized sepal data
sdsepaldata = Standard_irisdata[:,[0,1]]

#creating the model using standardized sepal data
nn_model = NearestNeighbors(n_neighbors=2).fit(sdsepaldata)

#extracting sepal data from the test data of plant 1
testsepal = sdtestdata_plant1[:,[0,1]]

#distance and indices of nearest neighbours
distance,indices= nn_model.kneighbors(testsepal)

print('For sepal data')
#distances of nearest neighbors
print('Distances are:','\n',distance)
#Indices of nearest neighbors
print('Indices are:','\n',indices)

#labels of nearest neighbours
Predicted_labels = iris['target'][indices]
print('Labels of nearest neighbours:','\n',Predicted_labels)
#species names of nearest neighbours
Predicted_species = iris['target_names'][Predicted_labels]
print('Species names of nearest neighbours','\n',Predicted_species)


#creating the model for predictions using 5 neighbours
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(sdsepaldata,labels)

#extracting the sepal data from both plants
sepal_testdata_plantboth = sdtestdata_plantboth[:,[0,1]]
#predicted probabilites of each species for both plants 1 and 2
print('Predicted probabilities from each species:','\n',knn.predict_proba(sepal_testdata_plantboth))
print('Predicted species labels for each plant:','\n',knn.predict(sepal_testdata_plantboth))

#part2
#petal data

#getting the standard petal data
petaldata = Standard_irisdata[:,[2,3]]

#creating the model
nn_model2 = NearestNeighbors(n_neighbors=2).fit(petaldata)

#testing on the test data of plant1
testpetal = sdtestdata_plant1[:,[2,3]]
distance2,indices2= nn_model2.kneighbors(testpetal)

#distances
print('For petal data')
print('Distances of nearest neighbours:','\n',distance2)
#indices
print('Indices of nearest neighbours','\n',indices2)

#labels of nearest neighbors
Predicted_labels2 = iris['target'][indices2]
print('Labels of nearest neighbours','\n',Predicted_labels2)
#species names of nearest neighbors
Predicted_species2 = iris['target_names'][Predicted_labels2]
print('Species names of nearest neighbors','\n',Predicted_species2)


#creating the model for predictions using 5 neighbours
knn2 = KNeighborsClassifier(n_neighbors=5)
knn2.fit(petaldata,labels)

#extracting petal data from both plants
petal_testdata_plantboth = sdtestdata_plantboth[:,[2,3]]

#predicted probabilities of each species for plants 1,2 and labels
print('Predcited probabilities:','\n',knn2.predict_proba(petal_testdata_plantboth))
print('Predicted species labels for plants:','\n',knn2.predict(petal_testdata_plantboth))

#part3
#for both petal and sepal data

#creating the model
nn_model3 = NearestNeighbors(n_neighbors=2).fit(Standard_irisdata)

#distances and indices of nearest neighbours
distance3,indices3= nn_model3.kneighbors(sdtestdata_plant1)

#distances
print('For all data(sepal and petal):')
print('Distances of nearest neighbors','\n',distance3)
#indices
print('Indices of nearest neighbours','\n',indices3)

#labels of nearest neighbors
Predicted_labels3 = iris['target'][indices3]
print('Labels of nearest neighbors','\n',Predicted_labels3)
#species names of nearest neighbors
Predicted_species3 = iris['target_names'][Predicted_labels3]
print('Species names of nearest neighbors:','\n',Predicted_species3)

#creating the model for predictions using 5 neighbours
knn3 = KNeighborsClassifier(n_neighbors=5)
knn3.fit(Standard_irisdata,labels)

#predicted probabilities of each species for plants 1,2 and labels
print('Probabilites of each species:','\n',knn3.predict_proba(sdtestdata_plantboth))
print('Labels of the two plants','\n',knn3.predict(sdtestdata_plantboth))







