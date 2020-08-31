
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("E:\\datasets\\cicids2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")
dataset.rename(columns={'Label' : 'Answer'}, inplace = True)
print(dataset['Answer'])


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset['Answer']=label_encoder.fit_transform(dataset['Answer'])
dataset.info()

dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

#to drop missing values
dataset.dropna(inplace=True)
nullvalues = dataset.isnull().sum()
nullvalues.head(30)


#stratifying data
#sorting data first so that class wise split can be done
dataset.sort_values(by=['Answer'], inplace=True)

#splitting the data class wose
valuecounts = dataset['Answer'].value_counts()
split_dataset = np.split(dataset, [valuecounts[0]], axis=0)

#Splitting the class-wise splitted data into train and test
trainpartition = 0.7

traintest0 = np.split(split_dataset[0], [int(len(split_dataset[0])*trainpartition)], axis=0)
traintest1 = np.split(split_dataset[1], [int(len(split_dataset[1])*trainpartition)], axis=0)

total_train = np.concatenate((traintest0[0], traintest1[0]))
total_test = np.concatenate((traintest0[1], traintest1[1]))

#Now that we have te partioned dataset. We are removing the target column
#and arranging data for the algorithm to accept
df_total_train = pd.DataFrame(total_train)
X_train = df_total_train.iloc[:, :-1].values
Y_train = df_total_train.iloc[:, 78].values

df_total_test = pd.DataFrame(total_test)
X_test = df_total_test.iloc[:, :-1].values
Y_test = df_total_test.iloc[:, 78].values

#training the model
from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state=0, max_iter=5000, tol=0.001)

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
