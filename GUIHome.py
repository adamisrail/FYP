#from WindowEvaluation import *
from WindowEvalWithTreeView import *

from WindowScanning import *

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *






logopath = r'D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\logo3.png'
wallpaper = r"D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\bg3.png"


# code for browse
def getExcel():
    global file_path

    file_path = filedialog.askopenfilename()

    #if file_path.endswith(".csv") or file_path.endswith(".xlsx"):
    if file_path.endswith(".csv"):
        print("csv filed detected")

        evaluatebtn["state"] = "normal"
        scanbtn["state"] = "normal"

    elif file_path == "":
        print("Empty location path")

    else:
        file_path = ""
        print("Invalid Format")
        messagebox.showerror("Error", "Invalid File Format!\nPlease browse again.\nValid Formats are '.csv' and '.xlsx'.")



def gotoevaluate():
    if file_path == "":
        messagebox.showerror("Error", "Please select a correct file path.")
    else:
        print("starting analysis from windowevaluation")
        folderpath = os.path.dirname(file_path)
        print(folderpath)
        homewindow.destroy()
        createwindowevaluationthread(file_path, folderpath)

def gotoscan():
    print("gotoscan")
    if file_path == "":
        messagebox.showerror("Error", "Please select a correct file path.")
    else:
        print("starting analysis from Window Scanning. THis is GUIHome though")
        homewindow.destroy()
        folderpath = os.path.dirname(file_path)
        gotocreatewindowscanthread(file_path, folderpath)


def startwindowhome():
    global homewindow
    homewindow = tk.Tk()
    #dont resize to size of widget upon its addition/pack
    homewindow.pack_propagate(False)
    #dont be resizable
    homewindow.resizable(0, 0)
    homewindow.geometry('800x800+200+0')
    homewindow.title("Smark Network Monitoring Tool")




    # width = 1600
    # height = 1600
    # img = Image.open(wallpaper)
    # img = img.resize((width, height), Image.ANTIALIAS)
    # img.save("D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\image4.png")
    # print("saved")
    # photoImg = PhotoImage(img)



    homecanvas = tk.Canvas(homewindow, width=800, height=800)
    homecanvas.pack(expand=YES, fill=BOTH)

    # background_label = Label(homecanvas, image=wallpaperimg)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)

    wallpaperimg = PhotoImage(file=wallpaper)
    #background image control here
    homecanvas.create_image(400, 400, image=wallpaperimg)


    homecanvas.create_text(450, 100, text="Smart Network Monitoring Tool", fill='#0b0230', font=('Arial', 25, 'bold'))


    # headinglabel = Label(homecanvas, text="Smart Network Monitoring Tool", fg='#FA9B01', font=('helvetica', 25, 'bold'))
    # homecanvas.create_window(450, 100, window=headinglabel)

    image = PhotoImage(file=logopath, master=None)
    logo = Label(homecanvas, image=image, bg='lavender')
    homecanvas.create_window(100, 100, window=logo)


    homecanvas.create_text(400, 200, text="Welcome", fill='#0b0230', font=('Arial', 35, 'bold'))
    #WelcomeLabel = Label(homecanvas, text="Welcome!", bg="white", font=('helvetica', 35, 'bold'))
    #homecanvas.create_window(400, 200, window=WelcomeLabel)

    homecanvas.create_text(400, 590, text="Please choose the input file received from network sniffing tool!", fill='#0b0230', font=('Arial', 15, 'bold'))

    # choosetrainalgofile = Label(homecanvas, text="Please choose the input file received from network sniffing tool!", bg='white',
    #                             font=('helvetica', 15, 'bold'))
    # choosetrainalgofile.pack()
    # homecanvas.create_window(400, 600, window=choosetrainalgofile)
    # homecanvas.pack()

    browseButton_Excel = tk.Button(text='Browse Input File', command=getExcel, bg='light blue', fg='black',
                                   font=('Arial', 12))
    homecanvas.create_window(200, 650, window=browseButton_Excel)

    global evaluatebtn
    evaluatebtn = tk.Button(text='Evaluate', command=lambda: gotoevaluate(), bg='light blue', fg='black',
                            font=('helvetica', 12))
    evaluatebtn["state"] = "disabled"
    homecanvas.create_window(600, 650, window=evaluatebtn)

    global scanbtn
    scanbtn = tk.Button(text='Start Scan', command=lambda: gotoscan(), bg='light blue', fg='black',
                            font=('helvetica', 12))

    scanbtn["state"] = "disabled"

    homecanvas.create_window(400, 650, window=scanbtn)

    homewindow.mainloop()


def errormessage():
    errorwindow = tk.Tk()
    errorwindow.title("Error window!")

    canvaserror = tk.Canvas(errorwindow, width=200, height=200)
    errorlabel = Label(canvaserror, text="Error Encountered", fg='red', font=('helvetica', 15, 'bold'))
    errorlabel.pack()
    canvaserror.create_window(100, 100, window=errorlabel)
    canvaserror.pack()

    errorwindow.mainloop()

