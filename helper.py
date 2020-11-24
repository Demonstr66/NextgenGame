from tkinter import *
import time

print('Imported success')


class timer():

    def __init__(self, widget, maxtime, endAct = None, endArgs = None):
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
    def _check(self):
        if self.on == True:
            self.widget.after(self.delay , self._tick)
    def _tick(self):
        if (self.time < self.maxtime) and (self.on != False):
            self.time += self.delay
            print(self.time)
            self.widget.config(text = self.time // 1000)
            self._check()
        elif self.time >= self.maxtime:
            self.endAct()
