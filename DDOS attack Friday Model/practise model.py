import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("E:\\datasets\\cicids2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
#renaming column Label to Answer for ease
dataset.columns
dataset.rename(columns={'Label' : 'Answer'}, inplace = True)
print(dataset['Answer'])

dataset['Flow Bytes/s'] = dataset['Flow Bytes/s'].astype(int, copy = True)
dataset.info()

dataset[' Flow Packets/s'] = dataset[' Flow Packets/s'].astype(int, copy = True)
dataset.info()


from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
dataset['Answer']=label_encoder.fit_transform(dataset['Answer'])
dataset.info()

nullvalues = dataset.isnull().sum()
nullvalues.head(30)

dataset.dropna(inplace=True)
nullvalues = dataset.isnull().sum()
nullvalues.head(30)


X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,78].values


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3, stratify=Y)


import pickle

# load the model from disk
loaded_model = pickle.load(open('E:\\Python Models\\LogisticRegression_Model1.sav', 'rb'))

Y_predict = loaded_model.predict(X_test)


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_predict, Y_test)
print(cm)


result = loaded_model.score(X_test, Y_test)
print(result)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_predict,Y_test)
print(cm)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx




import csv

with open(r'names.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    rowcontents = [1, 2, 3, 4]
    writer.writerow(rowcontents)


rowcontents = [1, 2, 3]
rowcontents.append(4)
rowcontents = [rowcontents, 4]
print(rowcontents)


df1 = pd.read_csv("E:\\datasets\\cicids2017\\MachineLearningCVE\\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
df2 = pd.read_csv("C:\\Users\\Rehan Mehmood\\Desktop\\CICFlowMeter-4.0\\bin\\data\\daily\\2020-03-08_Flow.csv")


intersection = set(df1.columns).intersection(set(df2.columns))
difference  = set(df1.columns).difference(set(df2.columns))
len(intersection)
len(difference)


df1.columns
df2.columns


df1.shape
df2.shape


df1.info()
df2.info()

df1.drop(columns = df1.iloc[:,[0,1]], axis = 1, inplace = True)

#For iterating rows 1 by 1

for i in range(len(df2)):
    Xrow = df2.iloc[[i],:].values
    print(i)
    Y_predict = loaded_model.predict(Xrow)
    if Y_predict == 1:
        print("ALERTT!!!")



    len(Y_predict)
    df2.shape
    X_test.shape
    Xrow.shape
    dataset.head(2)




from sklearn.linear_model import LogisticRegression
Classifier =LogisticRegression(random_state=0, max_iter = 10000)
Classifier.fit(X_train,Y_train)


Y_predict=Classifier.predict(X_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_predict,Y_test)
print(cm)


from sklearn.metrics import accuracy_score
accuracy_score(Y_predict,Y_test)


import statsmodels.api as sm
mode = sm.OLS(Y,X)
fii = mode.fit()
print(fii.summary())



#dataset[:] = dataset[:].astype(float)


print(nullvalues)



from collections import Counter
dataset.hist(column='Answer')
Counter(dataset[:])


dataset.columns
dataset['Flow Bytes/s'] = dataset['Flow Bytes/s'].apply(lambda x: np.complex(x))
dataset.info()

dataset[' Flow Packets/s'] = dataset[' Flow Packets/s'].apply(lambda x: np.complex(x))
dataset.info()


#To remove missing and infinite valeus in dataset

infvaluearray = np.isfinite(dataset).sum()
infvaluearray2 = np.isfinite(dataset).all()

nullvaluearray = np.isnan(dataset).any()

nullvalues = dataset.isnull().sum()
nullvalues.head(30)


from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(dataset[['Flow Bytes/s']])
dataset['Flow Bytes/s'] = imp.transform(dataset[['Flow Bytes/s']])

nullvalues = dataset.isnull().sum()
nullvalues.head(30)

imp = imp.fit(dataset[['Flow Bytes/s']])
dataset['Flow Packets/s'] = imp.transform(dataset[['Flow Packets/s']])

nullvalues = dataset.isnull().sum()
nullvalues.head(30)

nullvaluearray  = np.isnan(dataset).any()
