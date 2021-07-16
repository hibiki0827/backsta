## Information
* for details about dataset: look at data.md
* details about analysis: look at project.md

## STEP1: preparation
* creating github account -> done
* creating project in osf.io -> done
* preregistreation -> done
* updating readme.md
* updating data.md
* updating dataaccess.md


## STEP2: looking at the data
* read-in the EEG files
* sub 06 block3 and sub 07 block 01 seem to be missing!!
* electrode Fp1 weird -> excluded!!
 * probably Fp1 was on the wrong place somewhere posterior

## STEP3: Preprocessing - filtering
* filter: l_freq=0.1, h_freq=50.0
* reference: average
* raw files saved 
* -> all done

## STEP4: Preprocessing - ICA
* ICA templates for eye movements (vertical & horizontal) taken from sub 01
* automatic detection with threshold 0.85
* excluded components can be found in "excludedcomp.csv" (can be found on github)
* some of the components could not be found vis the loop (the loop gave an error if only one of the two components exist) -> used templates by hand
* -> done

## STEP5: Analysis
* dividing in epochs
* standard
* target
* non_Target
* first and last repetition


------------------------------------------------------------------

## Notes
* updating readme.md
* updating data.md
* updating dataaccess.md
* updating project.md
* creating timeline in gitkarten
* creating project in osf.io
* looking for more literature
* preregistration in osf.io




whiat I am thinking about right now:

the repetition positivity 
* the repetition positivity reflects the repetition supression
* higher sensory levels provide prediction signal to lower levels
* suppression of prediction error
* slow positive wave from 5 - 250ms SOT inceasing with standard stimulus repetition

I should expect a repetition positivity that increases for every repetition (e.g. Bladweg 2007)

I should see a MMN for the deviants 

problem: what should I expect for the standard right after the Deviant
* one version: RP increases with repetiton ->  does not only depend on the last stimulus -> there could be an decrease but according to the pattern before the deviant the standard is still somehow expected
* another version: the deviant makes the brain reset the prediction -> no repetition positivity should be seen

# test

## test

### test
