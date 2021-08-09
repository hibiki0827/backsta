
#%%
'''
Summerterm 2021, Marburg University

Erika Tsumaya

last time modified 09.08.2021

'''
#%%
print("import...", "\n")

import os
import numpy as np
import mne
import scipy
import pandas
import matplotlib.pyplot as plt
from mne.preprocessing import ICA, corrmap
import csv
import pickle

print("done", "\n")
#%%
#mne.sys_info()
#%matplotlib widget
#data[f"s{subnum}_b{block}"].plot(n_channels= len(data[f"s{subnum}_b{block}"].ch_names), scalings= dict(eeg=100e-6));
#%%
'''
data path, subject number, excluded channels etc.

13 participants, 3 blocks

blink templates taken from s001_01

'''

print("read data...","\n")

data_path = "D:/Documents/Uni/Master/2.FS/project_work/data/ds003061-download"
subs = ("001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011","012", "013")
blocks = ("01", "02", "03")
exclude = ["EXG1", "EXG2", "EXG3", "EXG4", "EXG5", "EXG6", "EXG7", "EXG8", "Erg1", "Erg2", "Plet", "GSR1", "GSR2", "Resp", "Temp"]
montage = mne.channels.make_standard_montage(kind="standard_1020")
data = {}

#blink templates taken from s001_b01
blink_up = np.array(
    [9.27232148e-01,  6.88029640e-01,  5.36014083e-01,  2.06996308e-01,
     1.71720814e-01,  1.32454037e-01,  4.95864143e-02, -1.70251330e-01,
     -1.07496435e-01, -5.46747800e-02, -7.71291430e-03, -1.47149995e-01,
     -1.56361445e-01, -1.85272168e-01, -2.35943771e-01, -2.57900767e-01,
     -2.19778203e-01, -2.02909735e-01, -2.02559648e-01, -2.53258240e-01,
     -2.44054884e-01, -2.57069098e-01, -2.66091388e-01, -3.73519464e-01,
     -3.16921066e-01, -2.82894408e-01, -3.40218685e-01, -3.62830139e-01,
     -3.44898350e-01, -2.94982183e-01, -2.45050874e-01, -2.04689998e-01,
     1.09887898e+00,  1.16700095e+00,  1.17248381e+00,  7.64162094e-01,
     5.83467262e-01,  2.18552982e-01,  2.75549989e-01,  3.60570287e-01,
     4.52480026e-01,  5.44292646e-01,  9.91249833e-02,  3.64920556e-02,
     5.20339434e-02,  9.94234389e-03,  3.04339454e-04, -1.29312145e-01,
     -1.09688325e-01, -1.18726063e-01, -1.25641485e-01, -1.62974611e-01,
     -2.35786630e-01, -2.05318504e-01, -1.98679539e-01, -1.88798386e-01,
     -2.36257533e-01, -2.40695987e-01, -2.60032244e-01, -3.00619674e-01,
     -3.32267387e-01, -3.24114397e-01, -2.97971669e-01, -3.45995592e-01]
     )


blink_side = np.array([-0.33922854, -0.62536674, -0.2830531 , -0.12686595, -0.2495228 ,
       -0.39664488, -0.58496531, -0.43122263, -0.33485414, -0.20302252,
       -0.10771165, -0.07851789, -0.13151675, -0.19602348, -0.24987198,
       -0.16311459, -0.11886555, -0.07255183, -0.04736974, -0.04975024,
       -0.04906283, -0.0737508 , -0.0591185 , -0.12331506, -0.08030168,
       -0.04041821, -0.02540602,  0.02492581,  0.03376099,  0.01634087,
        0.00409601, -0.00914933,  0.02053277,  0.26352692,  0.66990746,
        0.28182251, -0.01023313, -0.01652596,  0.08786898,  0.22608648,
        0.41579777,  0.68082451,  0.48098485,  0.39111475,  0.19971894,
        0.06602516, -0.02521904, -0.01370518,  0.04002649,  0.10972991,
        0.20794667,  0.28013455,  0.17792816,  0.11525115,  0.05290126,
        0.01187765,  0.00111259,  0.01038832,  0.05511766,  0.1273169 ,
        0.12348581,  0.05561234,  0.0288663 ,  0.05521555])


print("\n","done","\n")

#%%

'''
read in raw files

filtering: low 0.1, high 50

sub 06 block 03, sub 07 block 01 do not exist

'''

for i in range(13):
    subnum = subs[i]
    for k in range(3):
        block = blocks[k]
        if block == "03" and subnum == "006":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "007":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        else:
            filename = f"sub-{subnum}_task-P300_run-{block}_eeg.bdf"
            data[f"s{subnum}_b{block}"] =  mne.io.read_raw_bdf(f"{data_path}/sub-{subnum}/eeg/{filename}", eog=None, stim_channel='auto', exclude=exclude, preload=True, verbose=None)
            types = ["eeg" if ch != "Status" else "stim" for ch in data[f"s{subnum}_b{block}"].ch_names]
            data[f"s{subnum}_b{block}"].set_channel_types(dict(zip(data[f"s{subnum}_b{block}"].ch_names, types)))
            data[f"s{subnum}_b{block}"].set_montage(montage)
            data[f"s{subnum}_b{block}"].info["bads"] = ["Fp1"] 
            data[f"s{subnum}_b{block}"].interpolate_bads(mode="accurate")
            data[f"s{subnum}_b{block}"].filter(l_freq=0.1, h_freq=50.0)
            data[f"s{subnum}_b{block}"].set_eeg_reference("average")
            print("\n",f"participants{subnum} block{block} done","\n")
            data[f"s{subnum}_b{block}"].save(f"{data_path}/rawfilter/s{subnum}_b{block}-raw.fif", overwrite=True)
            print("\n",f"participants{subnum} block{block} saved as 's{subnum}_b{block}-raw.fif'","\n")

print("\n","... all done","\n")



#%%
'''
ICA fitting

'''

data_ICA = {}
data_ICA_copy = {}

for i in range(13):
    subnum = subs[i]
    for k in range(3):
        block = blocks[k]
        if block == "03" and subnum == "006":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "007":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        else:
            filename = f"s{subnum}_b{block}-raw.fif"
            data_ICA[f"s{subnum}_b{block}"] = mne.io.read_raw_fif(f"{data_path}/rawfilter/{filename}", preload=True)
            #data_ICA[f"s{subnum}_b{block}"].set_eeg_reference("average")
            data_ICA_copy[f"s{subnum}_b{block}"] = data_ICA[f"s{subnum}_b{block}"].copy()
            data_ICA_copy[f"s{subnum}_b{block}"].filter(l_freq=1.0, h_freq=None)
            ica = ICA(n_components=15, max_iter='auto', random_state=97)
            ica.fit(data_ICA_copy[f"s{subnum}_b{block}"], reject=dict(eeg=250e-6))
            ica.save(f"{data_path}/ica/s{subnum}_b{block}-ica.fif")
            print("\n",f"participants{subnum} block{block} saved as 's{subnum}_b{block}-ica.fif'","\n")

print("\n","... all done","\n")


#%%
'''
looking for eye components using templates
applying ICA

'''

blinks = {}

for i in range(8,9):
    subnum = subs[i]
    for k in range(3):
        block = blocks[k]
        if block == "03" and subnum == "006":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "007":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif subnum == "004" or subnum == "002" or subnum == "010":
            continue
        else:
            ica = mne.preprocessing.read_ica(f"{data_path}/ica/s{subnum}_b{block}-ica.fif")
            fig = ica.plot_components(title=f"s{subnum}_b{block}_components")[0]
            fig.savefig(fname = f"{data_path}/ica/componentplots/s{subnum}_b{block}_components.png")
            plt.close("all")
            corrmap([ica], blink_up, threshold=0.85, label="blink_up", show=False)
            corrmap([ica], blink_side, threshold=0.85, label="blink_side", show=False)
            badcomponents = []
            for label in ica.labels_:
                badcomponents.extend(ica.labels_[label])

            blinks[f"s{subnum}_b{block}"] = badcomponents
            ica.exclude = badcomponents
            filename = f"s{subnum}_b{block}-raw.fif"
            raw =  mne.io.read_raw_fif(f"{data_path}/rawfilter/{filename}", preload=True)
            ica.apply(raw)
            raw.save(f"{data_path}/icaapplied/s{subnum}_b{block}-raw.fif",overwrite=True)

#%%

'''
for some participants it did not work in the loop

'''

subnum = "008"
block = "03"


ica = mne.preprocessing.read_ica(f"{data_path}/ica/s{subnum}_b{block}-ica.fif")
fig = ica.plot_components(title=f"s{subnum}_b{block}_components")[0]
fig.savefig(fname = f"{data_path}/ica/componentplots/s{subnum}_b{block}_components.png")
plt.close("all")
corrmap([ica], blink_up, threshold=0.85, label="blink_up", show=False)
#corrmap([ica], blink_side, threshold=0.85, label="blink_side", show=False)
badcomponents = []
for label in ica.labels_:
    badcomponents.extend(ica.labels_[label])
blinks[f"s{subnum}_b{block}"] = badcomponents
ica.exclude = badcomponents
filename = f"s{subnum}_b{block}-raw.fif"
raw =  mne.io.read_raw_fif(f"{data_path}/rawfilter/{filename}", preload=True)
ica.apply(raw)
raw.save(f"{data_path}/icaapplied/s{subnum}_b{block}-raw.fif",overwrite=True)

print("\n","... done","\n")

#sub002b02threshold: 0.8 blink_up

#%%
'''
write csv with excluded components

'''

a_file = open("excludedcomp.csv", "w")
writer = csv.writer(a_file)

for key, value in blinks.items():

    writer.writerow([key, value])


a_file.close()

            


#%%
'''
make epochs and averages for each participant

'''

data = {}
data_epochs = {}
data_standard = {}
data_target = {}
data_non_target = {}
data_fr = {}
data_lr = {}
standard_avg = {}
target_avg = {}
non_target_avg = {}
fr_avg = {}
lr_avg = {}

for i in range(13):
    subnum = subs[i]
    for k in range(3):
        block = blocks[k]
        if block == "03" and subnum == "006":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "007":
            data[f"s{subnum}_b{block}"] = "doesn't exist"
        elif block == "01" and subnum == "012":
            data[f"s{subnum}_b{block}"] = "excluded"
        else:
            data[f"s{subnum}_b{block}"] =  mne.io.read_raw_fif(f"{data_path}/icaapplied/s{subnum}_b{block}-raw.fif", preload=True) 
            events = mne.find_events(data[f"s{subnum}_b{block}"], min_duration=0.001, shortest_event=1) 
            stim_events = events[(events[:,2] == 2) | (events[:,2] == 8) | (events[:,2] == 4)]
            stims_df = pandas.DataFrame(stim_events)
            backcode = stims_df[2].shift(1) 
            stims_df.insert(3, 'backCode', backcode)
            forwardcode = stims_df[2].shift(-1) 
            stims_df.insert(4, 'forwardCode', forwardcode)

            first_rep = stims_df[(stims_df["backCode"] == 4) | (stims_df["backCode"] == 8)]
            del first_rep['backCode']
            del first_rep['forwardCode']
            last_rep = stims_df[(stims_df["forwardCode"] == 4) | (stims_df["forwardCode"] == 8)]
            del last_rep['backCode']
            del last_rep['forwardCode']

            fr_events = first_rep.to_numpy(dtype=int)
            lr_events = last_rep.to_numpy(dtype=int)


            standard_events = events[(events[:,2] == 2)]
            target_events = events[(events[:,2] == 4)]
            non_target_events = events[(events[:,2] == 8)]

            data_epochs[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], stim_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_epochs[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/epochs_{subnum}_b{block}-epo.fif", overwrite=True)
            data_standard[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], standard_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_standard[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/standard_{subnum}_b{block}-epo.fif", overwrite=True)
            data_target[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], target_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_target[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/target_{subnum}_b{block}-epo.fif", overwrite=True)
            data_non_target[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], non_target_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_non_target[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/non_target_{subnum}_b{block}-epo.fif", overwrite=True)
            data_fr[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], fr_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_epochs[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/fr_{subnum}_b{block}-epo.fif", overwrite=True)
            data_lr[f"s{subnum}_b{block}"] = mne.Epochs(data[f"s{subnum}_b{block}"], lr_events, tmin=-0.3, tmax=1,preload=True, baseline=(-0.3,-0.05))
            data_epochs[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/lr_{subnum}_b{block}-epo.fif", overwrite=True)

            standard_avg[f"s{subnum}_b{block}"] = data_standard[f"s{subnum}_b{block}"].average()
            standard_avg[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/sta_avg_{subnum}_b{block}-epo.fif")
            target_avg[f"s{subnum}_b{block}"] = data_target[f"s{subnum}_b{block}"].average()
            target_avg[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/tar_avg_{subnum}_b{block}-epo.fif")
            non_target_avg[f"s{subnum}_b{block}"] = data_non_target[f"s{subnum}_b{block}"].average()
            non_target_avg[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/ntar_avg_{subnum}_b{block}-epo.fif")
            fr_avg[f"s{subnum}_b{block}"] = data_fr[f"s{subnum}_b{block}"].average()
            fr_avg[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/fr_avg_{subnum}_b{block}-epo.fif")
            lr_avg[f"s{subnum}_b{block}"] = data_lr[f"s{subnum}_b{block}"].average()
            lr_avg[f"s{subnum}_b{block}"].save(f"{data_path}/epochs/lr_avg_{subnum}_b{block}-epo.fif")
            print("\n",f"participants{subnum} block{block} done","\n")





print("ok")



#%%

'''
make lists out of dicts

'''

l_standard = list(standard_avg.values())
l_target = list(target_avg.values())
l_non_target = list(non_target_avg.values())
l_fr = list(fr_avg.values())
l_lr = list(lr_avg.values())


#%%

'''
save lists

'''

import pickle
file_name = "standard.pkl"

open_file = open(file_name, "wb")

pickle.dump(l_standard, open_file)

open_file.close()

file_name = "target.pkl"

open_file = open(file_name, "wb")

pickle.dump(l_target, open_file)

open_file.close()

file_name = "non_target.pkl"

open_file = open(file_name, "wb")

pickle.dump(l_non_target, open_file)

open_file.close()

file_name = "fr.pkl"

open_file = open(file_name, "wb")

pickle.dump(l_fr, open_file)

open_file.close()

file_name = "lr.pkl"

open_file = open(file_name, "wb")

pickle.dump(l_lr, open_file)

open_file.close()


#%%
'''
read lists

'''

file_name = ("standard.pkl")
open_file = open(file_name, "rb")
standard = pickle.load(open_file)

open_file.close()

file_name = ("target.pkl")
open_file = open(file_name, "rb")
target = pickle.load(open_file)

open_file.close()

file_name = ("non_target.pkl")
open_file = open(file_name, "rb")
non_target = pickle.load(open_file)

open_file.close()

file_name = ("fr.pkl")
open_file = open(file_name, "rb")
fr = pickle.load(open_file)

open_file.close()

file_name = ("lr.pkl")
open_file = open(file_name, "rb")
lr = pickle.load(open_file)

open_file.close()

print("done")

#%%

'''
grand average

'''

mne.grand_average(standard).plot_joint(title="Grandaverage standard");
mne.grand_average(target).plot_joint(title="Grandaverage target");
mne.grand_average(non_target).plot_joint(title="Grandaverage non target");
mne.grand_average(fr).plot_joint(title="Grandaverage first repetition");
mne.grand_average(lr).plot_joint(title="Grandaverage last repetition");

#%%
'''
difference waves

'''

diff = mne.combine_evoked([mne.grand_average(target), mne.grand_average(standard)], weights=[1,-1])
diff.plot_joint(title ="Differencewave target - standard" );

diff = mne.combine_evoked([mne.grand_average(lr), mne.grand_average(fr)], weights=[1,-1])
diff.plot_joint(title ="Differencewave last - first repetition" );

