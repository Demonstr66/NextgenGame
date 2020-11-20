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
        'timer': None,
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


#---------------RefactoringFunc------
def startGame():
    mainMenuFr.forget()
    gameFr.pack( expand=True, fill='both' )
    newRound( currRound )
    render()

    #------------------------------------------------------LESSON
    # Тут я покажу как использовать наш класс,
    # когда будет вызвана функция startGame
    # Мы создадим меня)))

    #Как видишь, тут только 2 аргумента, self пропускаем
    # Если бы у нас в конструкторе был только self
    # То тут вызывали бы так human()
dima = human('Dima', 26)
    # теперь dima - это экземпляр класса human и обладает всеми
    # его методами и атрибутами

    # Теперь я поздороваюсь
print('ex N:____1')
dima.sayHi()
print('#------------------------------')

    # Но что если мне нужно только имя?
    # легко
print('ex N:____2')
print(dima.name)
print('#------------------------------')

    # Теперь создадим тебя
leha = human('Alex', 14)

    # Здоровайся
print('ex N:____3')
leha.sayHi()
print('#------------------------------')
    # Выведется
    # Hi, my name is Alex
    # I was born at 06.01.1994

    # Стоп стоп стоп, это же не твоя дата рождения
    # верно, тк дату рождения мы статично присваиваем в классе всем одинаковою
    # но это не беда
leha.birthday = "30.09.2006"

    # Вот теперь скажи привет
print('ex N:____4')
leha.sayHi()
print('#------------------------------')
    # Теперь все гуд

    # А что тамс любимым фильмом?
    # print(leha.__bestFilm)
    #Можешь расскоментироватьи попробовать - будет ошибка

    #А вот так норм
print('ex N:____5')
print(leha.getBestFilm())
print('#------------------------------')

    # Конечно это не помешает нам сделать вот так
leha.__bestFilm = 'Titanik'
print('ex N:____6')
print(leha.__bestFilm)
print('#------------------------------')


    # Но это не изменит внутреннее значение
    # Поэтому когда мы захотим узнать
    # Какой ты фильм любишь по настоящему
    # Мы вызываем опять геттер и видим изначальный результат
print('ex N:____7')
print(leha.getBestFilm())
print('#------------------------------')

    # Может не очень понятно зачем защищать некоторые переменные или методы
    # от перезаписи, попробую объяснить на примере
    # Создадим ребенка,тк дети тоже люди воспользуемся уже готовым классом
baby = human('Masha', 1)

    # Маше всего 1 год, пусть поздоровается с нами
    # Но мы помним, что дату рождения надо изменить
baby.birthday = "01.01.2020"
print('ex N:____8')
baby.sayHi()
print('#------------------------------')

    # Вроде все ок, но как то слишком внятно она говорит для младенца
    # Изменим это. Благодаря тому, что метод sayHi не защищен от перезаписи
    # Мы легко можем это сделать
baby.sayHi = lambda: print('agu agu agu')
print('ex N:____9')
baby.sayHi()
print('#------------------------------')

    # Так что любые незащащенные методы и атрибуты мы можем переписать.
    # Это называется переопределить метод или перегрузить
    # И если это большой проект,то мы можем и не знать
    # переопределял метод кто то до нас или нет.
    # Или какие то внутренние функции будут ссылаться на измененную функцию
    # а она уже будет делать что то новое
    # например вернемся ко мне
    # и переопределим метод который печатает вторую строчку
dima.printBirthday = lambda: print('bla bla bla')
    # а теперь представь, что я в армии. Ко мне подходит генерал и говорит
    # "Солдат, ты кто? Когда родился"
    # А я отвечаю
print('ex N:____10')
dima.sayHi()
print('#------------------------------')
    # Упс, как не удобно получилось)
    # Что бытаких моментов избегать как раз и надо защищать некоторые методы
    # или атрибуты.
    # А теперь попробуй в классе human изменить название метода на
    # __printBirthday
    # и тогда такой неловкой ситуации не будет)
    # Вроде все

    #------------------------------------------------------LESSON
def newRound( round ):
    global fieldModel, fieldBtns, currStatus

    row = rounds[ currRound ][ 'row' ]
    col = rounds[ currRound ][ 'col' ]

    fieldModel = modelInit( row, col, rounds[ currRound ][ 'numberOfColors' ] )
    fieldBtns = createField( row, col )

    currStatus = rounds[ currRound ][ 'status' ]

    time = rounds[ currRound ][ 'rndColorOfCell' ]
    if ( time ):
        fieldFr.after( time, rndChangeColor)
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
