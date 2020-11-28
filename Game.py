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

    def stop(self):
        self._field.on = False

    # def destroy(self):
    #     self._field.destroy()

    def _initVisualElements( self ):
        self._bar = Frame( self, bg = 'grey', width = 80)
        self._bar.pack(side = 'left', fill = 'y')

        self._status = Label(
            self,
            text = self._status,
            justify = CENTER,
            font = ( 'Arial', 12 ),
            height = 2,
            bg = 'red'
        )
        self._status.pack( fill = 'x' )

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
        self.on = True

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
                    self._click(cell, i, j)
                )
                field[i].append( cell )
        return field

    def _click(self, c, i, j):
        def r(s):
            if self.on:
                self._model[i][j] = c.next()
                self._check()
            else:
                c['state'] = DISABLED
        return r

    def _check(self):
        sample = self._model[0][0]
        win = True
        for i in range( self._row ):
            for j in range( self._col ):
                if self._model[i][j] != sample:
                    win = False

        if win:
            self.event_generate('<<Game_win>>')
    def destroy(self):
        for i in range( self._row ):
            for j in range( self._col ):
                self._btns[i][j].destroy()
