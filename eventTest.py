from tkinter import *

root = Tk()
root.title("NextgenTetris")

def show(e):
    txt.pack()

btn1 = Button(root, text="Создать событие")
btn1.bind( '<Button-1>', lambda e: root.event_generate('<<MyEvent>>') )
btn1.pack()

txt = Label( root, text = "Событие получено" )

root.bind( '<<MyEvent>>', show )




root.mainloop()
