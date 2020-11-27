from tkinter import *

class MainMenu(Frame):
    """Game main menu"""
    def __init__(self, master = None, **kw):
        kw.update({
            'bd': 15
        })
        Frame.__init__( self, master, kw)


        self._title = Label(
            self,
            text='Welcome to Nextgen Game!',
            justify=CENTER,
            font=('Comic Sans MS', 14)
        )
        self._title.pack()
        self._startBtn = MenuButton(self, text = "Start")
        self._levelsBtn = MenuButton(self, text = "Levels")

    def show(self):
        self.pack()
    def hide(self):
        self.forget()

class MenuButton(Button):
    def __init__(self, master, **kw):
        kw.update({
            'justify': CENTER,
            'height': '1', 'width': '10',
            'bg': 'darkblue',
            'fg': 'white',
            'font': ('Comic Sans MS', 14)
        })
        Button.__init__(self, master, kw)
        self.pack()
