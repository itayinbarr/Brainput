from front.front import MyWindow
from tkinter import *

# Opening Window
window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()