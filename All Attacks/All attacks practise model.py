import numpy as np
import pandas as pd


ddosdataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
portscandataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv")
infiltrationdataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv")
webattackdataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv")

ddosdataset.columns = portscandataset.columns

intersection = set(ddosdataset.columns).intersection(set(portscandataset.columns))
difference = set(ddosdataset.columns).difference(set(portscandataset.columns))
len(intersection)
len(difference)

difference = set(ddosdataset.columns).difference(set(infiltrationdataset.columns))
difference
difference = set(ddosdataset.columns).difference(set(webattackdataset.columns))
difference
difference = set(ddosdataset.columns).difference(set(portscandataset.columns))
difference

complete_dataset = pd.concat([ddosdataset, portscandataset])
len(ddosdataset) + len(portscandataset)
len(complete_dataset)

complete_dataset = pd.concat([complete_dataset, infiltrationdataset])
len(ddosdataset) + len(portscandataset) + len(infiltrationdataset)
len(complete_dataset)

complete_dataset = pd.concat([complete_dataset, webattackdataset])
len(ddosdataset) + len(portscandataset) + len(infiltrationdataset) +len(webattackdataset)
len(complete_dataset)

complete_dataset[' Label'].value_counts()

len(infiltrationdataset)
infiltrationdataset[' Label'].value_counts()

len(webattackdataset)
webattackdataset[' Label'].value_counts()



dataset.rename(columns={' Label': 'Answer'}, inplace=True)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset['Answer'] = label_encoder.fit_transform(dataset['Answer'])

dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

dataset.dropna(inplace=True)

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 78].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, stratify=Y)

from sklearn.linear_model import LogisticRegression
Classifier = LogisticRegression(random_state=0, max_iter=9000, tol=0.001)

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

from sklearn.metrics import classification_report
print('\nClasification report:\n', classification_report(Y_test, Y_predict))


