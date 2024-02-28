from tkinter import *

count=0
def btn_click():
    count=count+1
    print("Button clicked ", count ," times.")
  

window = Tk()

btn = Button(window, text="Click Me!", command=btn_click)

btn.pack()

window.mainloop()
