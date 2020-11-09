#ВНЁС ИЗМЕНЕНИЯ
#Ну давай еще что то на анг
#Напримерм
from tkinter import *
import random
from tkinter import messagebox as mb
#!/usr/bin/env python
# -- coding: utf-8 --

root = Tk()
root.title("NextgenTetris")

newVariable = IntVar(root)
mainFrame = Frame( root, bd = 15) 
mainFrame.pack( expand=True, fill='both' )

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='Menu')
mainmenu.add_command(label='Restart')

menuFr = Frame( mainFrame, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( mainFrame, bd = 0)
fieldFr.pack( expand=True, fill='both')

colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]
fieldColorsCode = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
fieldOfBtns = []


startX = IntVar(root)
startY = IntVar(root)
btnSize = IntVar(root)

startX.set(15)
startY.set(70)
btnSize.set(80)


def fieldClick(event):
    for i in range(3):
        for j in range(3):    
            if event.widget == fieldOfBtns[i][j]:
                currCode = fieldColorsCode[i][j]
                currCode += 1
                if currCode == len(colors): currCode = 0
                fieldColorsCode[i][j] = currCode
                event.widget.config( bg = colors[ currCode ] )
    check = True
    sample = fieldColorsCode[0][0]
    for i in range(3):
        for j in range(3):
           if  fieldColorsCode[i][j] != sample: check = False
    
    if check:
        newField()
            
def makefield():
    for i in range(3):
        fieldOfBtns.append([])
        fieldFr.rowconfigure(i, weight=1, minsize = btnSize.get())
        for j in range(3):
            fieldFr.columnconfigure(j, weight=1,  minsize = btnSize.get())
            
            colorCode = random.randint(0, len(colors) - 1)
            fieldColorsCode[i][j] = colorCode
            btn = Button( fieldFr, bg = colors[ colorCode ])
            
            btn.grid( row=i, column=j, sticky='nsew')
            
            btn.bind('<Button-1>',fieldClick)
            fieldOfBtns[i].append( btn )
makefield()

def newField():
    infoTxt.config( text = "WOW!!! YOU WIN!" )
    answ = mb.askokcancel('YOU WIN!','Start new round?')
    if answ:
        fieldColorsCode.clear()
        for i in range(3):
            fieldColorsCode.append([])
            for j in range(3):
                fieldColorsCode[i].append(0)
        fieldOfBtns.clear()
        #makefield()    





infoTxt = Label(
    menuFr,
    bg='white',
    text = 'All cells must be the same color',
    justify = CENTER,
    font = ( 'Arial', 12 )
)

infoTxt.pack( padx=0, pady=0)

root.mainloop()
