from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
root.title("NextgenTetris")

btnSize = 80
currRound = 1
row = 2
col = 2
colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]
status = ""

fieldModel = []
fieldBtns = []


#---------------RefactoringFunc------
def startGame():
    mainMenuFr.forget()
    gameFr.pack( expand=True, fill='both' )

    newGame( currRound )
    render()

def newGame( round ):
    global fieldModel, fieldBtns, status

    fieldModel = modelInit( row, col )
    fieldBtns = createField( row, col )

    status = "All cells must be the same color"
def modelInit( r, c ):
    m = []
    for i in range( r ):
        m.append([])
        for j in range( c ):
            code = random.randint( 0, len(colors) - 1 )
            m[i].append( code )
    return m

def createField( r, c ):
    field = []
    for i in range( r ):
        field.append([])
        for j in range( c ):
            btn = Button( fieldFr )
            btn.grid( row=i, column=j, sticky='nsew')
            btn.bind( '<Button-1>', fieldOnClick )
            field[i].append( btn )
    return field

def check():
    win = True
    sample = fieldModel[0][0]
    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            if sample != fieldModel[i][j]:
                win = False

    if (win):
        status = "WOOW!! YOU WIN!"
        ask('YOU WIN!', 'Start new round?', newRound, gotoMainMenu)
def fieldDestroy():
    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            fieldBtns[i][j].destroy()
def newRound():
    print('New Round')

def gotoMainMenu():
    fieldDestroy()
    gameFr.forget()
    mainMenuFr.pack( expand=True, fill='both' )

def ask(title, text, okAction, cancelAction):
    if mb.askokcancel(title, text):
        okAction()
    else:
        cancelAction()
def changeColor( w ):
    global fieldModel, fieldBtns, status

    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            if fieldBtns[i][j] == w:
                fieldModel[i][j] += 1
            if fieldModel[i][j] == len(colors):
                fieldModel[i][j] = 0
    render()

def render():
    #--------Field--------------------
    for i in range( len(fieldModel) ):
        fieldFr.rowconfigure( i, weight=1, minsize = btnSize )
        for j in range( len(fieldModel[0]) ):
            fieldFr.columnconfigure( j, weight=1,  minsize = btnSize )
            fieldBtns[i][j].config(
                bg = colors[ fieldModel[i][j] ]
            )
    #--------InfoText--------------------
    infoTxt.config( text = status )

#---------------OnClick--------------
def startOnClick():
    startGame()

def fieldOnClick(e):
    changeColor( e.widget )
    check()



gameFr = Frame( root, bd = 15)
#gameFr.pack( expand=True, fill='both' )

menuFr = Frame( gameFr, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( gameFr, bd = 0)
fieldFr.pack( expand=True, fill='both')

showcurrRound = Label( menuFr, text = f'Round:{currRound}', font=('David',12), bg='#DDD')
showcurrRound.pack(anchor='ne')

mainMenuFr = Frame( root, bd = 15)
mainMenuFr.pack( expand=True, fill='both' )

infoTxt = Label(
    menuFr,
    bg='white',
    justify = CENTER,
    font = ( 'Arial', 12 )
)
infoTxt.pack( padx=0, pady=0)

welcomelbl = Label(
    mainMenuFr,
    text='Welcome to Nextgen Game!',
    justify=CENTER,
    font=('Comic Sans MS', 14)
)
welcomelbl.pack()

startBtn = Button(
    mainMenuFr,
    text='start',
    justify= CENTER,
    command = startOnClick,
    height=1, width=10,
    bg = 'darkblue',
    fg='white',
    font=('Comic Sans MS', 14)
)
startBtn.pack()

levelsBtn = Button(
    mainMenuFr,
    text='levels',
    justify = CENTER,
    height = 1, width = 10,
    bg = 'darkblue',
    fg='white',
    font=('Comic Sans MS', 14)
)
levelsBtn.pack()





root.mainloop()
