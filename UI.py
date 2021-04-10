import tkinter as tk
from tkinter import ttk

tempList = ['1', 'b'], ['2', 'c'], ['3', 'd'], ['70', 'adsasd']




def CreateList():
    scores = tk.Tk()
    label = tk.Label(scores, text="Fight Videos", font=("Arial", 30)).grid(row=0, columnspan=3)
    cols = ('Name of video', 'Why the video is violent')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(name, score))

    showScores = tk.Button(scores, text="Continue", command=scores.destroy).grid()


    scores.mainloop()



CreateList() #show the list

tempList = ['a', '3'], ['2', '1212'] #update the videos
CreateList() #show the list

