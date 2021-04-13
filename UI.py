import tkinter as tk
from tkinter import ttk
from random import randint

tempList = ["aa", "bb"], ["gal", "sap"]

UI = tk.Tk()

def CreateList():
    i = 0
    while (i<100000000): #time for waiting for new video demo
        i= i + 1
    global tempList
    label = tk.Label(UI, text="Fight Videos", font=("Arial", 30)).grid(row=0, columnspan=3)
    cols = ('Name of video', 'Why the video is violent')
    listBox = ttk.Treeview(UI, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)

    #update the array with new values
    new_num1 = str(randint(0,1000))
    new_num2 = str(randint(0,1000))
    tempList = tempList + ((new_num1, new_num2),)


    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(name, score))

#   showScores = tk.Button(UI, text="Continue", command=UI.destroy).grid()
    UI.after(2000, CreateList)  # run itself again after 2000 ms


CreateList() #show the list
closeButton = tk.Button(UI, text="Close", width=15, command=exit).grid(row=4, column=1)
UI.mainloop()






