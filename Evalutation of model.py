import pandas as pd
import csv
import numpy as np

path = 'C:\\Users\\Rehan Mehmood\\Desktop\\p2 project work\\Data\\a.csv'
offloadfilepath = 'C:\\Users\\Rehan Mehmood\\Desktop\\p2 project work\\Data\\Evalutation file.csv'
attackerIP = '192.168.1.105'

try:
    dataset = pd.read_csv(path)


except:
    print("File not found for evaluation")
    exit()

totalflows = len(dataset)
totalp=0
tp=0
fp=0
totaln=0
tn=0
fn=0

Xrow = dataset.iloc[:, 1].values
for i in range(len(dataset)):
    #for ddos flow
    if dataset.iloc[:, 1].values[i] == attackerIP:
        #count for ddos flow
        totalp = totalp + 1
        if dataset.iloc[:, 83].values[i] == 1:
            #count for flows that are ddos and predicted 1 (right)
            tp = tp + 1
        else:
            fn = fn + 1

    #for normal flows
    elif dataset.iloc[:, 1].values[i] != attackerIP:
        # count for normal flow
        totaln = totaln + 1
        if dataset.iloc[:, 83].values[i] == 0:
            # count for flows that are ddos and predicted 0 (right)
            tn = tn + 1
        else:
            fp = fp + 1

Posprecision = tp/(tp+fp)
Negprecision = tn/(tn+fn)

precall = tp/(tp+fn)
nrecall = tn/(tn+fp)

Accuracy = (tp + tn)/totalflows
Accuracyddos = tp/totalp
Accuracynormal = tn/totaln

print("Total flow count captured = " + str(len(dataset)))

print("DDOS Flows = "+str(totalp))
print("Normal Flows = "+str(totaln))


print("True Positives = "+str(tp))
print("False Positives = "+str(fp))
print("True Negatives = "+str(tn))
print("False Negatives = "+str(fn))


print("Accuracy = "+str(Accuracy))
print("Accuracy DDOS = "+str(Accuracyddos))
print("Accuracy Normal = "+str(Accuracynormal))


print("Precision Positive class = "+str(Posprecision))
print("Precision Negative class = "+str(Negprecision))

print("Recall Positive class = "+str(precall))
print("Recall Negative class = "+str(nrecall))

#for passing complete row content to csv writer rather than the dataset where the columns 1,2,3,4 etc have been removed

totalflowswrite = ["Total Flows", totalflows]
totalpwrite = ["Total DDOS Flows", totalp]
totalnwrite = ["Total Normal Flows", totaln]


tpwrite = ["True Positives", tp]
fpwrite = ["False Positives", fp]


tnwrite = ["True Negatives", tn]
fnwrite = ["False Negatives", fn]


Accuracywrite = ["Accuracy", Accuracy]
Accuracyddoswrite = ["Accuracy DDOS", Accuracyddos]
Accuracynormalwrite = ["Accuracy Normal", Accuracynormal]


posprecisionwrite = ["Positive Class Precision", Posprecision]
negprecisionwrite = ["Negative Class Precision", Negprecision]


precallwrite = ["Positive Class Recall", precall]
nrecallwrite = ["Negative Class Recall", nrecall]




#Writing a CSV file for offline Analysis
with open(offloadfilepath, 'a', newline='') as offlinefile:
    writer = csv.writer(offlinefile)
    writer.writerow("")
    writer.writerow(totalflowswrite)
    writer.writerow(totalpwrite)
    writer.writerow(totalnwrite)

    writer.writerow(tpwrite)
    writer.writerow(fpwrite)
    writer.writerow(tnwrite)
    writer.writerow(fnwrite)

    writer.writerow(Accuracywrite)
    writer.writerow(Accuracyddoswrite)
    writer.writerow(Accuracynormalwrite)

    writer.writerow(posprecisionwrite)
    writer.writerow(negprecisionwrite)

    writer.writerow(precallwrite)
    writer.writerow(nrecallwrite)
