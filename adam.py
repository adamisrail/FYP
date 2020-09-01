import pandas as pd
import numpy as np
import time
import pickle
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import *
import threading
from datetime import datetime





def startscanning(inputfilepath, outputfilepath):
    # load the model from disk

    path = inputfilepath
    offlinefilepath = outputfilepath

    loaded_model = pickle.load(open(r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\LogisticRegression_Model1.sav', 'rb'))
    #data recieved from cicflowmeter is this file
    path = r"D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\2020-03-15_Flow.csv"

    offlinefilepath = r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\outputfile.csv'

    x = 0
    y = 1
    while(True):

        if numberx == 1:
            setnumber(0)
            print("Break while")
            break

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

                if numberx == 1:
                    print("break for")
                    break
                settotalflows(y)
                y = y + 1
                Xrow = dataset.iloc[[i], :].values




                try:
                    Y_predict = loaded_model.predict(Xrow)
                except:
                    print("we in except, continue")
                    continue

                #for printing out number of rows
                #print(y)
                if Y_predict == 1:

                    now = datetime.now()
                    dt_string = now.strftime("%H:%M:%S %d/%m/%Y ")
                    ipaddress = complete_dataset.iloc[[i], 1].values
                    ipaddressnew = str(ipaddress)[2:-2]
                    try:
                        enterrow([ipaddressnew, "Yes", dt_string])
                    except:
                        print("GUI closed maybe")
                        quitwhileloopandwindow()



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


def setnumber(number):
    global numberx
    numberx = number

numberx = 0
def setbreakevaluatecode(number):
    global numberx
    numberx = number

def quitwhileloopandwindow():
    try:
        print("Evaluate ended")
        setbreakevaluatecode(1)
        windowscanning.destroy()

    except:
        print("exceptt to end code")

def enterrow(data):
    # tv1.insert("", "end", values=data)
    # windowscanning.update()
    print("enterrow")

#just delete this and start from GUIstart

def gotocreatewindowscanthread(inputfile, outputfile):
    createwindowscanthread = threading.Thread(target=lambda: createwindowscan(inputfile, outputfile))
    createwindowscanthread.start()



def gotostartscan(inputfile, outputfile):
    print("gotostartscan")
    setnumber(0)
    threadstartstan = threading.Thread(target=lambda: startscanning(inputfile, outputfile))
    threadstartstan.start()
    quitscanbtn["state"] = "normal"
    startscanbtn["state"] = "disabled"



def enterrow(data):
    tv1.insert("", "end", values=data)
    windowscanning.update()

def settotalflows(text):
    labeltotalflows.config(text=text)
    windowscanning.update()


def createwindowscan(inputfile, outputfile):

    #creating the gui envoirnment for widgets


    global windowscanning
    windowscanning = tk.Tk()
    windowscanning.protocol("WM_DELETE_WINDOW", quitwhileloopandwindow)
    windowscanning.geometry('800x800')
    windowscanning.title("Smark Network Monitoring Tool")
    windowscanning.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
    windowscanning.resizable(0, 0)


    homecanvas = tk.Canvas(windowscanning, width=800, height=800)
    homecanvas.pack()
    headinglabel = Label(homecanvas, text="Smart Network Monitoring Tool", fg='#FA9B01', font=('helvetica', 25, 'bold'))
    homecanvas.create_window(400, 100, window=headinglabel)

    global startscanbtn
    startscanbtn = Button(homecanvas, text="Start Scan", command=lambda: gotostartscan(inputfile, outputfile), bg='#FA9B01', fg='black', font=('helvetica', 12, 'bold'))
    homecanvas.create_window(300, 700, window=startscanbtn)
    startscanbtn["state"] = "normal"

    global quitscanbtn
    quitscanbtn = tk.Button(text='Quit Scan', command=lambda: quitwhileloopandwindow(), bg='red', fg='black', font=('helvetica', 12, 'bold'))
    quitscanbtn["state"] = "disabled"
    homecanvas.create_window(500, 700, window=quitscanbtn)


    global labeltotalflows
    labeltotalflows = Label(homecanvas, text="0", font=('helvetica', 10, 'bold'))
    homecanvas.create_window(20, 570, window=labeltotalflows)

    treeviewframe = LabelFrame(windowscanning, text="Excel Data")
    treeviewframe.place(height=400, width=800, rely=0.2, relx=0)

    global tv1
    tv1 = ttk.Treeview(treeviewframe)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(treeviewframe, orient="vertical",
                               command=tv1.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(treeviewframe, orient="horizontal",
                               command=tv1.xview)  # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    listofcolumns = ["IP Address", "Anomaly Detected", "Time of Detection"]

    tv1["column"] = listofcolumns
    tv1["show"] = "headings"
    tv1.heading("IP Address", text="IP Address")
    tv1.heading("Anomaly Detected", text="Anomaly Detected")
    tv1.heading("Time of Detection", text="Time of Detection")
    windowscanning.mainloop()



gotocreatewindowscanthread("abc", "abc")
