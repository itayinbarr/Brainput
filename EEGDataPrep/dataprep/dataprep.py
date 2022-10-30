import mne


# Plot Function
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    raw.plot(duration=4)


# Bandpass, high pass, low pass, re-referencing, picking bad channels
def step1(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(["Fz", "Pz", "C3", "C4", "Cz"])
    bandpass_filter(raw)
    rereference(raw)
    print("---------------------------------")
    print("Pick bad channels")
    raw.plot(duration=4)
    return raw


# Deleting bad channels picked, Epochs
def step2(raw, file):
    inspect_bads(raw)
    epochs = epoching(raw)
    processedFileName = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}.fif"
    # raw.save(processedFileName)


# ICA and save processed file
def step3(raw, file):
    processedFileName = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}.fif"
    # raw.save(processedFileName)


# Inspecting bad channels after first filtering phase
def inspect_bads(raw):
    print("---------------------------------")
    if len(raw.info['bads']) > 0:
        raw.pick(picks='eeg', exclude="bads")
        print("Removed bad channels picked in step one")
    else:
        print("No bad channels picked")


# Ephoching function
def epoching(raw):
    events = mne.make_fixed_length_events(raw, start=5, duration=2.5)
    reject_criteria = dict(mag=4000e-15,  # 4000 fT
                           grad=4000e-13,  # 4000 fT/cm
                           eeg=150e-6,  # 150 µV
                           eog=250e-6)  # 250 µV
    return mne.Epochs(raw, events, tmin=-0.2, tmax=0.5, reject=reject_criteria, preload=True)


# Bandpass filter function
def bandpass_filter(raw):
    # Filtering to low-pass and high-pass, picking specific electrodes
    raw.filter(l_freq=1, h_freq=40)
    # Down Sampling
    raw.resample(sfreq=250)
    # Cleaning powerline noise
    freqs = (60, 120, 180, 240)
    raw.notch_filter(freqs=freqs, picks='eeg', method='spectrum_fit', filter_length='4s')


# Re-referenceing function
def rereference(raw):
    raw.set_eeg_reference(ref_channels=['Cz'])
