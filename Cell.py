from tkinter import *
from config import *
import math, random

class Cell(Button):
    def __init__(self, master = None, **kw):
        kw = self._parse(kw)
        kw.update({
            'image': pixelVirtual,
            'width': BTN_S,
            'height': BTN_S,
            'compound': CENTER
        })
        Button.__init__( self, master, kw)

        self.color = 0
        self._update()
    def _color():
        doc = 'The code of color property.'
        def fget(self):
            return self._color
        def fset(self, value):
            self._color = value
            if self._color >= self._max:
                self._color -= self._max
            self._update()
        return locals()
    color = property(**_color())

    def next(self, e = None):
        newColor = self.color
        if self._rndOrder:
            while newColor == self.color:
                newColor = random.randint( 0, self._max - 1 )
        else:
            newColor += 1
        self.color = newColor

        return self.color

    def _update(self):
        color = COLORS[ self.color ]
        self['bg'] = color

    def _parse(self, kw):
        try:
            self._max = int( kw.pop( 'max' ) )
        except ValueError:
            raise ValueError(f'max must be INT value') from None
        except KeyError:
            self._max = len(COLORS)

        try:
            self._rndOrder = bool( kw.pop( 'rndOrder' ) )
        except ValueError:
            raise ValueError(f'rndOrder must be BOOLEAN value') from None
        except KeyError:
            self._rndOrder = False
        return kw
