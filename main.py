from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
root.title("NextgenTetris")

startX = IntVar(root)
startY = IntVar(root)
btnSize = IntVar(root)

startX.set(15)
startY.set(70)
btnSize.set(80)

rounds = 1
rowscolumns = 3
colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]
fieldModel = []
fieldBtns = []

def fieldModelfill():
    for i in range(rowscolumns):
        fieldModel.append([])
        for j in range(rowscolumns):
            fieldModel[i].append(0)
fieldModelfill()


def fieldClick(event):
    for i in range(rowscolumns):
        for j in range(rowscolumns):    
            if event.widget == fieldBtns[i][j]:
                currCode = fieldModel[i][j]
                currCode += 1                
                if currCode == len(colors): currCode = 0
                fieldModel[i][j] = currCode
                event.widget.config( bg = colors[ currCode ] )
    check = True
    sample = fieldModel[0][0]
    for i in range(rowscolumns):
        
        for j in range(rowscolumns):
            if  fieldModel[i][j] != sample: check = False
    
    if check:
        global rounds
        rounds += 1
        newField()


def makefield():
    
    infoTxt.pack( padx=0, pady=0)
    startBtn.forget()
    levelsBtn.forget()
    for i in range(rowscolumns):
        fieldBtns.append([])
        fieldFr.rowconfigure(i, weight=1, minsize = btnSize.get())
        for j in range(rowscolumns):
            fieldFr.columnconfigure(j, weight=1,  minsize = btnSize.get())  
            
            colorCode = random.randint(0, len(colors) - 1)
            fieldModel[i][j] = colorCode
            btn = Button( fieldFr, bg = colors[ colorCode ])
            
            btn.grid( row=i, column=j, sticky='nsew')  
            
            btn.bind('<Button-1>',fieldClick)
            fieldBtns[i].append( btn )

def newField():
    infoTxt.config( text = "WOW!!! YOU WIN!" )
    answ = mb.askokcancel('YOU WIN!','Start new round?')
    if answ:
        btnsDestroy()
        fieldModel.clear()
        global rowscolumns
        rowscolumns = 4
        fieldModelfill()
        fieldBtns.clear()
        makefield()   
        showRounds['text'] = f'Rounds:{rounds}'
        infoTxt['text'] = 'All cells must be the same color'
        
def btnsDestroy():
    for i in range(rowscolumns):   
        for j in range(rowscolumns): 
            fieldBtns[i][j].destroy()
        

mainFrame = Frame( root, bd = 15) 
mainFrame.pack( expand=True, fill='both' )

menuFr = Frame( mainFrame, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( mainFrame, bd = 0)
fieldFr.pack( expand=True, fill='both')

startBtn = Button(menuFr,text='start',justify= CENTER,command = makefield,height=1,width=10)
startBtn.pack()

levelsBtn = Button(menuFr,text='levels',justify= CENTER,height=1,width=10)
levelsBtn.pack()

showRounds = Label(menuFr,text=f'Rounds:{rounds}',font=('David',12),bg='#DDD')
showRounds.pack(anchor='ne')

infoTxt = Label(
    menuFr,
    bg='white',
    text = 'All cells must be the same color',
    justify = CENTER,
    font = ( 'Arial', 12 )
)


root.mainloop()
