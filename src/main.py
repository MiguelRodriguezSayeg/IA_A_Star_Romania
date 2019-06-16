from tkinter import Tk
from romania import RomaniaMap
from gui import MainApplication
from agent import Agent

root = Tk()

app = MainApplication(root,Agent(RomaniaMap()))
root.mainloop()