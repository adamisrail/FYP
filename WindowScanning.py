import pandas as pd
import numpy as np
import time
import pickle
import csv
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import *





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

                y = y + 1
                Xrow = dataset.iloc[[i], :].values

                try:
                    Y_predict = loaded_model.predict(Xrow)
                except:
                    print("we in except, continue")
                    continue
                #for printing out number of rows
                print(y)
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




def createwindowscan(inputfilepath, outputfilepath):
    print(("create window scan"))
    #creating the gui envoirnment for widgets

    global windowscanning



    # initalise the tkinter GUI
    windowscanning = tk.Tk()
    windowscanning.title("Smark Network Monitoring Tool")
    windowscanning.geometry("500x500")  # set the root dimensions
    windowscanning.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
    windowscanning.resizable(0, 0)  # makes the root window fixed in size.

    # Frame for TreeView
    frame1 = tk.LabelFrame(windowscanning, text="Excel Data")
    frame1.place(height=250, width=500)

    # Frame for open file dialog
    file_frame = tk.LabelFrame(windowscanning, text="Open File")
    file_frame.place(height=100, width=400, rely=0.65, relx=0)

    # Buttons
    button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
    button1.place(rely=0.65, relx=0.50)

    button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
    button2.place(rely=0.65, relx=0.30)

    # The file/file path text
    label_file = ttk.Label(file_frame, text="No File Selected")
    label_file.place(rely=0, relx=0)

    ## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(frame1, orient="vertical",
                               command=tv1.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal",
                               command=tv1.xview)  # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set,
                  yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    def File_dialog():
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        label_file["text"] = filename
        return None

    def Load_excel_data():
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end",
                       values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    windowscanning.mainloop()



#just delete this and start from GUIstart
createwindowscan("abc", "abc")



