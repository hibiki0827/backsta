# Data analyses

Provide readers/users with a general outline of the conducted analyses and corresponding outcomes.

## Overview


### 1. filtering

* exclude Fp1 -> bad channel
* filtering data with: low freq: 1Hz, high freq: 50Hz 
* eeg reference: "average"

### 2. ICA

* fit ica on a copy of the data
* ica ran with 15 components
* take blink templates from participant 01 block 01
* automatic detection and exclusion of blink component -> threshold 0.85

### 3. averaging

## Outcomes

### ICA components

[comp_plots.pdf](https://github.com/hibiki0827/backsta/files/6950452/comp_plots.pdf)



