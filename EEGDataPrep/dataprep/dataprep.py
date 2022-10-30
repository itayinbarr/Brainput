import mne

# Plot Function
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    raw.plot(duration=4)
    print(raw.info)


# Bandpass, high pass, low pass, re-referencing, picking bad channels
def step1(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    bandpass_filter(raw)
    rereference(raw)
    print("Pick Bad Channels")
    raw.plot(duration=4)
    return raw

# Deleting bad channels picked, Epochs
def step2(raw, file):
    inspect_bads(raw)
    processedFileName = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}.fif"
    # raw.save(processedFileName)


# Inspecting bad channels after first filtering phase
def inspect_bads(raw):
    if len(raw.info['bads']) > 0:
        raw.pick(picks='eeg', exclude="bads")
        print("removed bad channels")
    print("Removed bad channels picked in step one")
    raw.plot(duration=4)



# Bandpass filter function
def bandpass_filter(raw):
    # Filtering to low-pass and high-pass, picking specific electrodes
    raw.filter(l_freq=1, h_freq=40, filter_length="4s")
    # Down Sampling
    raw.resample(sfreq=200)
    # Cleaning powerline noise
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='4s')


# Re-referenceing function
def rereference(raw):
    raw.set_eeg_reference(ref_channels=['Cz'])
