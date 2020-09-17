
import pandas as pd
import numpy as np

import pickle
import csv
import tkinter as tk

from tkinter import *
from tkinter import filedialog, messagebox, ttk
import threading
import time





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



                #tv1.delete(*tv1.get_children())

                tv1.set(0, 'one', value=(y))

                tv1.set(1, 'one', value=(totalp - 1))
                tv1.set(2, 'one', value=(totaln - 1))

                tv1.set(3, 'one', value=(tp - 1))
                tv1.set(4, 'one', value=(tn - 1))
                tv1.set(5, 'one', value=(fp - 1))
                tv1.set(6, 'one', value=(fn - 1))

                tv1.set(7, 'one', value=(round(Accuracy, 2)))
                tv1.set(8, 'one', value=(round(Accuracyddos, 2)))
                tv1.set(9, 'one', value=(round(Accuracynormal, 2)))

                tv1.set(10, 'one', value=(round(Posprecision, 2)))
                tv1.set(11, 'one', value=(round(Negprecision, 2)))

                tv1.set(12, 'one', value=(round(precall, 2)))
                tv1.set(13, 'one', value=(round(nrecall, 2)))


                # enterrow(round(Accuracy, 2))
                # enterrow(round(Accuracyddos, 2))
                # enterrow(round(Accuracynormal, 2))
                #
                # enterrow(round(Posprecision, 2))
                # enterrow(round(Negprecision, 2))
                #
                # enterrow(round(precall, 2))
                # enterrow(round(nrecall, 2))

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

def enterrow(data):
    tv1.insert("", "end", values=data)
    windowevaluate.update()

def createwindowevaluation(inputfile, outputfile):

    #creating the gui envoirnment for widgets


    global windowevaluate
    windowevaluate = tk.Tk()
    # windowtwo.geometry('800x800+200+0')
    windowevaluate.title("Smark Network Monitoring Tool")

    homecanvas = tk.Canvas(windowevaluate, width=800, height=800)
    homecanvas.pack()

    headinglabel = Label(homecanvas, text="Smart Network Monitoring Tool", fg='#0b0230', font=('helvetica', 25, 'bold'))
    homecanvas.create_window(400, 100, window=headinglabel)



    #creating the top part to get the attacker ip

    attackersiplabel = Label(homecanvas, text="Enter the Attackers IP for evaluation", fg='black', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(400, 170, window=attackersiplabel)

    inputboxip = tk.Entry(windowevaluate)
    homecanvas.create_window(300, 210, window=inputboxip)

    global  startscanafteriprecievedbtn
    startscanafteriprecievedbtn = tk.Button(text='Start Scanning', command=lambda: gotostartevaluatingthread(inputboxip.get(), inputfile, outputfile), bg='light blue', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(500, 210, window=startscanafteriprecievedbtn)


    global quitevaluatebtn
    quitevaluatebtn = tk.Button(text='Quit Evaluate',
                                            command= quitandopenhomewindow,
                                            bg='red', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(400, 700, window=quitevaluatebtn)

    quitevaluatebtn["state"] = "disabled"


    treeviewframe = LabelFrame(windowevaluate, text="Excel Data")
    treeviewframe.place(height=330, width=400, rely=0.35, relx=0.25)

    global tv1
    tv1 = ttk.Treeview(treeviewframe)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% o its container (frame1).

    # treescrolly = tk.Scrollbar(treeviewframe, orient="vertical",
    #                            command=tv1.yview)  # command means update the yaxis view of the widget
    # treescrollx = tk.Scrollbar(treeviewframe, orient="horizontal",
    #                            command=tv1.xview)  # command means update the xaxis view of the widget
    # tv1.configure(xscrollcommand=treescrollx.set,
    #               yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    # treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    # treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    listofcolumns = ["Measure", "Measure Value"]

    # tv1["column"] = listofcolumns
    # tv1["show"] = "headings"
    # tv1.heading("Measure", text="Measure")
    # tv1.heading("Measure Value", text="Measure Value")

    tv1["columns"] = ("one")
    # tv1["show"] = "headings"
    tv1.column('#0')
    tv1.column("one", width=150)

    tv1.heading('#0', text="Measures")
    tv1.heading("one", text="Values")

    tv1.insert(parent="", index="end", iid=0, text='Total Flows', values=("0"))
    tv1.insert(parent="", index="end", iid=1, text='Total Positive Flows', values=("0"))
    tv1.insert(parent="", index="end", iid=2, text='Total Negative Flows', values=("0"))

    tv1.insert(parent="", index="end", iid=3, text='True Positives', values=("0"))
    tv1.insert(parent="", index="end", iid=4, text='True Negatives', values=("0"))
    tv1.insert(parent="", index="end", iid=5, text='False Positives', values=("0"))
    tv1.insert(parent="", index="end", iid=6, text='False Negatives', values=("0"))

    tv1.insert(parent="", index="end", iid=7, text='Average Accuracy', values=("0"))
    tv1.insert(parent="", index="end", iid=8, text='Positive Class Accuracy', values=("0"))
    tv1.insert(parent="", index="end", iid=9, text='Negative Class Accuracy', values=("0"))

    tv1.insert(parent="", index="end", iid=10, text='Positive Class Precision', values=("0"))
    tv1.insert(parent="", index="end", iid=11, text='Negative Class Precision', values=("0"))

    tv1.insert(parent="", index="end", iid=12, text='Positive Class Recall', values=("0"))
    tv1.insert(parent="", index="end", iid=13, text='Negative Class Recall', values=("0"))

    windowevaluate.mainloop()

#createwindowevaluation(r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\2020-03-15_Flow.csv', r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models')