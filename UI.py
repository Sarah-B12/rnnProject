import os
import tkinter as tk
from tkinter import ttk
from random import randint
import shutil

fight_videos = ["here", "be"], ["the", "videos"]


UI = tk.Tk()
label = tk.Label(UI, text="Fight Videos", font=("Arial", 30)).grid(row=0, columnspan=3)
cols = ('Name of video', 'Why the video is violent')
listBox = ttk.Treeview(UI, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)


def UpdateList():
    global fight_videos
    data_dir = 'video_forBD/Fight'
    files = os.listdir(data_dir)
    if files:  # if folder Fight is not empty
        current_vid = files[0]

        #update the array with new values
        new_num1 = str(randint(0,1000))
        new_num2 = str(randint(0,1000))
        current_vid_results = ((new_num1, new_num2),)


        for i, (name, score) in enumerate(current_vid_results, start=1):
            listBox.insert("", "end", values=(name, score))

        shutil.move(os.path.join(data_dir, current_vid), 'video_forBD/Fight_Tested')
#   showScores = tk.Button(UI, text="Continue", command=UI.destroy).grid()
    UI.after(2000, UpdateList)  # run itself again after 2000 ms


UpdateList()  # show the list
closeButton = tk.Button(UI, text="Close", width=15, command=exit).grid(row=4, column=1)
UI.mainloop()






