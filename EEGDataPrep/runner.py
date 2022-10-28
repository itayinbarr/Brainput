from front.front import MyWindow
from tkinter import *

# Opening Window
window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("500x500")
window.mainloop()
