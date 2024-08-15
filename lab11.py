import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix,classification_report


#loading the dataset
iris = pd.read_csv('iris.csv')

#measurement data
iris_d = iris[['sepal.length','sepal.width','petal.length','petal.width']]

iris_data = np.array(iris_d)
print(iris_data)

#class labels
species = iris['v_short']

#converting class labels to numerical values
label_encoder = preprocessing.LabelEncoder()
species = label_encoder.fit_transform(species)
print(species)

#split the dataset in to train and test

X = iris_data
y = species

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)

#preprocessing of training and testing data

#training data
scaler = StandardScaler()
scaler.fit(X_train)
X_trainS = scaler.transform(X_train)

#testing data
X_testS = scaler.transform(X_test)


#training the model
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter=1000)
mlp.fit(X_trainS,y_train)

#predicitng the speceis labels of test data
predictions = mlp.predict(X_testS)
print('Predicted labels for test data using model 1:','\n',predictions)

#confusion matrix
print('Confusion matrix for model 1:','\n',confusion_matrix(y_test,predictions))
print('Classification report for model 1:','\n',classification_report(y_test,predictions))

#data of three plants
plant1 = [[5.9,3.0,7.0,5.0]]
plant2 = [[4.6,3.0,1.5,0.2]]
plant3 = [[6.2, 3.0,4.1,1.2]]

#standardize plant values
plant1S = scaler.transform(plant1)
plant2S = scaler.transform(plant2)
plant3S = scaler.transform(plant3)

#predicting plant 1
predictions_plant1 = mlp.predict(plant1S)
print('Predictions for plant 1:','\n',predictions_plant1)

#predicting plant 2
predictions_plant2 = mlp.predict(plant2S)
print('Predictions for plant 2:','\n',predictions_plant2)

#predicting plant 3
predictions_plant3 = mlp.predict(plant3S)
print('Predictions for plant 3:','\n',predictions_plant3)

#creating model using 2 as number of neurons

mlp2 = MLPClassifier(hidden_layer_sizes=(2,2,2), max_iter=1000)
mlp2.fit(X_trainS,y_train)

#predicitng the speceis labels of test data
predictions2 = mlp2.predict(X_testS)


#confusion matrix
print('Confusion matrix for model 2:','\n',confusion_matrix(y_test,predictions2))
print('Classification report for model 2:','\n',classification_report(y_test,predictions2))








