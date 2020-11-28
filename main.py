from tkinter import *
import random
from tkinter import messagebox as mb

root = Tk()

from Game import *
from MainMenu import *

root.title("NextgenTeteris")

class App():
    def __init__( self, master ):
        self._menu = None
        self._game = None
        self._dialog = None
        self._round = 0
        self._menu = MainMenu( root )
        self._menu.show()

        master.bind( '<<Start-Click>>', self._onStartGame )
        master.bind( '<<Game_win>>', self._onGameWin)

    def _onStartGame( self, e = None ):
        self._startRound()

    def _onNextRound(self):
        if len(ROUNDS) - 1 != self._round:
            self._round += 1
        self._startRound()

    def _onGameWin( self, e = None ):
        self._game.stop()

        self._dialog = Ask(
            "You win!",
            "Start next Level?",
            self._onNextRound,
            self._toMainMenu,
            "ok"
        )
        self._dialog.show()

    def _toMainMenu(self):
        self._game.destroy()
        self._menu.show()

    def _startRound(self):
        self._menu.hide()
        if self._game:
            self._game.hide()
            self._game.destroy()
        self._game = Game( root, round = self._round )
        self._game.show()



app = App(root)

root.resizable(0, 0)

root.mainloop()
