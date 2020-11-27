from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()
from Game import *
from MainMenu import *

root.title("NextgenTetris")

app = Game( root, round = 2 )
menu = MainMenu( root )

menu.show()
app.show()

root.resizable(0, 0)

root.mainloop()
