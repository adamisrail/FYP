import pandas as pd
import numpy as np
import time
import pickle
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *





def startscanning():
    # load the model from disk



    loaded_model = pickle.load(open(r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\LogisticRegression_Model1.sav', 'rb'))
    #data recieved from cicflowmeter is this file
    path = r"D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\2020-03-15_Flow.csv"

    offlinefilepath = r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\outputfile.csv'

    x = 0
    y = 1
    while(True):
        try:

            dataset = pd.read_csv(path, skiprows=x)
            complete_dataset = pd.read_csv(path, skiprows=x)

            x = x + len(dataset)

            #print(x)

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


            for i in range(len(dataset)):
                Xrow = dataset.iloc[[i], :].values
                Y_predict = loaded_model.predict(Xrow)

                #for printing out number of rows
                print(y)
                y = y + 1
                settp(y)
                settn(y+1)
                setfp(y+2)
                setfn(y+3)
                if Y_predict == 1:
                    print("ALERTT!!!")

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



def settp(text):
    tptextlabel.config(text=text)
    windowtwo.update()
    # FPlabel['text'] = "1234"


def gettp():
    return 0

def settn(text):
    tntextlabel.config(text=text)
    windowtwo.update()
    #FPlabel['text'] = "1234"

def gettn():
    return 0


def setfp(text):
    fptextlabel.config(text=text)
    windowtwo.update()
    # FPlabel['text'] = "1234"


def getfp():
    return 0

def setfn(text):
    fntextlabel.config(text=text)
    windowtwo.update()
    # FPlabel['text'] = "1234"


def getfn():
    return 0



def onbuttonclickstartscan():
    startscanning()


def createwindowtwo():

    #creating the gui envoirnment for widgets

    global windowtwo
    windowtwo = tk.Tk()
    # windowtwo.geometry('800x800+200+0')
    windowtwo.title("Smark Network Monitoring Tool")

    homecanvas = tk.Canvas(windowtwo, width=800, height=800, bg='white')
    homecanvas.pack()
    headinglabel = Label(homecanvas, text="Smart Network Monitoring Tool", bg='white', fg='#FA9B01', font=('helvetica', 25, 'bold'))
    homecanvas.create_window(400, 100, window=headinglabel)



    #creating the top part to get the attacker ip

    attackersiplabel = Label(homecanvas, text="Enter the Attackers IP for evaluation", bg='white', fg='black', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(400, 200, window=attackersiplabel)

    inputboxip = tk.Entry(windowtwo)
    homecanvas.create_window(300, 250, window=inputboxip)

    startscanafteriprecievedbtn = tk.Button(text='Start Scanning', command=onbuttonclickstartscan, bg='#FA9B01', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(500, 250, window=startscanafteriprecievedbtn)



    #now adding widgets for evaluation display

    tpheadinglabel = Label(homecanvas, text="True Positives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, 350, window=tpheadinglabel)
    global tptextlabel
    tptextlabel = Label(homecanvas, text=gettp(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(150, 400, window=tptextlabel)


    tnheadinglabel = Label(homecanvas, text="Ture Negatives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, 350, window=tnheadinglabel)
    global tntextlabel
    tntextlabel = Label(homecanvas, text=gettn(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(316, 400, window=tntextlabel)


    fpheadinglabel = Label(homecanvas, text="False Positives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, 350, window=fpheadinglabel)
    global fptextlabel
    fptextlabel = Label(homecanvas, text=getfp(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(483, 400, window=fptextlabel)


    fnheadinglabel = Label(homecanvas, text="False Negatives", bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, 350, window=fnheadinglabel)
    global fntextlabel
    fntextlabel = Label(homecanvas, text=getfn(), bg='white', font=('helvetica', 15, 'bold'))
    homecanvas.create_window(650, 400, window=fntextlabel)



    windowtwo.mainloop()


createwindowtwo()

