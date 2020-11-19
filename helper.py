from tkinter import *
import time

print('Imported success')
#Этот наш файлик, который мыподключаемв какой-либо проект
# Для наглядности,печатаем это)
# При импорте мы сможем пользоваться всем чторасполагается в этом файлике,
# в том числе и классами

#Тут все просто - создаем класс
# В данномслучае это будет human)
class human(): #Вот так объявляется класс, тут собки должны быть пустыми
               # Вообще туда иногдаможно и даже нужно передавать кое что
               # Но об этом не сейчас

    #Это базовый метод, __init__ - так называемый конструктор
    # Само название подсказывает для чего нужен этот метод =)
    # Тут есть один базовый аргумент - self
    # А дальше мы можем указывать любые параметры которые нам нужны

    # self - Это как бы сам экземпляр класса, который будет создан,
    # когда мы наш класс где-нибудь используем
    # например dima = human("dima", 26)
    #Тут мы создали "Экземпляр класса" human и передали туда два параметра
    # конструктор класса human в этом случае бы выглядел так
    # __init__(self, name, age)


    def __init__(self, name, age):

        #Атрибуты класса практически то же самое, что обычные переменные
        # Только объявляются вот так
        # Тут мы объявдем атрибут name и присваеваем ему значение
        # которое будет передано
        self.name = name
        self.age = age

        #а тут мы просто создаем новую переменную
        self.birthday = "06.01.1994"
        #Эта переменная легко будет доступнаиз экземпляра класса
        # как для чтения так и для записи

        # Но что если я не хочу то бы кто то менял значения по умолчанию?
        # Например я точно уверен, что все любят аватар
        # Так зачем же нам это менять?
        self.__bestFilm = 'AVATAR'
        #В питоне как я понял нельзя создать приватный атрибут класса,
        # Но двойное подчеркивание в начале названия значительно усложнит
        # Работу с ней. Так например получить значение теперь

    def getBestFilm(self):
        return self.__bestFilm
    # Методы мы создаем просто обычным способом,
    # только первым аргументом всегда указываем self
    def sayHi(self):
        # Благодаря тому, что мы сохранили первоначальное значение, как атрибут
        # Мы теперь легко можем к нему обратиться
        print(f'Hi, my name is {self.name}')

        # так эе мы можем ссылаться на свои же собственные функции
        # через self
        self.printBirthday()

    def printBirthday(self):
        print(f'I was born at {self.birthday}')






class timer():
    def __init__(self, root):
        self.root = root
        self.label = Label( self.root, text="")
        self.label.pack()
        self.n = 0
        self.update_clock()

    def update_clock(self):
        self.n += 1
        print(self.n)
        self.label.configure(text=self.n)
        self.root.after(1, self.update_clock)
