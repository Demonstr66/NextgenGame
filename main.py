from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
root.title("NextgenTetris")

btnSize = 80
currRound = 1
row = 3
col = 3
colors = ["#f00", "#0f0", "#00f", "#ff0", "#f0f", "#0ff", "#000", "#fff"]
status = ""

fieldModel = []
fieldBtns = []


#def fieldClick(event):
    #for i in range(rowscolumns):
        #for j in range(rowscolumns):    
            #if event.widget == fieldBtns[i][j]:
                #currCode = fieldModel[i][j]
                #currCode += 1                
                #if currCode == len(colors): currCode = 0
                #fieldModel[i][j] = currCode
                #event.widget.config( bg = colors[ currCode ] )
    #check = True
    #sample = fieldModel[0][0]
    #for i in range(rowscolumns):
        
        #for j in range(rowscolumns):
            #if  fieldModel[i][j] != sample: check = False
    
    #if check:
        #global currRound
        #currRound += 1
        #newField()


#def makefield():
    #for i in range(rowscolumns):
        #fieldBtns.append([])
        #fieldFr.rowconfigure(i, weight=1, minsize = btnSize.get())
        #for j in range(rowscolumns):
            #fieldFr.columnconfigure(j, weight=1,  minsize = btnSize.get())  
            
            #colorCode = random.randint(0, len(colors) - 1)
            #fieldModel[i][j] = colorCode
            #btn = Button( fieldFr, bg = colors[ colorCode ])
            
            #btn.grid( row=i, column=j, sticky='nsew')  
            
            #btn.bind('<Button-1>',fieldClick)
            #fieldBtns[i].append( btn )

#def newField():
    #infoTxt.config( text = "WOW!!! YOU WIN!" )
    #answ = mb.askokcancel('YOU WIN!','Start new round?')
    #if answ:
        #btnsDestroy()
        #fieldModel.clear()
        #global rowscolumns
        #rowscolumns = 4
        #fieldModelfill()
        #fieldBtns.clear()
        #makefield()   
        #showcurrRound['text'] = f'currRound:{currRound}'
        #infoTxt['text'] = 'All cells must be the same color'
        
#def btnsDestroy():
    #for i in range(rowscolumns):   
        #for j in range(rowscolumns): 
            #fieldBtns[i][j].destroy()
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
    sample = fieldModel[0][0]
    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            if sample != fieldModel[i][j]:
                return False
    return True
        
def changeColor( w ):
    global fieldModel, fieldBtns, status
    
    for i in range( len(fieldModel) ):
        for j in range( len(fieldModel[0]) ):
            if fieldBtns[i][j] == w:
                fieldModel[i][j] += 1
            if fieldModel[i][j] == len(colors):
                fieldModel[i][j] = 0
    if check():
        status = "WOOOW, YOU WIN!"
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
    
        

gameFr = Frame( root, bd = 15) 
#gameFr.pack( expand=True, fill='both' )

menuFr = Frame( gameFr, bd = 0)
menuFr.pack( expand=True, fill='both' , side='top' )

fieldFr = Frame( gameFr, bd = 0)
fieldFr.pack( expand=True, fill='both')

mainMenuFr = Frame( root, bd = 15) 
mainMenuFr.pack( expand=True, fill='both' )

infoTxt = Label(
    menuFr,
    bg='white',
    justify = CENTER,
    font = ( 'Arial', 12 )
)
infoTxt.pack( padx=0, pady=0)

startBtn = Button(
    mainMenuFr,
    text='start',
    justify= CENTER,
    command = startOnClick,
    height=1, width=10
)
startBtn.pack()

levelsBtn = Button( mainMenuFr, text='levels', justify = CENTER, height = 1, width = 10 )
levelsBtn.pack()

showcurrRound = Label( menuFr, text = f'Round:{currRound}', font=('David',12), bg='#DDD')
showcurrRound.pack(anchor='ne')




root.mainloop()
