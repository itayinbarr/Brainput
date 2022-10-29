import mne


# Plot Function
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    raw.plot(duration=4)


# Main processing function
def process_eeg(file):
    raw = mne.io.read_raw(file, preload=True)
    bandpass_filter(raw)
    raw.plot(duration=4)
    processedFileName = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}.fif"
    # raw.save(processedFileName)


# Bandpass filter function
def bandpass_filter(raw):
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    # Filtering to low-pass and high-pass, picking specific electrodes
    raw.filter(l_freq=0.05, h_freq=40, filter_length="4s")
    # Down Sampling
    mne.Info
    raw.resample(sfreq=200)
    # Cleaning powerline noise
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='3s')
