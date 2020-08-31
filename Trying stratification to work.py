#Summary in this code we have our own code for data stratifiation and also we have trained a logistic regression model with
#an accuracy of 98.8%.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("E:\\datasets\\cicids2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
dataset.rename(columns={'Label' : 'Answer'}, inplace = True)
print(dataset['Answer'])


from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
dataset['Answer']=label_encoder.fit_transform(dataset['Answer'])
dataset.info()

dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

#to drop missing values
dataset.dropna(inplace=True)
nullvalues = dataset.isnull().sum()
nullvalues.head(30)


#stratifying data
#sorting data first so that class wise split can be done
dataset.sort_values(by=['Answer'],inplace=True)

#splitting the data class wose
valuecounts = dataset['Answer'].value_counts()
split_dataset = np.split(dataset, [valuecounts[0]], axis=0)

#Splitting the class-wise splitted data into train and test
trainpartition = 0.7

traintest0 = np.split(split_dataset[0], [int(len(split_dataset[0])*trainpartition)], axis=0)

traintest1 = np.split(split_dataset[1], [int(len(split_dataset[1])*trainpartition)], axis=0)

#testing if works fine
len(split_dataset[0])*trainpartition
len(traintest0[0])
len(split_dataset[0])*(1-trainpartition)
len(traintest0[1])

len(split_dataset[1])*trainpartition
len(traintest1[0])
len(split_dataset[1])*(1-trainpartition)
len(traintest1[1])

#Now we have class wise data splitted into train and test.
#we need to concat the training data of each class to
#get total_train and testing data of each class to get total_test data

total_train = np.concatenate((traintest0[0], traintest1[0]))

total_test = np.concatenate((traintest0[1], traintest1[1]))

#testing
len(total_train)
len(dataset)*0.7

len(total_test)
len(dataset)*0.3

#Now that we have te partioned dataset. We are removing the target column
#and arranging data for the algorithm to accept
df_total_train = pd.DataFrame(total_train)
X_train = df_total_train.iloc[:, :-1].values
Y_train = df_total_train.iloc[:, 78].values

df_total_test = pd.DataFrame(total_test)
X_test = df_total_test.iloc[:, :-1].values
Y_test = df_total_test.iloc[:, 78].values


#testing
df_total_train.shape
X_train.shape
Y_train.shape

df_total_test.shape
X_test.shape
Y_test.shape


#training the model
from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state=0, max_iter=10000, tol=0.001)
Classifier.fit(X_train, Y_train)

Y_predict = Classifier.predict(X_test)

#storing the model
import pickle
filepath = 'C:\\Users\\Rehan Mehmood\\Dropbox\\P1 Research\\Pyhton Codes\Adam\\Logistic Regression\\LogReg maxitr 10k tol 001.sav'
pickle.dump(Classifier, open(filepath, 'wb'))

#Evaluation
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_predict, Y_test)
print(cm)

from sklearn.metrics import accuracy_score
accuracy_score(Y_predict, Y_test)










#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX things to be used later maybe but not useful now



split_dataset[0]
split_dataset[1]

df_split_dataset0 = pd.DataFrame(split_dataset[0])
df_split_dataset0
df_split_dataset0.shape
df_split_dataset0['Answer'].value_counts()

df_split_dataset1 = pd.DataFrame(split_dataset[1])
df_split_dataset1
df_split_dataset1.shape
df_split_dataset1['Answer'].value_counts()


X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, 78].values
y = pd.DataFrame(y)


#training the model
from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state=0, max_iter=2000, tol=0.001)

import time
now = time.time()
Classifier.fit(X_train, Y_train)
now = time.time() - now
now

Y_predict = Classifier.predict(X_test)

#Evaluation
from sklearn.metrics import accuracy_score
accuracy_score(Y_predict, Y_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_predict, Y_test)
print(cm)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, stratify=y)

len(X)*0.7
len(X_train)
len(X)*0.3
len(X_test)


df_Y_train = pd.DataFrame(Y_train)
df_Y_train[0].value_counts()

df_Y_test = pd.DataFrame(Y_test)
df_Y_test[0].value_counts()


dataset['Answer'].value_counts()

print(dataset['Answer'].value_counts())


df_ytrain = pd.DataFrame(Y_train)
print(df_ytrain[0].value_counts())

df_ytest = pd.DataFrame(Y_test)
print(df_ytest[0].value_counts())


from sklearn.model_selection import StratifiedShuffleSplit

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=0)
sss.get_n_splits(X, y)

print(sss)

for train_index, test_index in sss.split(X, y):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = y[train_index], y[test_index]
    print(1234)


X_train.shape
X_test.shape






