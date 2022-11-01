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
        self.lblStep2 = Label(win, text='Removing bad channels, epoching, inspecting epochs,')
        self.lblStep3 = Label(win, text='ICA & Save processed file')
        # Buttons
        self.btnOpenFile = Button(win, text='Load File', command=self.select_file)
        self.btnRawPlot = Button(win, text='Plot Raw', command=self.create_plot)
        self.btnProcessedPlot = Button(win, text='Plot Processed', command=self.plot_processed)
        self.btnStep1 = Button(win, text='Step One', command=self.first_step)
        self.btnStep2 = Button(win, text='Step Two', command=self.second_step)
        self.btnStep3 = Button(win, text='Save Epochs', command=self.save_epochs)
        # EEG file loaded by user
        self.selectedFile = "No file loaded"
        self.midProcess = mne.create_info(4, sfreq=40)
        self.processed_epochs = mne.create_info(4, sfreq=40)
        self.savedFileName = "Untitled"
        # Placing the objects
        # Labels
        self.lblTitle.place(x=20, y=50)
        self.lblSubtitle.place(x=20, y=90)
        self.lblBtnLeft.place(x=20, y=140)
        self.lblBtnRight.place(x=190, y=140)
        self.lblStep1.place(x=250, y=180)
        self.lblStep2.place(x=250, y=220)
        self.lblStep3.place(x=250, y=240)
        # Buttons
        self.btnOpenFile.place(x=170, y=90)
        self.btnRawPlot.place(x=20, y=180)
        self.btnProcessedPlot.place(x=20, y=220)
        self.btnStep1.place(x=190, y=180)
        self.btnStep2.place(x=190, y=220)
        self.btnStep3.place(x=190, y=280)

    # Triggered when Load File is pressed
    def select_file(self):
        filetypes = (
            ('set files', '*.set'),
            ('BrainVision files', '*.vhdr'),
            ('BrainVision files', '*.vmrk'),
            ('BrainVision files', '*.eeg'),
            ('European data format files', '*.edf'),
            ('BioSemi data format files', '*.bdf'),
            ('General data format files', '*.gdf'),
            ('Neuroscan CNT files', '*.cnt'),
            ('EGI simple binary files', '*.egi'),
            ('EGI MFF files', '*.mff'),
            ('EEGLAB files', '*.set'),
            ('EEGLAB files', '*.fdt'),
            ('Nicolet files', '*.data'),
            ('eXimia EEG data files', '*.nxe'),
            ('Persyst EEG data files', '*.lay'),
            ('Persyst EEG data files', '*.dat'),
            ('Nihon Kohden EEG data files', '*.21e'),
            ('Nihon Kohden EEG data files', '*.pnt'),
            ('Nihon Kohden EEG data files', '*.log'),
            ('Nihon Kohden EEG data files', '*.21e'),
            ('XDF EEG data files', '*.xdf'),
            ('XDF EEG data files', '*.xdfz'),
            ('Elekta NeuroMag data files', '*.fif')
        )
        self.selectedFile = askopenfilename(filetypes=filetypes, title='Open a file')
        if not self.selectedFile:
            messagebox.showerror("Bad File Loaded", "Bad File. Load Again")
        if self.selectedFile:
            print("---------------------------------")
            print(f"{self.selectedFile.rsplit('/', 1)[-1].split('.')[0]}", "selected successfully, click "
                                                                           "Step One to proceed with processing")
            print(self.selectedFile)

    # Triggered when Plot Raw is pressed
    def create_plot(self):
        plot_raw(self.selectedFile)

    # Plot an already-processed file
    def plot_processed(self):
        plot_processed_file(self.selectedFile)

    # Triggered when Step One is pressed
    def first_step(self):
        self.midProcess = step1(self.selectedFile)

    # Triggered when Step Two is pressed
    def second_step(self):
        self.midProcess = step2(self.midProcess, self.selectedFile)

    # Triggered when Load File is pressed
    def save_epochs(self):
        save_processed_epochs(self.midProcess, self.selectedFile)
        print("---------------------------------")
        print("Your preprocessed file is new in data/preprocessed folder.")
