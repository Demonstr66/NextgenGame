from tkinter import *
root = Tk()
root.geometry('400x300')
main = Frame( root, bg = 'green' )
status = Label( main, bg = 'red', text = "Status bar", height = 3 )
status.pack()
bar = Frame( main, bg = 'blue', width = 80)
bar.pack(side = 'right', fill = 'y')

main.pack(expand = True, fill = 'both')
root.mainloop()
