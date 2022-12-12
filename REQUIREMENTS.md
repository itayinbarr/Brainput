App Requirements Document
==============================

## Goals
- Minimize the need to work with code in order to preprocess EEG data in the future.
- Gain experience with developing code related to EEG, using relevant libraries.

Description
------------
A software which engages with the user using a GUI. It allows the user to preprocess the EEG data
before passing it as training datasets.

This software is able to use common practices in order to remove noises and external interruptions 
to the EEG data.
From within the repo directory run

Features
--
- GUI made to minimize using code through the whole preprocessing process.
- Plot the raw data before analysis, as well in the end of the process.
- Remove artifacts using ICA analysis, FIR, bandpass filters, Epoching.
- Inspecting bad channels and epochs throughout the process.
- Saving the preprocessed file.

GUI
--
Simplified, single page. Built using TKInter library, which is prebuilt with Python, hence a solid dependency.

It will contain:
- Title
- Subtitle
- Load file button
- Plot Raw button
- Plot processed button
- Step1, step2 & save buttons
- Labels explaining the steps throughout the preprocessing

Plots
---
Aside from the plots which appear twice throughout the process in order to 
manually inspect the channels and epochs, the user can generate plots of the data.
- Plotting the raw data
- Plotting the preprocessed data

Artifact analysis
---
The methods and functions used in the process are based on MNE-python library, which is open-source
and contains extremely useful pretrained models and tools.

MNE-python is used in a variety of academic institutions.

The majority of knowledge used to build this app is derived from free documents which belong to universities of Ohio 
and Pennsylvania. Other sources were used, like the website of Keras, MNE, 3Blue1Brown

Project Organization
------------

    ├── README.md                    <- The top-level README for developers using this project
    ├── REQUIREMENTS.md              <- App requirements document.
    ├── LICENSE.md                   <- MIT
    ├── .gitignore                   <- For envornment directories
    ├── data                         <- Data directories, containing both raw and preprocessed (recommended to store here)
    │   ├── processed                <- Preprocessed files directory
    │   └── raw                      <- Raw files directory
    │
    ├── EEGDataPrep                  <- Containing the software itself
    │   ├── dataprep                 <- Directory of all functions of the software
    │   │   └── dataprep.py          <- All functions of the software
    │   │
    │   └── front                    <- Directory of GUI code
    │   │   └── front.py             <- Frontend code
    │   │
    │   ├── __init__.py              <- For syntax purposes
    │   └── runner.py                <- Running the software
    │
    └── tests                        <- Tests directory
        └── backend_tests.py         <- Unit tests of backend
 
Dependencies
------------

- Python
- MNE Python
- TKInter
--------
