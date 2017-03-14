#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.03), Wed Oct 10 16:22:23 2012
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'Syntax1'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'],expInfo['session'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='#505050') # the same color as rgb [80,80,80]

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
WaitforTrigger = visual.TextStim(win=win, ori=0, name='WaitforTrigger',
    text='Get Ready!',
    font='Arial',
    pos=[0, -0.65], height=0.12, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
coloralien = visual.ImageStim(win=win, name='coloralien',
    image='stimuli'+os.path.sep+'Color.bmp', mask=None,
    ori=0, pos=[0, 0], units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "FirstAcquisition"
FirstAcquisitionClock = core.Clock()
greyalien = visual.ImageStim(win=win, name='greyalien',
    image='stimuli'+os.path.sep+'Grey.bmp', mask=None,
    ori=0, pos=[0, 0],units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixateAlien = visual.ImageStim(win=win, name='fixateAlien',
    image=None, mask=None,
    ori=0, pos=[0, 0], units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
sentence = sound.Sound('A', secs=3.9)
sentence.setVolume(1)
greyAlien = visual.ImageStim(win=win, name='greyAlien',
    image='stimuli/Grey.bmp', mask=None,
    ori=0, pos=[0, 0], units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-3.0)
questionAlien = visual.ImageStim(win=win, name='questionAlien',
    image=None, mask=None,
    ori=0, pos=[0, 0], units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "RemainingTime"
RemainingTimeClock = core.Clock()
greyAlienRemaining = visual.ImageStim(win=win, name='greyAlienRemaining',
    image='stimuli/Grey.bmp', mask=None,
    ori=0, pos=[0, 0], units='pix', size=[719.42, 539.65],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Done"
DoneClock = core.Clock()
doneText = visual.TextStim(win=win, ori=0, name='doneText',
    text="You're Done!",
    font='Arial',
    pos=[0, 0], height=0.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"Ready"-------
t = 0
ReadyClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
Trigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
Trigger.status = NOT_STARTED
# keep track of which components have finished
ReadyComponents = []
ReadyComponents.append(WaitforTrigger)
ReadyComponents.append(coloralien)
ReadyComponents.append(Trigger)
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Ready"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = ReadyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WaitforTrigger* updates
    if t >= 0.0 and WaitforTrigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        WaitforTrigger.tStart = t  # underestimates by a little under one frame
        WaitforTrigger.frameNStart = frameN  # exact frame index
        WaitforTrigger.setAutoDraw(True)
    
    # *coloralien* updates
    if t >= 0.0 and coloralien.status == NOT_STARTED:
        # keep track of start time/frame for later
        coloralien.tStart = t  # underestimates by a little under one frame
        coloralien.frameNStart = frameN  # exact frame index
        coloralien.setAutoDraw(True)
    
    # *Trigger* updates
    if t >= 0.0 and Trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        Trigger.tStart = t  # underestimates by a little under one frame
        Trigger.frameNStart = frameN  # exact frame index
        Trigger.status = STARTED
        # keyboard checking is just starting
        Trigger.clock.reset()  # now t=0
        event.clearEvents()
    if Trigger.status == STARTED:  # only update if being drawn
        theseKeys = event.getKeys(keyList=['5', 'num_5', 'num_add', '+'])
        if len(theseKeys) > 0:  # at least one key was pressed
            Trigger.keys = theseKeys[-1]  # just the last key pressed
            Trigger.rt = Trigger.clock.getTime()
            # abort routine on response
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Ready"-------
for thisComponent in ReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine"FirstAcquisition"-------
t = 0
FirstAcquisitionClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
FirstAcquisitionComponents = []
FirstAcquisitionComponents.append(greyalien)
for thisComponent in FirstAcquisitionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "FirstAcquisition"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FirstAcquisitionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *greyalien* updates
    if t >= 0.0 and greyalien.status == NOT_STARTED:
        # keep track of start time/frame for later
        greyalien.tStart = t  # underestimates by a little under one frame
        greyalien.frameNStart = frameN  # exact frame index
        greyalien.setAutoDraw(True)
    elif greyalien.status == STARTED and t >= (0.0 + 2.0):
        greyalien.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FirstAcquisitionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "FirstAcquisition"-------
for thisComponent in FirstAcquisitionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('run-designs/syntax_run1.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine"trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.Add(6.000000)
    # update component parameters for each repeat
    fixateAlien.setImage('stimuli'+os.path.sep+'%s.bmp'%(thisTrial.FixateAlien))
    questionAlien.setImage("stimuli/%s.bmp"%(thisTrial.QuestionAlien))
    sentence.setSound('stimuli/%s/%s_2.wav'%(thisTrial.Type,thisTrial.Sentence))
    trial_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    trial_resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(fixateAlien)
    trialComponents.append(sentence)
    trialComponents.append(trial_resp)
    trialComponents.append(greyAlien)
    trialComponents.append(questionAlien)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixateAlien* updates
        if t >= 0.0 and fixateAlien.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixateAlien.tStart = t  # underestimates by a little under one frame
            fixateAlien.frameNStart = frameN  # exact frame index
            fixateAlien.setAutoDraw(True)
        elif fixateAlien.status == STARTED and t >= (0.0 + thisTrial.Latency):
            fixateAlien.setAutoDraw(False)
        # start/stop sentence
        if t >= 0.1 and sentence.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence.tStart = t  # underestimates by a little under one frame
            sentence.frameNStart = frameN  # exact frame index
            sentence.play()  # start the sound (it finishes automatically)
        elif sentence.status == STARTED and t >= (0.1 + 3.9):
            sentence.stop()  # stop the sound (if longer than duration)
        
        # *trial_resp* updates
        if t >= 0.1 and trial_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_resp.tStart = t  # underestimates by a little under one frame
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.status = STARTED
            # keyboard checking is just starting
            trial_resp.clock.reset()  # now t=0
            event.clearEvents()
        elif trial_resp.status == STARTED and t >= (0.1 + 5.9):
            trial_resp.status = STOPPED
        if trial_resp.status == STARTED:  # only update if being drawn
            theseKeys = event.getKeys(keyList=['1', 'num_1', '2', 'num_2', '3', 'num_3', '4', 'num_4'])
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_resp.keys = theseKeys[-1]  # just the last key pressed
                trial_resp.rt = trial_resp.clock.getTime()
                # was this 'correct'?
                if (trial_resp.keys == str(Correct)): trial_resp.corr = 1
                else: trial_resp.corr=0
        
        # *greyAlien* updates
        if t >= (thisTrial.Latency+2) and greyAlien.status == NOT_STARTED:
            # keep track of start time/frame for later
            greyAlien.tStart = t  # underestimates by a little under one frame
            greyAlien.frameNStart = frameN  # exact frame index
            greyAlien.setAutoDraw(True)
        elif greyAlien.status == STARTED and t >= (2+thisTrial.Latency + thisTrial.BlankDur):
            greyAlien.setAutoDraw(False)
        
        # *questionAlien* updates
        if t >= (thisTrial.Latency) and questionAlien.status == NOT_STARTED:
            # keep track of start time/frame for later
            questionAlien.tStart = t  # underestimates by a little under one frame
            questionAlien.frameNStart = frameN  # exact frame index
            questionAlien.setAutoDraw(True)
        elif questionAlien.status == STARTED and t >= (thisTrial.Latency + 2.0):
            questionAlien.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested that we end
            routineTimer.reset()  # this is the new t0 for non-slip Routines
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if len(trial_resp.keys) == 0:  # No response was made
       trial_resp.keys=None
       # was no response the correct answer?!
       if str(Correct).lower() == 'none': trial_resp.corr = 1  # correct non-response
       else: trial_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('trial_resp.keys',trial_resp.keys)
    trials.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials.addData('trial_resp.rt', trial_resp.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):  params = []
else:  params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine"RemainingTime"-------
t = 0
RemainingTimeClock.reset()  # clock 
frameN = -1
# routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
RemainingTimeComponents = []
RemainingTimeComponents.append(greyAlienRemaining)
for thisComponent in RemainingTimeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "RemainingTime"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = RemainingTimeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *greyAlienRemaining* updates
    if t >= 0.0 and greyAlienRemaining.status == NOT_STARTED:
        # keep track of start time/frame for later
        greyAlienRemaining.tStart = t  # underestimates by a little under one frame
        greyAlienRemaining.frameNStart = frameN  # exact frame index
        greyAlienRemaining.setAutoDraw(True)
    elif greyAlienRemaining.status == STARTED and t >= (0.0 + 10.0):
        greyAlienRemaining.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        #routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RemainingTimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "RemainingTime"-------
for thisComponent in RemainingTimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine"Done"-------
t = 0
DoneClock.reset()  # clock 
frameN = -1
# routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
DoneComponents = []
DoneComponents.append(doneText)
for thisComponent in DoneComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Done"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = DoneClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *doneText* updates
    if t >= 0.0 and doneText.status == NOT_STARTED:
        # keep track of start time/frame for later
        doneText.tStart = t  # underestimates by a little under one frame
        doneText.frameNStart = frameN  # exact frame index
        doneText.setAutoDraw(True)
    elif doneText.status == STARTED and t >= (0.0 + 4.0):
        doneText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested that we end
        # routineTimer.reset()  # this is the new t0 for non-slip Routines
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Done"-------
for thisComponent in DoneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Shutting down:
win.close()
core.quit()

