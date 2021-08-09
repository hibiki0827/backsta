# Lab notebook


## STEP1: preparation (Weeks 1 - 5: 04.05.2021 - 13.06.2021)
* creating github repository 
* creating project in osf.io 
* preregistration on osf 
* get to know jupyter, python, docker etc.
* literature search
* problems/ issues:
  * docker doesn't run -> solved
  * couldn't find as much literature as I wanted to

## STEP2: looking at the data (Weeks  6 & 7: 07.06.2021 - 20.06.2021)
* read-in the EEG files
* sub 06 block3 and sub 07 block 01 seem to be missing!!
* electrode Fp1 weird -> excluded!!
  * probably Fp1 was on the wrong place somewhere posterior
* problems/ issues:
  * problems with mne: didn't run properly   

## STEP3: Preprocessing - filtering (Weeks 8 & 9: 21.06. - 04.07.)
* filter: l_freq=0.1, h_freq=50.0
* reference: average
* raw files saved 
  *  problems with mne: didn't run properly -> solved
  *  problems with reading the data -> solved
 
## STEP4: Preprocessing - ICA (Weeks 10 - 11: 05.07. - 18.07.)
* ICA templates for eye movements (vertical & horizontal) taken from sub 01
* automatic detection with threshold 0.85
* excluded components can be found in [excludedcomp.csv](https://github.com/hibiki0827/backsta/blob/master/project/excludedcomp.csv)
* for some of the subjects it could not be found in the loop (the loop gave an error if only one of the two components exist) -> used templates by hand 
* problems / issues
  * couldn't save components -> solved
  *  for some of the subjects it could not be found with the loop -> used templates manually (probably try exept would have been the smarter solution)

## STEP5: Analysis (Weeks 12 - 13: 19.07. - 01.08.)
* dividing in epochs
* standard
* target
* non_Target
* first and last repetition
* subject 12 block 01 weird electrode?? weird plots -> excluded
* grand averages
* difference waves: target-standard, first&last repetition
* problems / issues:
  * subject 12 block 01 weird -> excluded (see picture)
  * all standards had the same marker -> how can I filter out the firt and last repetition -> solved using Pandas package and shifting markers to select standards following deviants

grand average before excluding sub 12 bl 01

![ga_stand](https://user-images.githubusercontent.com/73951037/128662218-4319f3a0-974c-44fa-ba2a-1084168c92d1.png)


## STEP6: Poster & Jupyter notebook (Weeks 14 - : 02.08. - 
* creating jupyter notebook out of github account
* updating github pages
* updating osf.io
* making poster
* problems / issues:
  * problems with turining github repository into jupyter notebook: wrong page displayed -> solved




