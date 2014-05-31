from tkinter import *
import menu

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Card Game Title')

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight = 1)
        top.columnconfigure(0, weight = 1)

        self._mainmenu = menu.MainMenu()
        self._mainmenu.grid()

Game().mainloop()
