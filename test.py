from tkinter import *
import webbrowser

def weblink(*args):
    index = lb.curselection()[0]
    item = lb.get(index)
    webbrowser.open_new(item)

list_of_items = ['Google news',
                 'c://1.avi',
                 'Yahoo news',
                 'https://news.yahoo.com/']
root = Tk()
lb = Listbox(root)
lb.bind('<<ListboxSelect>>', weblink)
for item in list_of_items:
    lb.insert(END, item)
lb.pack()
root.mainloop()