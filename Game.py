from tkinter import *
from config import *
import math, random

from levels import *
from helper import *
from Cell import *


class Game(Frame):
    def __init__(self, master = None, round = 0):
        Frame.__init__( self, master )

        self._round = round
        self._parse( ROUNDS[ self._round ] )
        self._initVisualElements()

    def show(self):
        self.pack( expand=True, fill='both' )

    def hide(self):
        self.forget()


    def _initVisualElements( self ):
        self._status = Label(
            self,
            text = self._status,
            justify = CENTER,
            font = ( 'Arial', 12 ),
            height = 2,
            bg = 'red'
        )
        self._status.pack( fill = 'x' )

        self._bar = Frame( self, bg = 'grey', width = 80)
        self._bar.pack(side = 'left', fill = 'y')
        self._field = GameField(
            self,
            self._row,
            self._col,
            self._numberOfColors,
            self._rndOrderColors
        )
        self._field.show()


    def _parse( self, options ):
        self._row = options['row']
        self._col = options['col']
        self._status = options['status']
        self._timer = options['timer']
        self._rndCellColors = options['rndCellColors']
        self._numberOfColors = options['numberOfColors']
        self._rndOrderColors = options['rndOrderColors']
        self._id = options['id']


class GameField(Frame):
    def __init__( self, master, row, col, maxColor, rndOrder):
        kw = {
            'bd': 8
        }
        Frame.__init__( self, master, kw )

        self._row = row
        self._col = col
        self._max = maxColor
        self._rndOrder = rndOrder
        self._model = self._modelInit()
        self._btns = self._createBtns()

    def show(self):
        self.pack()
    def hide(self):
        self.forget()
    def _modelInit(self):
        model = []
        for i in range( self._row ):
            model.append([])
            for j in range( self._col ):
                code = random.randint( 0, self._max - 1 )
                model[i].append( code )
        return model

    def _createBtns(self):
        field = []
        for i in range( self._row ):
            field.append([])
            for j in range( self._col ):
                cell = Cell( self, max = self._max, rndOrder = self._rndOrder)
                cell.color = self._model[i][j]
                cell.grid( row = i, column = j, sticky = 'nsew' )
                cell.bind(
                    '<Button-1>',
                    self.click(cell, i, j)
                )
                field[i].append( cell )
        return field

    def click(self, c, i, j):
        def r(s):
            self._model[i][j] = c.next()
        return r
