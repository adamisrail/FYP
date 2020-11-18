import numpy as np
import pandas as pd
import smtplib

sender_address = 'adamisrail@gmail.com'
sender_pass = input(str("Enter your password"))
receiver_address = 'adamisrail@gmail.com'
mail_content = "Completed"

ddospath = r"F:\Adam\Datasets\CICIDS Dataset 2017\MachineLearningCVE\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
portscanpath = r"F:\Adam\Datasets\CICIDS Dataset 2017\MachineLearningCVE\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"


ddosdataset = pd.read_csv(ddospath)
portscandataset = pd.read_csv(portscanpath)

ddosdataset.info()
portscandataset.info()

intersection = set(ddosdataset.columns).intersection(set(portscandataset.columns))
difference = set(ddosdataset.columns).difference(set(portscandataset.columns))
len(intersection)
len(difference)


dataset = pd.concat([ddosdataset, portscandataset])
dataset.info()

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset.rename(columns={' Label': 'Answer'}, inplace=True)
dataset['Answer'] = label_encoder.fit_transform(dataset['Answer'])
dataset['Answer'].value_counts()

ddosdataset[' Label'].value_counts()


dataset.replace([np.inf, -np.inf], np.nan, inplace=True)
dataset.dropna(inplace=True)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 78].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, stratify=y_train)  # 0.25 x 0.8 = 0.2


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=3500, hidden_layer_sizes=(78,), max_iter=300, random_state=1)


import time
#clf.fit and email when done
starttime = time.time()
clf.fit(X_train, y_train)
totaltime = time.time() - starttime
print(totaltime)

mail_content = str(totaltime)
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
session.sendmail(sender_address, receiver_address, mail_content)
session.quit()
print("Mail Sent")


# clf.n_layers_
# clf.n_outputs_
# len(clf.coefs_)
# len(clf.coefs_[0])



Y_predict = clf.predict(X_test)
Y_predict_val = clf.predict(X_val)


from sklearn.metrics import accuracy_score
accuracy_score(Y_predict, y_test)
accuracy_score(Y_predict_val, y_val)



from sklearn.metrics import classification_report
print('\nClasification report:\n', classification_report(y_test, Y_predict))

print('\nClasification report:\n', classification_report(y_val, Y_predict_val))
