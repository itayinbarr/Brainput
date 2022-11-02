BRAINPUT
==============================

MNE Python based software, for automated EEG data preprocessing.

Getting Started
------------

I recommend storing the raw data files in

`./data/raw`

From within the repo directory run

`./EEGDataPrep/runner.py`

You can now load a file (it has to be a supported type by MNE Python). For a full list of supported file types, 
go to the bottom of the file.

For plotting the raw data, press the Plot Raw button. 

For starting to preprocess the file, press Step One. After it finishes, it loads a plot for you to choose bad channels 
to remove. After clicking on the bad channels, close the plot window and press Step Two.

After pressing step two and the software finishes processing, it loads a plot of the processed epochs to choose 
manually if we see a bad epoch.

When finished, press Save Epochs. You can access the preprocessed file in:  

`./data/preprocessed`

Project Organization
------------

    ├── README.md                    <- The top-level README for developers using this project
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
- unittest
--------
