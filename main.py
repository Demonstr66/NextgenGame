from tkinter import *
import random
from tkinter import messagebox as mb
from helper import *

root = Tk()
root.title("NextgenTetris")

btnSize = 80
currRound = 0
currStatus = ""

colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff","#60F", "#f90"]
#           red    green   blue   yellow   pink   lBlue    white  black  fiolet  orange
rounds = [
    {
        'id': 1,
        'row': 2, 'col': 2,
        'status': 'All cells must be the same color! 1',
        'timer': 50000,
        'rndColorOfCell': False, # Or timer
        'rndOrderColors': False,
        'numberOfColors': 10
    },
    {
        'id': 2,
        'row': 2, 'col': 3,
        'status': 'All cells must be the same color! 2',
        'timer': None,
        'rndColorOfCell': False, # Or timer
        'rndOrderColors': True,
        'numberOfColors': 5
    },
    {
        'id': 3,
        'row': 3, 'col': 3,
        'status': f'All cells must be the same color! 3',
        'timer': None,
        'rndColorOfCell': 10000, # Or False
        'rndOrderColors': True,
        'numberOfColors': 8
    },
]

fieldModel = []
fieldBtns = []

currtime = 0


#---------------RefactoringFunc------
def startGame():
    mainMenuFr.forget()
    gameFr.pack( expand=True, fill='both' )
    newRound( currRound )
    render()
def newRound( round ):
    global fieldModel, fieldBtns, currStatus, currtime
    currtime = 0
    Show.config(text=currtime)
    row = rounds[ currRound ][ 'row' ]
    col = rounds[ currRound ][ 'col' ]

    fieldModel = modelInit( row, col, rounds[ currRound ][ 'numberOfColors' ] )
    fieldBtns = createField( row, col )

    currStatus = rounds[ currRound ][ 'status' ]

    time = rounds[ currRound ][ 'rndColorOfCell' ]
    if ( time ):
        fieldFr.after( time, rndChangeColor)
    # timerCreate(rounds[currRound][ 'timer' ])

# def timerCreate(timeimp):
#     global currtime
#     t = timer(Show,timeimp)
#     t.start()
#     currtime = t.time




def rndChangeColor():
    global fieldModel

    time = rounds[ currRound ][ 'rndColorOfCell' ]


    i = random.randint( 0, len(fieldModel) - 1 )
    j = random.randint( 0, len(fieldModel[0]) - 1 )

    oldColor = fieldModel[i][j]
    newColor = oldColor

    while newColor == oldColor:
        newColor = random.randint( 0, rounds[ currRound ][ 'numberOfColors' ] - 1 )
    fieldModel[i][j] = newColor

    render()
    if not check(): fieldFr.after( time, rndChangeColor )
def modelInit( r, c, colorNum ):
    m = []
    for i in range( r ):
        m.append([])
        for j in range( c ):
            code = random.randint( 0, colorNum - 1 )
            m[i].append( code )
    return m

def createField( r, c ):
    field = []
    for i in range( r ):
        field.append([])
        for j in range( c ):
            btn = Button( fieldFr )
            btn.grid( row=i, column=j, sticky='nsew')
            btn.bind( '<Button-1>', btnFieldClick(i, j))
            field[i].append( btn )
    return field


def nextLevel():
    global currRound

    fieldDestroy()
    newRound( currRound )
    render()

def check():
    global currRound, currStatus
    win = True
    sample = fieldModel[0][0]
    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            if sample != fieldModel[i][j]:
                win = False

    if win:
        currStatus = "WOOW!! YOU WIN!"
        currRound += 1
        print(t.stop())

        typeModal = "askokcancel"
        if ( currRound == len(rounds) ):
            typeModal = "askretrycancel"
            currRound = len(rounds) - 1
        mb = ask('YOU WIN!', 'Start new round?', nextLevel, gotoMainMenu, typeModal)
        mb.create()


def fieldDestroy():
    if ( fieldModel != [] ):
        for i in range( len(fieldModel) ):
            for j in range( len(fieldModel[0]) ):
                fieldBtns[i][j].destroy()


def gotoMainMenu():
    fieldDestroy()
    gameFr.forget()
    mainMenuFr.pack( expand=True, fill='both' )

# def ask(title, text, okAction, cancelAction, type):
#     if ( type == "okcancel" ):
#         okAction() if mb.askokcancel(title, text) else cancelAction()
#     if ( type == "retrycancel" ):
#         okAction() if mb.askretrycancel(title, text) else cancelAction()


def changeColor(i, j):
    global fieldModel

    n = fieldModel[i][j]
    newColor = n

    if rounds[ currRound ][ 'rndOrderColors' ] == True:
        while newColor == n:
            newColor = random.randint( 0, rounds[ currRound ][ 'numberOfColors' ] - 1 )
    else:
        newColor += 1
        if newColor == rounds[ currRound ][ 'numberOfColors' ]:
            newColor = 0

    fieldModel[i][j] = newColor
    render()


def render():
    global currtime
    #--------Field--------------------
    for i in range( len(fieldModel) ):
        fieldFr.rowconfigure( i, weight=1, minsize = btnSize )
        for j in range( len(fieldModel[0]) ):
            fieldFr.columnconfigure( j, weight=1,  minsize = btnSize )
            fieldBtns[i][j].config(
                bg = colors[ fieldModel[i][j] ]
            )
    #--------InfoText--------------------
    infoTxt.config( text = currStatus )
    showCurrRound.config( text = f'Round: {currRound + 1}' )



#---------------OnClick--------------
def startOnClick():
    startGame()

def btnFieldClick(i, j):
    def btnOnClick(e):
        changeColor(i, j)
        check()
    return btnOnClick
#---------------VisualElements-------

gameFr = Frame( root, bd = 15)
#gameFr.pack( expand=True, fill='both' )
Show = Label(gameFr, text=0)
Show.pack()
t = timer(Show)


menuFr = Frame( gameFr, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( gameFr, bd = 0 )
fieldFr.pack( expand=True, fill='both')

showCurrRound = Label( menuFr, font=('David',12), bg='#DDD')
showCurrRound.pack(anchor='ne')

mainMenuFr = Frame( root, bd = 15)
mainMenuFr.pack( expand=True, fill='both' )

infoTxt = Label(
    menuFr,
    # bg='white',
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




root.resizable(0, 0)

root.mainloop()
