# Data analyses

for details please download the [script](https://github.com/hibiki0827/backsta/blob/master/project/backsta.py)

## general information

* main analysis:
  * mne python
* other packages used:
  * os
  * numpy as np
  * pandas
  * matplotlib.pyplot
  * csv
  * pickle

## Overview


### 1. reading in the data & filtering

* montage: standard 10 -20 system
* 64 electrodes + misc -> misc channels excluded
* subject names : 001 - 013
* blocks 01 - 03
* exclude Fp1 -> bad channel - Fp1 seemed to be locaded at a wrong position (somewhere posterior)
* filtering data with: low freq: 1Hz, high freq: 50Hz 
* eeg reference set to "average"
* filtered data was saved as "s{subnum}_b{block}-raw.fif"

### 2. ICA

* fit ica on a copy of the data
* ica ran with 15 components
* ICA saved as: "s{subnum}_b{block}-ica.fif"
* take blink templates from participant 01 block 01  (vertical and horizontal eye movements)
* automatic detection and labeling of blink components using corrmap -> threshold 0.85
* appyling the ica
* data with applied ICA saved as "s{subnum}_b{block}-raw.fif" in a different folder than the filtered raw data

### 3. averaging

* making epochs based on events
* events taken into account:
  *  standard
  *  target 
  *  non target
* other events
  *  response 
  *  no response
* conditions:
  * standard
  * target
  * non target
  * firt repetition after deviant
  * last repetition after deviant
* averages made for each participant in each condition  and saved into dictionaries
* averages were turned into lists and saved using pickle
* grand average calculated and plotted using mne.grand_average

## Outcomes

### csv excluded components

[list](https://github.com/hibiki0827/backsta/blob/master/project/excludedcomp.csv)

### ICA components

[comp_plots.pdf](https://github.com/hibiki0827/backsta/files/6950452/comp_plots.pdf)

## Script

[analysis script](https://github.com/hibiki0827/backsta/blob/master/project/backsta.py)



