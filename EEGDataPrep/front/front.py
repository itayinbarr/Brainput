from tkinter import *
from EEGDataPrep.dataprep.dataprep import hello
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='EEG Raw data Processor')
        self.lbl2=Label(win, text='Create plot of Data')
        self.lbl3=Label(win, text='Create processed data')
        self.t1 = Button(win, text='Open a File', command=self.select_file)
        self.t2=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Create plot')
        self.btn2=Button(win, text='Create file')
        self.lbl1.place(x=100, y=70)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Add', command=self.add)
        self.b2=Button(win, text='Subtract')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)

    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )

    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))



