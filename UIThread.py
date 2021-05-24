import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
from random import randint
import shutil
import logging
import threading
import time
import webbrowser
import subprocess

def link_tree(self):
    input_id = listBox.focus()
    current_item = listBox.item(input_id)
    current_path = current_item.get('values')[0]
    current_directory = os.getcwd()
    full_file_path = current_directory + '/video_forBD/Fight_Tested/' + str(current_path) + '.avi'

    #open file
    if os.name == 'nt':
        webbrowser.open('{}'.format(full_file_path))
    else:
        subprocess.call(('open', full_file_path))
    # do whatever you want

UI = tk.Tk()
label = tk.Label(UI, text="Fight Videos", font=("Arial", 30)).grid(row=0, columnspan=3)
cols = ('Name of video', 'Why the video is violent')
listBox = ttk.Treeview(UI, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)
listBox.bind("<Double-1>", link_tree) #if double-click go to link_tree function

def Exit(my_thread):
    my_thread.do_run = False #if 'do_run' variable in the thread is False - the thread will be kill
    sys.exit("Bye Bye :)") #close program


def UpdateList():
    data_dir = 'video_forBD/Fight'
    t = threading.currentThread()

    while getattr(t, "do_run", True): #if 'do_run' == True - the thread is alive
        time.sleep(2)
        files = os.listdir(data_dir)
        if files:  # if folder Fight is not empty
            current_vid = files[0]
            current_vid_only_name = current_vid[:-4]


            #update the array with new values
            new_num1 = str(randint(0,1000))
            new_num2 = str(randint(0,1000))
            current_vid_results = ((current_vid_only_name, new_num2),)

            for i, (name, score) in enumerate(current_vid_results, start=1):
                listBox.insert("", "end", values=(name, score))



            shutil.move(os.path.join(data_dir, current_vid), 'video_forBD/Fight_Tested')

    #   showScores = tk.Button(UI, text="Continue", command=UI.destroy).grid()
    #    UI.after(2000, UpdateList)  # run itself again after 2000 ms

my_tread = threading.Thread(target=UpdateList)
my_tread.start()
closeButton = tk.Button(UI, text="Close", width=15, command=lambda: Exit(my_tread)).grid(row=4, column=1)
UI.mainloop()