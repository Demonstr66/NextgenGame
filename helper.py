from tkinter import *
import math, random
from config import *
from levels import ROUNDS

class Timer(Label):
    def __init__(self, master = None, **kw):
        kw = self._parse( kw )
        Label.__init__(self, master, kw)

        self._on = False
        self._ups = 10
        self._dalay = 1000 // self._ups
        self._setText(0)

    def start(self):
        self._currTime = 0
        self._k = 1

        if self._limit:
            self._currTime = self._limit
            self._k = -1

        self._on = True
        self._tick()

    def end(self):
        self._on = False

    @property
    def time(self):
        doc = 'The time property. Return current time or None if timer off'
        return self._currTime

    def _parse(self, kw):
        try:
            self._limit = int( kw.pop( 'limit' ) )
        except ValueError:
            raise ValueError(f'limit must be INT value') from None
        except KeyError:
            self._limit = None

        return kw

    def _tick(self):
        if self._on:
            self._currTime += self._k * ( self._dalay )
            self.after( self._dalay, self._tick )
            if self._k < 0: self._limitter()
            self._setText( self._currTime )

    def _limitter(self):
        if self._currTime <= 0:
            self.end()
            self.event_generate('<<Time_out>>')

    def _setText(self, time):
        if self._on:
            if self._k < 0: time = math.ceil( time / 1000 )
            else: time = math.floor( time / 1000 )
        minute = time // 60 % 100
        second = time % 60

        minute = str(minute).rjust(2, '0')
        second = str(second).rjust(2, '0')

        self['text'] = f'{minute} : {second}'
