from tkinter import *
from tkinter import messagebox as mb
import time

print('Imported success')

class ask():
    """Call messagebox"""

    def __init__(self, title,  text, okAction, cancelAction, type):
        self.title = title
        self.text = text
        self.okAction = okAction
        self.cancelAction = cancelAction
        self.type = type
    def create(self):
        if ( self.type == "askokcancel" ):
            self.okAction() if mb.askokcancel(self.title, self.text) else self.cancelAction()
        if ( self.type == "askretrycancel" ):
            self.okAction() if mb.askretrycancel(self.title, self.text) else self.cancelAction()

















class timer():

    def __init__(self, widget, maxtime = 0, endAct = None, endArgs = None):
        self.on = False
        self.delay = 10
        self.maxtime = maxtime
        self.time = None
        self.widget = widget
        self.endAct = endAct
        self.endArgs = endArgs
    def start(self):
        self.on = True
        self.time = 0
        self._tick()
        return self.time
    def stop(self):
        self.on = False
        self.time = 0
        return(self.time)
    def _check(self):
        if self.on == True:
            self.widget.after(self.delay , self._tick)
    def _tick(self):
        if (self.time < self.maxtime) and (self.on != False):
            self.time += self.delay
            self.widget.config(text = self.time // 1000)
            self._check()
        elif self.time >= self.maxtime:
            self.endAct()


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
