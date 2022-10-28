import os
import numpy as np
import mne


def test(file):
    raw = mne.io.read_raw(file)
    raw.compute_psd(fmax=50)
    raw.plot(duration=5, n_channels=30)