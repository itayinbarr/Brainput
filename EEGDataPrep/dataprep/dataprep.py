import mne


# Plot Function
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    raw.plot(duration=4, n_channels=5)


# Main processing function
def process_eeg(file):
    raw = mne.io.read_raw(file, preload=True)
    bandpass_filter(raw)
    # raw.save('Processed EEG Data.fif')
    raw.plot(duration=4)



# Bandpass filter function
def bandpass_filter(raw):
    raw.drop_channels(['Fp1', 'F3', 'F7', 'Below Eye', 'FC5', 'FC1', 'T7', 'Left Mastoid', 'CP5', 'CP1', 'P3', 'P7', 'O1', 'Oz', 'O2', 'P4', 'P8', 'Right Mastoid', 'CP6', 'CP2', 'T8', 'Above Eye', 'FC6', 'FC2', 'F4', 'F8', 'Fp2', 'AF7', 'AF3', 'AFz', 'F1', 'F5', 'FT7', 'FC3', 'FCz', 'C1', 'C5', 'TP7', 'CP3', 'P1', 'P5', 'PO7', 'PO3', 'POz', 'PO4', 'PO8', 'P6', 'P2', 'CP4', 'TP8', 'C6', 'C2', 'FC4', 'FT8', 'F6', 'F2', 'AF4', 'AF8', 'Empty', 'EKG', 'AudioOutput'])
    # Filtering to low-pass and high-pass, picking specific electrodes
    raw.filter(l_freq=1, h_freq=40, filter_length="4s")
    # Down Sampling
    raw.resample(sfreq=200)
    # Cleaning powerline noise
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='3s')
