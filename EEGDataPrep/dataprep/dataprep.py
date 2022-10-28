import os
import numpy as np
import mne
from copy import deepcopy


# Plot Function
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.plot(duration=4)


# Main processing function
def process_eeg(file):
    raw = mne.io.read_raw(file, preload=True)
    bandpass_filter(raw)


# Bandpass filter function
def bandpass_filter(raw):
    raw.filter(l_freq=1, h_freq=50)
    raw.plot(duration=4)