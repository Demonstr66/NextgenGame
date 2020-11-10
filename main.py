from tkinter import *
import random
from tkinter import messagebox as mb
#!/usr/bin/env python
# - coding: utf-8 -

root = Tk()
root.title("NextgenTetris")
root.resizable('False','False')

mainFrame = Frame( root, bd = 15) 
mainFrame.pack( expand=True, fill='both' )

menuFr = Frame( mainFrame, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( mainFrame, bd = 0)
fieldFr.pack( expand=True, fill='both')

colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]


rowscolumns = 3
fieldColorsCode = []
def fieldColorsCodefill():
    for i in range(rowscolumns):
        fieldColorsCode.append([])
        for j in range(rowscolumns):
            fieldColorsCode[i].append(0)
fieldColorsCodefill()
fieldOfBtns = []


startX = IntVar(root)
startY = IntVar(root)
btnSize = IntVar(root)

startX.set(15)
startY.set(70)
btnSize.set(80)

rounds = 1

showRounds = Label(menuFr,text=f'Rounds:{rounds}',font=('David',12),bg='#DDD')

def fieldClick(event):
    for i in range(rowscolumns):
        for j in range(rowscolumns):    
            if event.widget == fieldOfBtns[i][j]:
                currCode = fieldColorsCode[i][j]
                currCode += 1                
                if currCode == len(colors): currCode = 0
                fieldColorsCode[i][j] = currCode
                event.widget.config( bg = colors[ currCode ] )
    check = True
    sample = fieldColorsCode[0][0]
    for i in range(rowscolumns):
        
        for j in range(rowscolumns):
            if  fieldColorsCode[i][j] != sample: check = False
    
    if check:
        newField()


def makefield(): 
    showRounds.pack(anchor='ne')
    infoTxt.pack( padx=0, pady=0)
    welcomelbl.forget()
    startBtn.forget()
    levelsBtn.forget()
    for i in range(rowscolumns):
        fieldOfBtns.append([])
        fieldFr.rowconfigure(i, weight=1, minsize = btnSize.get())
        for j in range(rowscolumns):
            fieldFr.columnconfigure(j, weight=1,  minsize = btnSize.get())  
            
            colorCode = random.randint(0, len(colors) - 1)
            fieldColorsCode[i][j] = colorCode
            btn = Button( fieldFr, bg = colors[ colorCode ])
            
            btn.grid( row=i, column=j, sticky='nsew')  
            
            btn.bind('<Button-1>',fieldClick)
            fieldOfBtns[i].append( btn )

def newField():
    infoTxt.config( text = "WOW!!! YOU WIN!" )
    answ = mb.askokcancel('YOU WIN!','Start new round?')
    if answ:
        global rounds
        rounds += 1        
        btnsDestroy()
        fieldColorsCode.clear()
        global rowscolumns
        rowscolumns = 4
        fieldColorsCodefill()
        fieldOfBtns.clear()
        makefield()   
        showRounds['text'] = f'Rounds:{rounds}'
        infoTxt['text'] = 'All cells must be the same color'
        
def btnsDestroy():
    for i in range(rowscolumns):   
        for j in range(rowscolumns): 
            fieldOfBtns[i][j].destroy()
        
welcomelbl = Label(menuFr, text='Welcome to Nextgen Game!', justify=CENTER,font=('Comic Sans MS', 14))
welcomelbl.pack()
startBtn = Button(menuFr,text='start',justify= CENTER,command = makefield,height=1,width=10, bg = 'darkblue', fg='white', font=('Comic Sans MS', 14))
startBtn.pack()
levelsBtn = Button(menuFr,text='levels',justify= CENTER,height=1,width=10,bg = 'darkblue', fg='white', font=('Comic Sans MS', 14))
levelsBtn.pack()


infoTxt = Label(
    menuFr,
    bg='white',
    text = 'All cells must be the same color',
    justify = CENTER,
    font = ( 'Arial', 12 )
)


root.mainloop()