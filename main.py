from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
from Game import *
from MainMenu import *

root.title("NextgenTetris")

menu = None
game = None
dialog = None

menu = MainMenu( root )
menu.show()


def onStartGame(e):
    global game
    menu.hide()
    game = Game( root, round = 1)
    game.show()

def onGameWin(e):
    game.stop()


root.bind('<<Start-Click>>', onStartGame )
root.bind('<<Game_win>>', onGameWin)

root.resizable(0, 0)

root.mainloop()
