import os
import mne
from mne.preprocessing import ICA


# Plotting functions
# ---------------------------
# Plot raw data
def plot_raw(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    raw.plot(duration=4)


# Plot processed data
def plot_processed_file(file):
    data = mne.read_epochs(file, preload=True)
    data.plot()


# Step One functions
# ---------------------------
# Bandpass, high pass, low pass, re-referencing, picking bad channels
def step1(file):
    raw = mne.io.read_raw(file, preload=True)
    # Deleting extra channels for development sake. DELETE AFTER FINISHED
    raw.pick(['Pz', 'Cz', 'Fz', 'C3', 'C4'])
    bandpass_filter(raw)
    rereference(raw)
    print("---------------------------------")
    print("Pick bad channels")
    raw.plot(duration=4)
    return raw


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


# Step One functions
# ---------------------------
# Deleting bad channels picked, Epochs
def step2(raw, file):
    inspect_bads(raw)
    ica_analysis(raw)
    epochs = epoching(raw, True)
    print("---------------------------------")
    print("Pick bad epochs")
    epochs.plot()
    return epochs


# Inspecting bad channels after first filtering phase
def inspect_bads(raw):
    print("---------------------------------")
    if len(raw.info['bads']) > 0:
        raw.pick(picks='eeg', exclude="bads")
        print("Removed bad channels picked in step one")
    else:
        print("No bad channels picked")


# Ephoching & inspect epochs function
def epoching(raw, reject):
    events = mne.make_fixed_length_events(raw, start=5, duration=2.5)
    if reject:
        reject_criteria = dict(eeg=150e-6)  # 250 µV
        return mne.Epochs(raw, events, reject=reject_criteria, tmin=-0.2, tmax=0.5, preload=True)
    else:
        return mne.Epochs(raw, events, tmin=-0.2, tmax=0.5, preload=True)


# ICA analysis
def ica_analysis(raw):
    ica = ICA(method='fastica', max_iter='auto')
    ica.fit(raw)
    return ica.apply(raw)


# Save functions
# ---------------------------
# Saving Epochs
def save_processed_epochs(epochs, file):
    processed_file_name = f"Processed - {file.rsplit('/', 1)[-1].split('.')[0]}-epo.fif"
    epochs.save(fname=processed_file_name, overwrite=True)
    os.rename(processed_file_name, f"../data/preprocessed/{processed_file_name}")

