#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on January 21, 2022, at 11:05
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
expName = 'DSP_Resting_State'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Public\\Moore_fMRI\\DSP_PsychoPy\\DSP_Resting_State_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[.4,.4,.4], colorSpace='rgb',
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
    text='Waiting for the experimenter…',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ready_experimenter_resp = keyboard.Keyboard()
win.mouseVisible = False

# Initialize components for Routine "Ready_scanner"
Ready_scannerClock = core.Clock()
Ready_scanner_text = visual.TextStim(win=win, name='Ready_scanner_text',
    text='Waiting for the scanner…',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ready_scanner_resp = keyboard.Keyboard()

# Initialize components for Routine "RS_fixation"
RS_fixationClock = core.Clock()
from time import time
import datetime
Fixation_horz = visual.Line(
    win=win, name='Fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5,     colorSpace='rgb',  lineColor='black', fillColor=[1,1,1],
    opacity=1, depth=-1.0, interpolate=True)
Fixation_vert = visual.Line(
    win=win, name='Fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5,     colorSpace='rgb',  lineColor='black', fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
Scan_done = keyboard.Keyboard()

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Done_text = visual.TextStim(win=win, name='Done_text',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Done_resp = keyboard.Keyboard()

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

# ------Prepare to start Routine "Ready_scanner"-------
continueRoutine = True
# update component parameters for each repeat
Ready_scanner_resp.keys = []
Ready_scanner_resp.rt = []
_Ready_scanner_resp_allKeys = []
# keep track of which components have finished
Ready_scannerComponents = [Ready_scanner_text, Ready_scanner_resp]
for thisComponent in Ready_scannerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Ready_scannerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Ready_scanner"-------
while continueRoutine:
    # get current time
    t = Ready_scannerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Ready_scannerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ready_scanner_text* updates
    if Ready_scanner_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ready_scanner_text.frameNStart = frameN  # exact frame index
        Ready_scanner_text.tStart = t  # local t and not account for scr refresh
        Ready_scanner_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ready_scanner_text, 'tStartRefresh')  # time at next scr refresh
        Ready_scanner_text.setAutoDraw(True)
    
    # *Ready_scanner_resp* updates
    waitOnFlip = False
    if Ready_scanner_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ready_scanner_resp.frameNStart = frameN  # exact frame index
        Ready_scanner_resp.tStart = t  # local t and not account for scr refresh
        Ready_scanner_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ready_scanner_resp, 'tStartRefresh')  # time at next scr refresh
        Ready_scanner_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Ready_scanner_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Ready_scanner_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Ready_scanner_resp.status == STARTED and not waitOnFlip:
        theseKeys = Ready_scanner_resp.getKeys(keyList=['t'], waitRelease=False)
        _Ready_scanner_resp_allKeys.extend(theseKeys)
        if len(_Ready_scanner_resp_allKeys):
            Ready_scanner_resp.keys = _Ready_scanner_resp_allKeys[-1].name  # just the last key pressed
            Ready_scanner_resp.rt = _Ready_scanner_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ready_scannerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ready_scanner"-------
for thisComponent in Ready_scannerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ready_scanner_text.started', Ready_scanner_text.tStartRefresh)
thisExp.addData('Ready_scanner_text.stopped', Ready_scanner_text.tStopRefresh)
# check responses
if Ready_scanner_resp.keys in ['', [], None]:  # No response was made
    Ready_scanner_resp.keys = None
thisExp.addData('Ready_scanner_resp.keys',Ready_scanner_resp.keys)
if Ready_scanner_resp.keys != None:  # we had a response
    thisExp.addData('Ready_scanner_resp.rt', Ready_scanner_resp.rt)
thisExp.addData('Ready_scanner_resp.started', Ready_scanner_resp.tStartRefresh)
thisExp.addData('Ready_scanner_resp.stopped', Ready_scanner_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Ready_scanner" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "RS_fixation"-------
continueRoutine = True
# update component parameters for each repeat
tic = time()
thisExp.addData("main_task_start", tic)
thisExp.addData("real_timestamp_main_task_start'", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
Scan_done.keys = []
Scan_done.rt = []
_Scan_done_allKeys = []
# keep track of which components have finished
RS_fixationComponents = [Fixation_horz, Fixation_vert, Scan_done]
for thisComponent in RS_fixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
RS_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "RS_fixation"-------
while continueRoutine:
    # get current time
    t = RS_fixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RS_fixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Fixation_horz* updates
    if Fixation_horz.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_horz.frameNStart = frameN  # exact frame index
        Fixation_horz.tStart = t  # local t and not account for scr refresh
        Fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Fixation_horz.setAutoDraw(True)
    
    # *Fixation_vert* updates
    if Fixation_vert.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_vert.frameNStart = frameN  # exact frame index
        Fixation_vert.tStart = t  # local t and not account for scr refresh
        Fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Fixation_vert.setAutoDraw(True)
    
    # *Scan_done* updates
    waitOnFlip = False
    if Scan_done.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Scan_done.frameNStart = frameN  # exact frame index
        Scan_done.tStart = t  # local t and not account for scr refresh
        Scan_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Scan_done, 'tStartRefresh')  # time at next scr refresh
        Scan_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Scan_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Scan_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Scan_done.status == STARTED and not waitOnFlip:
        theseKeys = Scan_done.getKeys(keyList=['enter', 'return'], waitRelease=False)
        _Scan_done_allKeys.extend(theseKeys)
        if len(_Scan_done_allKeys):
            Scan_done.keys = _Scan_done_allKeys[0].name  # just the first key pressed
            Scan_done.rt = _Scan_done_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RS_fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RS_fixation"-------
for thisComponent in RS_fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Fixation_horz.started', Fixation_horz.tStartRefresh)
thisExp.addData('Fixation_horz.stopped', Fixation_horz.tStopRefresh)
thisExp.addData('Fixation_vert.started', Fixation_vert.tStartRefresh)
thisExp.addData('Fixation_vert.stopped', Fixation_vert.tStopRefresh)
# check responses
if Scan_done.keys in ['', [], None]:  # No response was made
    Scan_done.keys = None
thisExp.addData('Scan_done.keys',Scan_done.keys)
if Scan_done.keys != None:  # we had a response
    thisExp.addData('Scan_done.rt', Scan_done.rt)
thisExp.addData('Scan_done.started', Scan_done.tStartRefresh)
thisExp.addData('Scan_done.stopped', Scan_done.tStopRefresh)
thisExp.nextEntry()
toc = time()
thisExp.addData("main_task_end", toc)
thisExp.addData("real_timestamp_main_task_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("main_task_duration", (toc - tic))

# the Routine "RS_fixation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Done"-------
continueRoutine = True
# update component parameters for each repeat
Done_resp.keys = []
Done_resp.rt = []
_Done_resp_allKeys = []
# keep track of which components have finished
DoneComponents = [Done_text, Done_resp]
for thisComponent in DoneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DoneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Done"-------
while continueRoutine:
    # get current time
    t = DoneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DoneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Done_text* updates
    if Done_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Done_text.frameNStart = frameN  # exact frame index
        Done_text.tStart = t  # local t and not account for scr refresh
        Done_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Done_text, 'tStartRefresh')  # time at next scr refresh
        Done_text.setAutoDraw(True)
    
    # *Done_resp* updates
    waitOnFlip = False
    if Done_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Done_resp.frameNStart = frameN  # exact frame index
        Done_resp.tStart = t  # local t and not account for scr refresh
        Done_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Done_resp, 'tStartRefresh')  # time at next scr refresh
        Done_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Done_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Done_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Done_resp.status == STARTED and not waitOnFlip:
        theseKeys = Done_resp.getKeys(keyList=['enter', 'return'], waitRelease=False)
        _Done_resp_allKeys.extend(theseKeys)
        if len(_Done_resp_allKeys):
            Done_resp.keys = _Done_resp_allKeys[0].name  # just the first key pressed
            Done_resp.rt = _Done_resp_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Done"-------
for thisComponent in DoneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Done_text.started', Done_text.tStartRefresh)
thisExp.addData('Done_text.stopped', Done_text.tStopRefresh)
# check responses
if Done_resp.keys in ['', [], None]:  # No response was made
    Done_resp.keys = None
thisExp.addData('Done_resp.keys',Done_resp.keys)
if Done_resp.keys != None:  # we had a response
    thisExp.addData('Done_resp.rt', Done_resp.rt)
thisExp.addData('Done_resp.started', Done_resp.tStartRefresh)
thisExp.addData('Done_resp.stopped', Done_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Done" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
