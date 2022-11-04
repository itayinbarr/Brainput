from front.front import MyWindow
from tkinter import *

# Run this file to start the software
# ---------------------------

# Introduction
print("***************************")
print("***************************")
print("***************************")
print("Welcome to BRAINPUT - MNE Python based software, for automated EEG data preprocessing.")
print("---------------------------")
print("I recommend storing the raw data files in data/files")
print("---------------------------")

# You can use the input to load 1 or multiple windows
print("Type down the number of machine windows to open. When finished, press Enter")
numberOfWindows = int(input())
for i in range(numberOfWindows):
    window = Tk()
    mywin = MyWindow(window)
    window.title('BRAINPUT Machine')
    window.geometry("600x350")

window.mainloop()
