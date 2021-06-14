
#%%
print("import...", "\n")
import os
import numpy as np
import mne
print("done", "\n")

#%%

#read data
print("read data...","\n")

data_path = "D:/Documents/Uni/Master/2.FS/project_work/data/ds003061-download"
misc = ("EXG1", "EXG2", "EXG3", "EXG4", "EXG5", "EXG6", "EXG7", "EXG8")
exclude = ()
data = {}

for i in range(13):
    print(i)
    subs = ("001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011","012", "013")
    subnum = subs[i]
    for k in range(3):
        blocks = ("01", "02", "03")
        block = blocks[k]
        if block == "03" and subnum == "006":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "007":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        else:
            filename = f"sub-{subnum}_task-P300_run-{block}_eeg.bdf"
            data[f"s{subnum}_b{block}"] =  mne.io.read_raw_bdf(f"{data_path}/sub-{subnum}/eeg/{filename}", eog=None, misc=misc, stim_channel='auto', exclude=exclude, preload=False, verbose=None)

print("\n","done","\n")

# %%

# %%
subnum = "001"
block = "01"
events = mne.find_events(data[f"s{subnum}_b{block}"])  
raw = data[f"s{subnum}_b{block}"]


#%%
raw.plot()

epochs = mne.Epochs(raw, events, tmin=-0.3, tmax=0.7,
                    preload=True)

epochs.filter(l_freq=0.1, h_freq=None)
fig = epochs.plot()

print("done")

# %%
reject_criteria = dict(eeg=100e-6)  
epochs.drop_bad(reject=reject_criteria)
epochs.plot_drop_log()

