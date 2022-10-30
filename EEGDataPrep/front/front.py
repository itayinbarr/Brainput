from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from EEGDataPrep.dataprep.dataprep import *


class MyWindow:
    def __init__(self, win):
        # Creating the visuals
        # Labels
        self.lblTitle = Label(win, font="Helvetica 16 bold", text='EEG Raw data Processor')
        self.lblSubtitle = Label(win, text='Choose your EEG data')
        self.lblBtnLeft = Label(win, font="Helvetica 14 bold", text='Create plots from file')
        self.lblBtnRight = Label(win, font="Helvetica 14 bold", text='Process Your File')
        self.lblStep1 = Label(win, text='Bandpass, re-referencing & Channel inspection')
        self.lblStep2 = Label(win, text='Removing bad channels, epoching & Inspecting epochs')
        self.lblStep3 = Label(win, text='ICA & Save processed file')
        # Buttons
        self.btnOpenFile = Button(win, text='Load File', command=self.select_file)
        self.btnRawPlot = Button(win, text='Create plot', command=self.create_plot)
        self.btnStep1 = Button(win, text='Step One', command=self.first_step)
        self.btnStep2 = Button(win, text='Step Two', command=self.second_step)
        # EEG file loaded by user
        self.selectedFile = "No file loaded"
        self.midProcess = mne.create_info(4, sfreq=40)
        # Placing the objects
        # Labels
        self.lblTitle.place(x=20, y=50)
        self.lblSubtitle.place(x=20, y=90)
        self.lblBtnLeft.place(x=20, y=140)
        self.lblBtnRight.place(x=190, y=140)
        self.lblStep1.place(x=250, y=180)
        self.lblStep2.place(x=250, y=220)
        self.lblStep3.place(x=250, y=260)
        # Buttons
        self.btnOpenFile.place(x=170, y=90)
        self.btnRawPlot.place(x=20, y=180)
        self.btnStep1.place(x=190, y=180)
        self.btnStep2.place(x=190, y=220)

    def select_file(self):
        filetypes = (
            ('set files', '*.set'),
            ('All files', '*.*')
        )
        self.selectedFile = askopenfilename(filetypes=filetypes, title='Open a file')
        if not self.selectedFile:
            messagebox.showerror("Bad File Loaded", "Bad File. Load Again")
        if self.selectedFile:
            print("---------------------------------")
            print(f"{self.selectedFile.rsplit('/', 1)[-1].split('.')[0]}", "selected successfully, click "
                                                                           "Step One to proceed with processing")

    def create_plot(self):
        plot_raw(self.selectedFile)

    def first_step(self):
        self.midProcess = step1(self.selectedFile)

    def second_step(self):
        step2(self.midProcess, self.selectedFile)
