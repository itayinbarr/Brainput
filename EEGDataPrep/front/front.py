from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


class MyWindow:
    def __init__(self, win):
        # Creating the visuals
        # Labels
        self.lblTitle = Label(win, font="Helvetica 16 bold", text='EEG Raw data Processor')
        self.lblSubtitle = Label(win, text='Choose your EEG data')
        self.lblBtnLeft = Label(win, font="Helvetica 12 bold", text='Create plot from file')
        self.lblBtnRight = Label(win, font="Helvetica 12 bold", text='Process Your File')
        # Buttons
        self.btnOpenFile = Button(win, text='Load File', command=self.select_file)
        self.btnLeft = Button(win, text='Create plot', command=self.add)
        self.btnRight = Button(win, text='Process file', command=self.add)
        # EEG file loaded by user
        self.selectedFile = "No file loaded"
        # Placing the objects
        # Labels
        self.lblTitle.place(x=100, y=70)
        self.lblSubtitle.place(x=100, y=110)
        self.lblBtnLeft.place(x=100, y=180)
        self.lblBtnRight.place(x=300, y=180)
        # Buttons
        self.btnOpenFile.place(x=100, y=140)
        self.btnLeft.place(x=100, y=220)
        self.btnRight.place(x=300, y=220)

    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        self.selectedFile = askopenfilename(filetypes=filetypes, title='Open a file')
        if not self.selectedFile:
            messagebox.showerror("Bad File Loaded", "Bad File. Load Again")

    def add(self):
        messagebox.showinfo("Selected File", self.selectedFile)
