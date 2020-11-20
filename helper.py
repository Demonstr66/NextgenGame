from tkinter import *
import time

print('Imported success')
#Этот наш файлик, который мы подключаем в какой-либо проект
# Для наглядности,печатаем это)
# При импорте мы сможем пользоваться всем что располагается в этом файлике,
# в том числе и классами

#Тут все просто - создаем класс
# В данном случае это будет human)
class human(): #Вот так объявляется класс, тут собки должны быть пустыми
               #Вообще туда иногда можно и даже нужно передавать кое что
               #Но об этом не сейчас

    #Это базовый метод, __init__ - так называемый конструктор
    # Само название подсказывает для чего нужен этот метод =)
    # Тут есть один базовый аргумент - self
    # А дальше мы можем указывать любые параметры которые нам нужны

    # self - Это как бы сам экземпляр класса, который будет создан,
    # когда мы наш класс где-нибудь используем
    # например dima = human("dima", 26)
    #Тут мы создали "Экземпляр класса" human и передали туда два параметра
    #Конструктор класса human будет таким
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
        #Эта переменная легко будет доступна из экземпляра класса
        # как для чтения так и для записи

        # Но что если я не хочу то бы кто то менял значения по умолчанию?
        # Например я точно уверен, что все любят фильм аватар
        # Так зачем же нам это менять?
        self.__bestFilm = 'AVATAR'
        #В питоне как я понял нельзя создать приватный атрибут класса,
        # Но двойное подчеркивание в начале названия значительно усложнит
        # изменение для неё. Так например получить значение теперь
        # Можно только через специальную функцию геттер,
        # которая будет возвращаться нам значение
    def getBestFilm(self):
        return self.__bestFilm
    # Методы мы создаем просто обычным способом,как функции
    # только первым аргументом всегда указываем self
    def sayHi(self):
        # Благодаря тому, что мы сохранили первоначальное значение, как атрибут
        # Мы теперь легко можем к нему обратиться
        print(f'Hi, my name is {self.name}')

        # так же мы можем ссылаться на свои же собственные функции
        # через self
        self.printBirthday()

    def printBirthday(self):
        print(f'I was born at {self.birthday}')
