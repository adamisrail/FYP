import numpy as np
import pandas as pd

import smtplib

sender_address = 'adamisrail@gmail.com'
sender_pass = input(str("Enter your password"))
receiver_address = 'adamisrail@gmail.com'
mail_content = "Completed"


dataset = pd.read_csv("F:\\Adam\\Datasets\\CICIDS Dataset 2017\\MachineLearningCVE\\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv")

dataset[" Label"].value_counts()

dataset.rename(columns={' Label': 'Answer'}, inplace=True)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset['Answer'] = label_encoder.fit_transform(dataset['Answer'])
dataset['Answer'].value_counts()

dataset.replace([np.inf, -np.inf], np.nan, inplace=True)

dataset.dropna(inplace=True)

dataset['Answer'].value_counts()

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 78].values

from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression

StratifiedKFold = model_selection.StratifiedKFold(n_splits=5)
#kfold = model_selection.KFold(n_splits=5)
Classifier = LogisticRegression(random_state=0, max_iter=1000, tol=0.001)

model = AdaBoostClassifier(n_estimators=50, random_state=0, base_estimator=Classifier)
# results = model_selection.cross_val_score(model, X, Y, cv=StratifiedKFold)
# print(results.mean())

import time


starttime = time.time()

Y_predict = model_selection.cross_val_predict(model, X, Y, cv=StratifiedKFold)

totaltime = time.time() - starttime

mail_content = "Completed"
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
session.sendmail(sender_address, receiver_address, mail_content)
session.quit()
print("Mail Sent")



Y_predict
len(Y_predict)
len(Y)


#Evaluation
from sklearn.metrics import accuracy_score
accuracy_score(Y, Y_predict)

from sklearn.metrics import recall_score
recall_score(Y, Y_predict)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y, Y_predict)
cm

tn, fp, fn, tp = confusion_matrix(Y, Y_predict).ravel()
tn
fp
fn
tp


from sklearn.metrics import classification_report
print('\nClasification report:\n', classification_report(Y, Y_predict))



