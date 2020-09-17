
import pandas as pd
import numpy as np

import pickle
import csv
import tkinter as tk

from tkinter import *

import threading






def startevaluating(attackerIP, inputfile, outputfile):
    print(attackerIP)

    # load the model from disk
    path = inputfile
    #the output path file has been set to be the folder from where the input file has been received
    offlinefilepath = outputfile
    #attackerIP = "192.168.18.82"

    loaded_model = pickle.load(open(r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\LogisticRegression_Model1.sav', 'rb'))
    #data recieved from cicflowmeter is this file
    #path = r"D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\2020-03-15_Flow.csv"
    #path = r"F:\Adam\CICflowmeter Current\CICFlowMeter-master\data\daily\2020-08-31_Flow.csv"

    offlinefilepath = r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\outputfile.csv'

    totalflows = 1
    totalp = 1
    tp = 1
    fp = 1
    totaln = 1
    tn = 1
    fn = 1

    x = 0
    y = 1

    startscanafteriprecievedbtn["state"] = "disabled"
    quitevaluatebtn["state"] = "normal"

    while(True):
        if numberx == 1:
            setnumber(0)
            print("Break while")
            break

        try:

            dataset = pd.read_csv(path, skiprows=x)
            complete_dataset = pd.read_csv(path, skiprows=x)

            x = x + len(dataset)


        except:

            print("File not found or bieng accessed or some error "
                  "with original file created by cicflowmeter")
            exit()

        #we have the data for analysis, now we have to analyse
        #THIS ALL IS IN WHILE LOOP

        #if loop if the dataset is not empty
        if len(dataset) != 0:

            dataset.drop(dataset.iloc[:, [0, 1, 2, 3, 5, 6, 83]], axis=1, inplace=True)
            complete_dataset.drop(complete_dataset.iloc[:, [83]], axis=1, inplace=True)

            #we have the data for analysis
            for i in range(len(dataset)):
                if numberx == 1:
                    print("break for")
                    break
                Xrow = dataset.iloc[[i], :].values
                try:
                    Y_predict = loaded_model.predict(Xrow)
                except:
                    print("entered continue")
                    continue
                compXrow = complete_dataset.iloc[[i], :].values
                #for printing out number of rows
                #print(y)
                y = y + 1

                # if Y_predict == 1:
                #     print("ALERTT!!!")

                totalflows = y


                if compXrow[0, 1] == attackerIP:

                    # count for ddos flow
                    totalp = totalp + 1
                    print(totalp)
                    #if dataset.iloc[:, 83].values[i] == 1:
                    if Y_predict == 1:
                        # count for flows that are ddos and predicted 1 (right)
                        tp = tp + 1
                    else:
                        fn = fn + 1

                # for normal flows
                elif compXrow[0, 1] != attackerIP:
                    # count for normal flow
                    totaln = totaln + 1
                    if Y_predict == 0:
                        # count for flows that are ddos and predicted 0 (right)
                        tn = tn + 1
                    else:
                        fp = fp + 1

                Posprecision = tp / (tp + fp)
                Negprecision = tn / (tn + fn)

                precall = tp / (tp + fn)
                nrecall = tn / (tn + fp)

                Accuracy = (tp + tn) / totalflows
                Accuracyddos = tp / totalp
                Accuracynormal = tn / totaln

                setposrow(totalp-1)
                setnegrow(totaln-1)

                settp(tp-1)
                settn(tn-1)
                setfp(fp-1)
                setfn(fn-1)

                setavgaccuracy(round(Accuracy, 2))
                setddosaccuracy(round(Accuracyddos, 2))
                setnormalaccuracy(round(Accuracynormal, 2))

                setprepos(round(Posprecision, 2))
                setpreneg(round(Negprecision, 2))

                setrecallpos(round(precall, 2))
                setrecallneg(round(nrecall, 2))

                # print("Total flow count captured = " + str(len(dataset)))
                #
                # print("DDOS Flows = " + str(totalp))
                # print("Normal Flows = " + str(totaln))
                #
                # print("True Positives = " + str(tp))
                # print("False Positives = " + str(fp))
                # print("True Negatives = " + str(tn))
                # print("False Negatives = " + str(fn))
                #
                # print("Accuracy = " + str(Accuracy))
                # print("Accuracy DDOS = " + str(Accuracyddos))
                # print("Accuracy Normal = " + str(Accuracynormal))
                #
                # print("Precision Positive class = " + str(Posprecision))
                # print("Precision Negative class = " + str(Negprecision))
                #
                # print("Recall Positive class = " + str(precall))
                # print("Recall Negative class = " + str(nrecall))

                #for passing complete row content to csv writer rather than the dataset where the columns 1,2,3,4 etc have been removed

                Xrow_without_Y = complete_dataset.iloc[[i], :].values
                Flattened_X = Xrow_without_Y.flatten()

                complete_Xrow_with_Y = np.append(Flattened_X, Y_predict)

                #Writing a CSV file for offline Analysis
                with open(offlinefilepath, 'a', newline='') as offlinefile:
                    writer = csv.writer(offlinefile)
                    writer.writerow(complete_Xrow_with_Y)


        # else:
        # print("dataset empty, sleeping for 3 seconds")
        # time.sleep(3)
    #when while ends
    print("While ended")
    windowevaluate.destroy()



def settp(text):
    tptextlabel.config(text=text)
    windowevaluate.update()

    # FPlabel['text'] = "1234"


def gettp():
    return 0

def settn(text):
    tntextlabel.config(text=text)
    windowevaluate.update()
    #FPlabel['text'] = "1234"

def gettn():
    return 0


def setfp(text):
    fptextlabel.config(text=text)
    windowevaluate.update()
    # FPlabel['text'] = "1234"


def getfp():
    return 0

def setfn(text):
    fntextlabel.config(text=text)
    windowevaluate.update()
    # FPlabel['text'] = "1234"


def getfn():
    return 0



def setposrow(text):
    posrowtextlabel.config(text=text)
    windowevaluate.update()

def setnegrow(text):
    negrowtextlabel.config(text=text)
    windowevaluate.update()

def setavgaccuracy(text):
    avgaccuracytextlabel.config(text=text)
    windowevaluate.update()

def setddosaccuracy(text):
    ddosaccuracytextlabel.config(text=text)
    windowevaluate.update()

def setnormalaccuracy(text):
    normalaccuracytextlabel.config(text=text)
    windowevaluate.update()


def setprepos(text):
    prepostextlabel.config(text=text)
    windowevaluate.update()

def setpreneg(text):
    prenegtextlabel.config(text=text)
    windowevaluate.update()

def setrecallpos(text):
    recallpostextlabel.config(text=text)
    windowevaluate.update()

def setrecallneg(text):
    recallnegtextlabel.config(text=text)
    windowevaluate.update()



def setnumber(number):
    global numberx
    numberx = number

numberx = 0
def setbreakevaluatecode(number):
    global numberx
    numberx = number

def quitandopenhomewindow():
    print("Evaluate ended")
    setbreakevaluatecode(1)


def createwindowevaluationthread(inputfile, outputfile):

    threadwindowevaluation = threading.Thread(target=lambda: createwindowevaluation(inputfile, outputfile))
    threadwindowevaluation.start()

def gotostartevaluatingthread(attackerIP, inputfile, outputfile):
    setnumber(0)
    threadstartevaluate = threading.Thread(target=lambda: startevaluating(attackerIP, inputfile, outputfile))
    threadstartevaluate.start()



def createwindowevaluation(inputfile, outputfile):

    #creating the gui envoirnment for widgets


    global windowevaluate
    windowevaluate = tk.Tk()
    # windowtwo.geometry('800x800+200+0')
    windowevaluate.title("Smark Network Monitoring Tool")

    homecanvas = tk.Canvas(windowevaluate, width=800, height=800, bg='white')
    homecanvas.pack()
    headinglabel = Label(homecanvas, text="Smart Network Monitoring Tool", bg='white', fg='#0b0230', font=('helvetica', 25, 'bold'))
    homecanvas.create_window(400, 100, window=headinglabel)



    #creating the top part to get the attacker ip

    attackersiplabel = Label(homecanvas, text="Enter the Attackers IP for evaluation", bg='white', fg='black', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(400, 200, window=attackersiplabel)

    inputboxip = tk.Entry(windowevaluate)
    homecanvas.create_window(300, 250, window=inputboxip)

    global  startscanafteriprecievedbtn
    startscanafteriprecievedbtn = tk.Button(text='Start Scanning', command=lambda: gotostartevaluatingthread(inputboxip.get(), inputfile, outputfile), bg='light blue', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(500, 250, window=startscanafteriprecievedbtn)



    #now adding widgets for evaluation display
    row11 = "320"
    row12 = int(row11) + 30
    posrowsheadinglabel = Label(homecanvas, text= "Positive Flows", bg='white',font=('helvetica', 15, 'bold'))
    homecanvas.create_window(250, row11, window=posrowsheadinglabel)
    global posrowtextlabel
    posrowtextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(250, row12, window=posrowtextlabel)

    negrowsheadinglabel = Label(homecanvas, text="Negative Flows", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(550, row11, window=negrowsheadinglabel)
    global negrowtextlabel
    negrowtextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(550, row12, window=negrowtextlabel)

    row21 = "400"
    row22 = int(row21) + 30
    tpheadinglabel = Label(homecanvas, text="True Positives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, row21, window=tpheadinglabel)
    global tptextlabel
    tptextlabel = Label(homecanvas, text=gettp(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, row22, window=tptextlabel)


    tnheadinglabel = Label(homecanvas, text="True Negatives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, row21, window=tnheadinglabel)
    global tntextlabel
    tntextlabel = Label(homecanvas, text=gettn(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, row22, window=tntextlabel)


    fpheadinglabel = Label(homecanvas, text="False Positives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, row21, window=fpheadinglabel)
    global fptextlabel
    fptextlabel = Label(homecanvas, text=getfp(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, row22, window=fptextlabel)


    fnheadinglabel = Label(homecanvas, text="False Negatives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, row21, window=fnheadinglabel)
    global fntextlabel
    fntextlabel = Label(homecanvas, text=getfn(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, row22, window=fntextlabel)


    row31 = "480"
    row32 = int(row31)+30

    avgaccuracyheadinglabel = Label(homecanvas, text="Average Accuracy", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(200, row31, window=avgaccuracyheadinglabel)
    global avgaccuracytextlabel
    avgaccuracytextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(200, row32, window=avgaccuracytextlabel)

    ddosaccuracyheadinglabel = Label(homecanvas, text="DDOS Accuracy", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(400, row31, window=ddosaccuracyheadinglabel)
    global ddosaccuracytextlabel
    ddosaccuracytextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(400, row32, window=ddosaccuracytextlabel)

    normalaccuracyheadinglabel = Label(homecanvas, text="Normal Accuracy", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(600, row31, window=normalaccuracyheadinglabel)
    global normalaccuracytextlabel
    normalaccuracytextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(600, row32, window=normalaccuracytextlabel)

    row41 = "560"
    row42 = int(row41) + 30

    preposheadinglabel = Label(homecanvas, text="Pos Precision", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, row41, window=preposheadinglabel)
    global prepostextlabel
    prepostextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, row42, window=prepostextlabel)

    prenegheadinglabel = Label(homecanvas, text="Neg Precision", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, row41, window=prenegheadinglabel)
    global prenegtextlabel
    prenegtextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, row42, window=prenegtextlabel)

    recallposheadinglabel = Label(homecanvas, text="Pos Recall", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, row41, window=recallposheadinglabel)
    global recallpostextlabel
    recallpostextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, row42, window=recallpostextlabel)


    recallnegheadinglabel = Label(homecanvas, text="Neg Recall", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, row41, window=recallnegheadinglabel)
    global recallnegtextlabel
    recallnegtextlabel = Label(homecanvas, text="0", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, row42, window=recallnegtextlabel)

    global quitevaluatebtn
    quitevaluatebtn = tk.Button(text='Quit Evaluate',
                                            command= quitandopenhomewindow,
                                            bg='red', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(400, 700, window=quitevaluatebtn)

    quitevaluatebtn["state"] = "disabled"


    windowevaluate.mainloop()




