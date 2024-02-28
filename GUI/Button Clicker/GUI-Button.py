from tkinter import *

count = 0

def btn_click():
    global count
    count = count+1
    count_text.config(text=count)
  

window = Tk()


count_text = Label(text="0")
count_text.pack()


btn = Button(window, text="Click Me!", command=btn_click)
btn.pack()

window.mainloop()
