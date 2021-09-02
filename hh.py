from tkinter import Tk, Frame, BOTH
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.create_menu()

    def create_menu(self):
        self.pack(fill=BOTH, expand=1)
        
