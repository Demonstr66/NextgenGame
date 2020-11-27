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
