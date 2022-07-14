#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on July 13, 2022, at 13:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.3'
expName = 'localizer'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': '0001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/subj%s_run%s_%s_%s' % (expInfo['participant'], expInfo['run'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Public\\Moore_fMRI\\LocalizerCode\\localizer_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Ready_experimenter"
Ready_experimenterClock = core.Clock()
Ready_experimenter_text = visual.TextStim(win=win, name='Ready_experimenter_text',
    text='Waiting for the experimenter...',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ready_experimenter_resp = keyboard.Keyboard()

# Initialize components for Routine "Alignment"
AlignmentClock = core.Clock()
Alignment_background = visual.Rect(
    win=win, name='Alignment_background',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=1, depth=0.0, interpolate=True)
Alignment_image = visual.ImageStim(
    win=win,
    name='Alignment_image', 
    image='Alignment.png', mask=None,
    ori=0, pos=(0, 0), size=[1.4,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
Alignment_resp = keyboard.Keyboard()

# Initialize components for Routine "Button_check"
Button_checkClock = core.Clock()
Button_text = visual.TextStim(win=win, name='Button_text',
    text='Button check.',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Index"
IndexClock = core.Clock()
Index_text = visual.TextStim(win=win, name='Index_text',
    text='Press the button under your index finger.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Index_resp = keyboard.Keyboard()

# Initialize components for Routine "Middle"
MiddleClock = core.Clock()
Middle_text = visual.TextStim(win=win, name='Middle_text',
    text='Press the button under your middle finger.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Middle_resp = keyboard.Keyboard()

# Initialize components for Routine "Repeat"
RepeatClock = core.Clock()
Repeat_text = visual.TextStim(win=win, name='Repeat_text',
    text='Repeat button check?\n\nExperimenter: Press Y or N.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Repeat_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text='Please fixate on the crosshair and pay attention to each image.\nThe images will go by quickly.\n\nPress the button with your INDEX FINGER if an image appears twice in a row.\n\nGet ready!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "wait_for_t"
wait_for_tClock = core.Clock()
scanner_t = keyboard.Keyboard()
import datetime

subject = str(expInfo['participant'])
subject = 'subj0' + subject[-3:]
session = 'run%04d' % int(expInfo['run'])

sequence_file = 'localizer' + os.sep + 'sequences' + os.sep + 'loc_' + subject + '_' + session + '.csv'

win.mouseVisible = False
fixation_wait_for_t = visual.ShapeStim(
    win=win, name='fixation_wait_for_t', vertices='cross',
    size=(0.02, 0.02),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(.8,.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.02, 0.02),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1.000,-1.000,-1.000],
    opacity=1, depth=-2.0, interpolate=True)
repeat_response = keyboard.Keyboard()

# Initialize components for Routine "null_block"
null_blockClock = core.Clock()
fixation_null = visual.ShapeStim(
    win=win, name='fixation_null', vertices='cross',
    size=(0.02, 0.02),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='That concludes this run.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Ready_experimenter"-------
continueRoutine = True
# update component parameters for each repeat
Ready_experimenter_resp.keys = []
Ready_experimenter_resp.rt = []
_Ready_experimenter_resp_allKeys = []
# keep track of which components have finished
Ready_experimenterComponents = [Ready_experimenter_text, Ready_experimenter_resp]
for thisComponent in Ready_experimenterComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ready_experimenterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready_experimenter"-------
while continueRoutine:
    # get current time
    t = Ready_experimenterClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ready_experimenterClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ready_experimenter_text* updates
    if Ready_experimenter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ready_experimenter_text.frameNStart = frameN  # exact frame index
        Ready_experimenter_text.tStart = t  # local t and not account for scr refresh
        Ready_experimenter_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ready_experimenter_text, 'tStartRefresh')  # time at next scr refresh
        Ready_experimenter_text.setAutoDraw(True)
    
    # *Ready_experimenter_resp* updates
    waitOnFlip = False
    if Ready_experimenter_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ready_experimenter_resp.frameNStart = frameN  # exact frame index
        Ready_experimenter_resp.tStart = t  # local t and not account for scr refresh
        Ready_experimenter_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ready_experimenter_resp, 'tStartRefresh')  # time at next scr refresh
        Ready_experimenter_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Ready_experimenter_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Ready_experimenter_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Ready_experimenter_resp.status == STARTED and not waitOnFlip:
        theseKeys = Ready_experimenter_resp.getKeys(keyList=['enter', 'return'], waitRelease=False)
        _Ready_experimenter_resp_allKeys.extend(theseKeys)
        if len(_Ready_experimenter_resp_allKeys):
            Ready_experimenter_resp.keys = _Ready_experimenter_resp_allKeys[0].name  # just the first key pressed
            Ready_experimenter_resp.rt = _Ready_experimenter_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ready_experimenterComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready_experimenter"-------
for thisComponent in Ready_experimenterComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ready_experimenter_text.started', Ready_experimenter_text.tStartRefresh)
thisExp.addData('Ready_experimenter_text.stopped', Ready_experimenter_text.tStopRefresh)
# check responses
if Ready_experimenter_resp.keys in ['', [], None]:  # No response was made
    Ready_experimenter_resp.keys = None
thisExp.addData('Ready_experimenter_resp.keys',Ready_experimenter_resp.keys)
if Ready_experimenter_resp.keys != None:  # we had a response
    thisExp.addData('Ready_experimenter_resp.rt', Ready_experimenter_resp.rt)
thisExp.addData('Ready_experimenter_resp.started', Ready_experimenter_resp.tStartRefresh)
thisExp.addData('Ready_experimenter_resp.stopped', Ready_experimenter_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ready_experimenter" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Alignment"-------
continueRoutine = True
# update component parameters for each repeat
Alignment_resp.keys = []
Alignment_resp.rt = []
_Alignment_resp_allKeys = []
# keep track of which components have finished
AlignmentComponents = [Alignment_background, Alignment_image, Alignment_resp]
for thisComponent in AlignmentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AlignmentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Alignment"-------
while continueRoutine:
    # get current time
    t = AlignmentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AlignmentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Alignment_background* updates
    if Alignment_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Alignment_background.frameNStart = frameN  # exact frame index
        Alignment_background.tStart = t  # local t and not account for scr refresh
        Alignment_background.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Alignment_background, 'tStartRefresh')  # time at next scr refresh
        Alignment_background.setAutoDraw(True)
    
    # *Alignment_image* updates
    if Alignment_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Alignment_image.frameNStart = frameN  # exact frame index
        Alignment_image.tStart = t  # local t and not account for scr refresh
        Alignment_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Alignment_image, 'tStartRefresh')  # time at next scr refresh
        Alignment_image.setAutoDraw(True)
    
    # *Alignment_resp* updates
    waitOnFlip = False
    if Alignment_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Alignment_resp.frameNStart = frameN  # exact frame index
        Alignment_resp.tStart = t  # local t and not account for scr refresh
        Alignment_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Alignment_resp, 'tStartRefresh')  # time at next scr refresh
        Alignment_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Alignment_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Alignment_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Alignment_resp.status == STARTED and not waitOnFlip:
        theseKeys = Alignment_resp.getKeys(keyList=['return', 'enter'], waitRelease=False)
        _Alignment_resp_allKeys.extend(theseKeys)
        if len(_Alignment_resp_allKeys):
            Alignment_resp.keys = _Alignment_resp_allKeys[-1].name  # just the last key pressed
            Alignment_resp.rt = _Alignment_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AlignmentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Alignment"-------
for thisComponent in AlignmentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Alignment_background.started', Alignment_background.tStartRefresh)
thisExp.addData('Alignment_background.stopped', Alignment_background.tStopRefresh)
thisExp.addData('Alignment_image.started', Alignment_image.tStartRefresh)
thisExp.addData('Alignment_image.stopped', Alignment_image.tStopRefresh)
# check responses
if Alignment_resp.keys in ['', [], None]:  # No response was made
    Alignment_resp.keys = None
thisExp.addData('Alignment_resp.keys',Alignment_resp.keys)
if Alignment_resp.keys != None:  # we had a response
    thisExp.addData('Alignment_resp.rt', Alignment_resp.rt)
thisExp.addData('Alignment_resp.started', Alignment_resp.tStartRefresh)
thisExp.addData('Alignment_resp.stopped', Alignment_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Alignment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Button = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Button')
thisExp.addLoop(Button)  # add the loop to the experiment
thisButton = Button.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisButton.rgb)
if thisButton != None:
    for paramName in thisButton:
        exec('{} = thisButton[paramName]'.format(paramName))

for thisButton in Button:
    currentLoop = Button
    # abbreviate parameter names if possible (e.g. rgb = thisButton.rgb)
    if thisButton != None:
        for paramName in thisButton:
            exec('{} = thisButton[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Button_check"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Button_checkComponents = [Button_text]
    for thisComponent in Button_checkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Button_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Button_check"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Button_checkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Button_checkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Button_text* updates
        if Button_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Button_text.frameNStart = frameN  # exact frame index
            Button_text.tStart = t  # local t and not account for scr refresh
            Button_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Button_text, 'tStartRefresh')  # time at next scr refresh
            Button_text.setAutoDraw(True)
        if Button_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Button_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Button_text.tStop = t  # not accounting for scr refresh
                Button_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Button_text, 'tStopRefresh')  # time at next scr refresh
                Button_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Button_checkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Button_check"-------
    for thisComponent in Button_checkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Button.addData('Button_text.started', Button_text.tStartRefresh)
    Button.addData('Button_text.stopped', Button_text.tStopRefresh)
    
    # ------Prepare to start Routine "Index"-------
    continueRoutine = True
    # update component parameters for each repeat
    Index_resp.keys = []
    Index_resp.rt = []
    _Index_resp_allKeys = []
    # keep track of which components have finished
    IndexComponents = [Index_text, Index_resp]
    for thisComponent in IndexComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IndexClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Index"-------
    while continueRoutine:
        # get current time
        t = IndexClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IndexClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Index_text* updates
        if Index_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Index_text.frameNStart = frameN  # exact frame index
            Index_text.tStart = t  # local t and not account for scr refresh
            Index_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Index_text, 'tStartRefresh')  # time at next scr refresh
            Index_text.setAutoDraw(True)
        
        # *Index_resp* updates
        waitOnFlip = False
        if Index_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Index_resp.frameNStart = frameN  # exact frame index
            Index_resp.tStart = t  # local t and not account for scr refresh
            Index_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Index_resp, 'tStartRefresh')  # time at next scr refresh
            Index_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Index_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Index_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Index_resp.status == STARTED and not waitOnFlip:
            theseKeys = Index_resp.getKeys(keyList=['y'], waitRelease=False)
            _Index_resp_allKeys.extend(theseKeys)
            if len(_Index_resp_allKeys):
                Index_resp.keys = _Index_resp_allKeys[-1].name  # just the last key pressed
                Index_resp.rt = _Index_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IndexComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Index"-------
    for thisComponent in IndexComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Button.addData('Index_text.started', Index_text.tStartRefresh)
    Button.addData('Index_text.stopped', Index_text.tStopRefresh)
    # check responses
    if Index_resp.keys in ['', [], None]:  # No response was made
        Index_resp.keys = None
    Button.addData('Index_resp.keys',Index_resp.keys)
    if Index_resp.keys != None:  # we had a response
        Button.addData('Index_resp.rt', Index_resp.rt)
    Button.addData('Index_resp.started', Index_resp.tStartRefresh)
    Button.addData('Index_resp.stopped', Index_resp.tStopRefresh)
    # the Routine "Index" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Middle"-------
    continueRoutine = True
    # update component parameters for each repeat
    Middle_resp.keys = []
    Middle_resp.rt = []
    _Middle_resp_allKeys = []
    # keep track of which components have finished
    MiddleComponents = [Middle_text, Middle_resp]
    for thisComponent in MiddleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MiddleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Middle"-------
    while continueRoutine:
        # get current time
        t = MiddleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MiddleClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Middle_text* updates
        if Middle_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Middle_text.frameNStart = frameN  # exact frame index
            Middle_text.tStart = t  # local t and not account for scr refresh
            Middle_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Middle_text, 'tStartRefresh')  # time at next scr refresh
            Middle_text.setAutoDraw(True)
        
        # *Middle_resp* updates
        waitOnFlip = False
        if Middle_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Middle_resp.frameNStart = frameN  # exact frame index
            Middle_resp.tStart = t  # local t and not account for scr refresh
            Middle_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Middle_resp, 'tStartRefresh')  # time at next scr refresh
            Middle_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Middle_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Middle_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Middle_resp.status == STARTED and not waitOnFlip:
            theseKeys = Middle_resp.getKeys(keyList=['b'], waitRelease=False)
            _Middle_resp_allKeys.extend(theseKeys)
            if len(_Middle_resp_allKeys):
                Middle_resp.keys = _Middle_resp_allKeys[-1].name  # just the last key pressed
                Middle_resp.rt = _Middle_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MiddleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Middle"-------
    for thisComponent in MiddleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Button.addData('Middle_text.started', Middle_text.tStartRefresh)
    Button.addData('Middle_text.stopped', Middle_text.tStopRefresh)
    # check responses
    if Middle_resp.keys in ['', [], None]:  # No response was made
        Middle_resp.keys = None
    Button.addData('Middle_resp.keys',Middle_resp.keys)
    if Middle_resp.keys != None:  # we had a response
        Button.addData('Middle_resp.rt', Middle_resp.rt)
    Button.addData('Middle_resp.started', Middle_resp.tStartRefresh)
    Button.addData('Middle_resp.stopped', Middle_resp.tStopRefresh)
    # the Routine "Middle" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Repeat"-------
    continueRoutine = True
    # update component parameters for each repeat
    Repeat_resp.keys = []
    Repeat_resp.rt = []
    _Repeat_resp_allKeys = []
    # keep track of which components have finished
    RepeatComponents = [Repeat_text, Repeat_resp]
    for thisComponent in RepeatComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RepeatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Repeat"-------
    while continueRoutine:
        # get current time
        t = RepeatClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RepeatClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Repeat_text* updates
        if Repeat_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Repeat_text.frameNStart = frameN  # exact frame index
            Repeat_text.tStart = t  # local t and not account for scr refresh
            Repeat_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Repeat_text, 'tStartRefresh')  # time at next scr refresh
            Repeat_text.setAutoDraw(True)
        
        # *Repeat_resp* updates
        waitOnFlip = False
        if Repeat_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Repeat_resp.frameNStart = frameN  # exact frame index
            Repeat_resp.tStart = t  # local t and not account for scr refresh
            Repeat_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Repeat_resp, 'tStartRefresh')  # time at next scr refresh
            Repeat_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Repeat_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Repeat_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Repeat_resp.status == STARTED and not waitOnFlip:
            theseKeys = Repeat_resp.getKeys(keyList=['y', 'n'], waitRelease=False)
            _Repeat_resp_allKeys.extend(theseKeys)
            if len(_Repeat_resp_allKeys):
                Repeat_resp.keys = _Repeat_resp_allKeys[-1].name  # just the last key pressed
                Repeat_resp.rt = _Repeat_resp_allKeys[-1].rt
                # was this correct?
                if (Repeat_resp.keys == str('y')) or (Repeat_resp.keys == 'y'):
                    Repeat_resp.corr = 1
                else:
                    Repeat_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RepeatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Repeat"-------
    for thisComponent in RepeatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if Repeat_resp.keys == 'n':
        Button.finished = True
    Button.addData('Repeat_text.started', Repeat_text.tStartRefresh)
    Button.addData('Repeat_text.stopped', Repeat_text.tStopRefresh)
    # check responses
    if Repeat_resp.keys in ['', [], None]:  # No response was made
        Repeat_resp.keys = None
        # was no response the correct answer?!
        if str('y').lower() == 'none':
           Repeat_resp.corr = 1;  # correct non-response
        else:
           Repeat_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Button (TrialHandler)
    Button.addData('Repeat_resp.keys',Repeat_resp.keys)
    Button.addData('Repeat_resp.corr', Repeat_resp.corr)
    if Repeat_resp.keys != None:  # we had a response
        Button.addData('Repeat_resp.rt', Repeat_resp.rt)
    Button.addData('Repeat_resp.started', Repeat_resp.tStartRefresh)
    Button.addData('Repeat_resp.stopped', Repeat_resp.tStopRefresh)
    # the Routine "Repeat" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'Button'


# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instruction_text, key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space', 'b', 'r', 'g', 'y'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text.started', instruction_text.tStartRefresh)
thisExp.addData('instruction_text.stopped', instruction_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(sequence_file),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wait_for_t"-------
    continueRoutine = True
    # update component parameters for each repeat
    scanner_t.keys = []
    scanner_t.rt = []
    _scanner_t_allKeys = []
    # keep track of which components have finished
    wait_for_tComponents = [scanner_t, fixation_wait_for_t]
    for thisComponent in wait_for_tComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wait_for_tClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wait_for_t"-------
    while continueRoutine:
        # get current time
        t = wait_for_tClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wait_for_tClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *scanner_t* updates
        waitOnFlip = False
        if scanner_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scanner_t.frameNStart = frameN  # exact frame index
            scanner_t.tStart = t  # local t and not account for scr refresh
            scanner_t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scanner_t, 'tStartRefresh')  # time at next scr refresh
            scanner_t.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(scanner_t.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(scanner_t.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if scanner_t.status == STARTED and not waitOnFlip:
            theseKeys = scanner_t.getKeys(keyList=['t'], waitRelease=False)
            _scanner_t_allKeys.extend(theseKeys)
            if len(_scanner_t_allKeys):
                scanner_t.keys = _scanner_t_allKeys[-1].name  # just the last key pressed
                scanner_t.rt = _scanner_t_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if thisTrial['block_type'] != 'block_start' and thisTrial['block_type'] != 'null_block':
            continueRoutine = False
        
        
        
        # *fixation_wait_for_t* updates
        if fixation_wait_for_t.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_wait_for_t.frameNStart = frameN  # exact frame index
            fixation_wait_for_t.tStart = t  # local t and not account for scr refresh
            fixation_wait_for_t.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_wait_for_t, 'tStartRefresh')  # time at next scr refresh
            fixation_wait_for_t.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wait_for_tComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait_for_t"-------
    for thisComponent in wait_for_tComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if scanner_t.keys in ['', [], None]:  # No response was made
        scanner_t.keys = None
    trials.addData('scanner_t.keys',scanner_t.keys)
    if scanner_t.keys != None:  # we had a response
        trials.addData('scanner_t.rt', scanner_t.rt)
    trials.addData('scanner_t.started', scanner_t.tStartRefresh)
    trials.addData('scanner_t.stopped', scanner_t.tStopRefresh)
    trials.addData('fixation_wait_for_t.started', fixation_wait_for_t.tStartRefresh)
    trials.addData('fixation_wait_for_t.stopped', fixation_wait_for_t.tStopRefresh)
    # the Routine "wait_for_t" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    if thisTrial['block_type'] == 'null_block':
        image.opacity = 0
    else:
        image.opacity = 1
    
    
    trials.addData('real_timestamp_trial_start', datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
    
    
    image.setImage("localizer//stimuli//" + img_name)
    repeat_response.keys = []
    repeat_response.rt = []
    _repeat_response_allKeys = []
    # keep track of which components have finished
    trialComponents = [image, fixation, repeat_response]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if thisTrial['block_type'] == 'null_block':
            image.opacity = 0
            continueRoutine=False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + .3-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + .8-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *repeat_response* updates
        waitOnFlip = False
        if repeat_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeat_response.frameNStart = frameN  # exact frame index
            repeat_response.tStart = t  # local t and not account for scr refresh
            repeat_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_response, 'tStartRefresh')  # time at next scr refresh
            repeat_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(repeat_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(repeat_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if repeat_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > repeat_response.tStartRefresh + .8-frameTolerance:
                # keep track of stop time/frame for later
                repeat_response.tStop = t  # not accounting for scr refresh
                repeat_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(repeat_response, 'tStopRefresh')  # time at next scr refresh
                repeat_response.status = FINISHED
        if repeat_response.status == STARTED and not waitOnFlip:
            theseKeys = repeat_response.getKeys(keyList=['y'], waitRelease=False)
            _repeat_response_allKeys.extend(theseKeys)
            if len(_repeat_response_allKeys):
                repeat_response.keys = _repeat_response_allKeys[-1].name  # just the last key pressed
                repeat_response.rt = _repeat_response_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    # check responses
    if repeat_response.keys in ['', [], None]:  # No response was made
        repeat_response.keys = None
    trials.addData('repeat_response.keys',repeat_response.keys)
    if repeat_response.keys != None:  # we had a response
        trials.addData('repeat_response.rt', repeat_response.rt)
    trials.addData('repeat_response.started', repeat_response.tStartRefresh)
    trials.addData('repeat_response.stopped', repeat_response.tStopRefresh)
    
    # ------Prepare to start Routine "null_block"-------
    continueRoutine = True
    routineTimer.add(12.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    null_blockComponents = [fixation_null]
    for thisComponent in null_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    null_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "null_block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = null_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=null_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_null* updates
        if fixation_null.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_null.frameNStart = frameN  # exact frame index
            fixation_null.tStart = t  # local t and not account for scr refresh
            fixation_null.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_null, 'tStartRefresh')  # time at next scr refresh
            fixation_null.setAutoDraw(True)
        if fixation_null.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_null.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                fixation_null.tStop = t  # not accounting for scr refresh
                fixation_null.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_null, 'tStopRefresh')  # time at next scr refresh
                fixation_null.setAutoDraw(False)
        if thisTrial['block_type'] != 'null_block':
            continueRoutine=False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in null_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "null_block"-------
    for thisComponent in null_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation_null.started', fixation_null.tStartRefresh)
    trials.addData('fixation_null.stopped', fixation_null.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
