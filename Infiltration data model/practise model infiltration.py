import numpy as np
import pandas as pd


dataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv")


dataset[" Label"].value_counts()


dataset[' Label'].value_counts()
dataset.rename(columns={' Label': 'Answer'}, inplace=True)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset['Answer'] = label_encoder.fit_transform(dataset['Answer'])
dataset['Answer'].value_counts()


nullvalues = dataset.isnull().sum()
nullvalues.head(30)

dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

nullvalues = dataset.isnull().sum()
nullvalues.head(30)

dataset.dropna(inplace=True)
nullvalues = dataset.isnull().sum()

dataset['Answer'].value_counts()

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 78].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y)

Y_test[0].value_counts
len(dataset)*0.7
len(X_train)
len(dataset)*0.3
len(X_test)

df_Y_test = pd.DataFrame(Y_test)
df_Y_test[0].value_counts()

#training the model
from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state=0, max_iter=1000, tol=0.001)

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
cm = confusion_matrix(Y_test, Y_predict)
cm

tn, fp, fn, tp = confusion_matrix(Y_test, Y_predict).ravel()
tn
fp
fn
tp


from sklearn.metrics import classification_report
print('\nClasification report:\n', classification_report(Y_test, Y_predict))










#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

dataset.describe()

intersection = set(ddosdataset.columns).intersection(set(portscandataset.columns))
difference = set(ddosdataset.columns).difference(set(portscandataset.columns))

len(intersection)
len(difference)

portscandataset.describe()

len(ddosdataset)+len(portscandataset)
len(dataset)

dataset.columns
dataset.head()

dataset.info()