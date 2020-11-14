from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
root.title("NextgenTetris")


btnSize = 80
currRound = 0
currStatus = ""

colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]
rounds = [
    {
        'id': 1,
        'row': 2, 'col': 2,
        'status': 'All cells must be the same color! 1',
        'timer': None,
        'rndColorOfCell': False, # Or timer
        'rndOrderColors': False,
        'numberOfColors': 3
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
        'status': 'All cells must be the same color! 3',
        'timer': None,
        'rndColorOfCell': False, # Or timer
        'rndOrderColors': False,
        'numberOfColors': 8
    },
]

fieldModel = []
fieldBtns = []


#---------------RefactoringFunc------
def startGame():
    mainMenuFr.forget()
    gameFr.pack( expand=True, fill='both' )

    newRound( currRound )
    render()

def newRound( round ):
    global fieldModel, fieldBtns, currStatus

    row = rounds[ currRound ][ 'row' ]
    col = rounds[ currRound ][ 'col' ]

    fieldModel = modelInit( row, col, rounds[ currRound ][ 'numberOfColors' ] )
    fieldBtns = createField( row, col )

    currStatus = rounds[ currRound ][ 'status' ]
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

    if (win):
        currStatus = "WOOW!! YOU WIN!"
        currRound += 1

        typeModal = "okcancel"
        if ( currRound == len(rounds) ):
            typeModal = "retrycancel"
            currRound = len(rounds) - 1
        ask('YOU WIN!', 'Start new round?', nextLevel, gotoMainMenu, typeModal)

def fieldDestroy():
    if ( fieldModel != [] ):
        for i in range( len(fieldModel) ):
            for j in range( len(fieldModel[0]) ):
                fieldBtns[i][j].destroy()


def gotoMainMenu():
    fieldDestroy()
    gameFr.forget()
    mainMenuFr.pack( expand=True, fill='both' )

def ask(title, text, okAction, cancelAction, type):
    if ( type == "okcancel" ):
        okAction() if mb.askokcancel(title, text) else cancelAction()
    if ( type == "retrycancel" ):
        okAction() if mb.askretrycancel(title, text) else cancelAction()

# def changeColor( w ):
#     global fieldModel, fieldBtns
#
#     for i in range( len(fieldModel) ):
#         for j in range( len(fieldModel[0]) ):
#             if fieldBtns[i][j] == w:
#                 fieldModel[i][j] += 1
#             if fieldModel[i][j] == len(colors):
#                 fieldModel[i][j] = 0
#     render()

def changeColor(i, j):
    global fieldModel
    if rounds[ currRound ][ 'rndOrderColors' ] == False:
        fieldModel[i][j] += 1
        if fieldModel[i][j] == rounds[ currRound ][ 'numberOfColors' ]:
            fieldModel[i][j] = 0
    else:
        n = fieldModel[i][j]
        newColor = n
        print('n', n)
        while newColor == n:
            newColor = random.randint( 0, rounds[ currRound ][ 'numberOfColors' ] - 1 )
            print("While:", n, newColor)
        fieldModel[i][j] = newColor

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
    infoTxt.config( text = currStatus )
    showcurrRound.config( text = f'Round: {currRound + 1}' )

#---------------OnClick--------------
def startOnClick():
    startGame()

# def fieldOnClick(e):
#     changeColor( e.widget )
#     check()

def btnFieldClick(i, j):
    def btnOnClick(e):
        changeColor(i, j)
        check()
    return btnOnClick
#---------------VisualElements-------

gameFr = Frame( root, bd = 15)
#gameFr.pack( expand=True, fill='both' )

menuFr = Frame( gameFr, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( gameFr, bd = 0)
fieldFr.pack( expand=True, fill='both')

showcurrRound = Label( menuFr, font=('David',12), bg='#DDD')
showcurrRound.pack(anchor='ne')

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



root.update_idletasks()

root.mainloop()
