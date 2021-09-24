#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on September 24, 2021, at 14:58
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
expName = 'DSP_Encoding_Refresher'  # from the Builder filename that created this script
expInfo = {'participant': '', 'group': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['group'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Public\\Moore_fMRI\\DSP_PsychoPy\\DSP_Encoding_Refresher_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
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

# Initialize components for Routine "Stim_stuff"
Stim_stuffClock = core.Clock()
if expInfo['group'] == 'alt':
    learning = './DSP_Videos/Learning/Learning_Alternate.mp4'
elif expInfo['group'] == 'nor':
    learning = './DSP_Videos/Learning/Learning_Normal.mp4'

# Initialize components for Routine "Learning"
LearningClock = core.Clock()
from time import time
import datetime
Learning_instruction = visual.TextStim(win=win, name='Learning_instruction',
    text='Spatial Video!\n\nLearn the layout.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Learning_3 = visual.TextStim(win=win, name='Learning_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Learning_2 = visual.TextStim(win=win, name='Learning_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Learning_1 = visual.TextStim(win=win, name='Learning_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Learning_video = visual.MovieStim3(
    win=win, name='Learning_video',
    noAudio = True,
    filename=learning,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-5.0,
    )

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

# ------Prepare to start Routine "Stim_stuff"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Stim_stuffComponents = []
for thisComponent in Stim_stuffComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Stim_stuffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stim_stuff"-------
while continueRoutine:
    # get current time
    t = Stim_stuffClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stim_stuffClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stim_stuffComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stim_stuff"-------
for thisComponent in Stim_stuffComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Stim_stuff" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Learning"-------
continueRoutine = True
routineTimer.add(66.000000)
# update component parameters for each repeat
tic = time()
thisExp.addData("main_tasl_start", tic)
thisExp.addData("real_timestamp_main_task_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
# keep track of which components have finished
LearningComponents = [Learning_instruction, Learning_3, Learning_2, Learning_1, Learning_video]
for thisComponent in LearningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LearningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Learning"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = LearningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LearningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Learning_instruction* updates
    if Learning_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Learning_instruction.frameNStart = frameN  # exact frame index
        Learning_instruction.tStart = t  # local t and not account for scr refresh
        Learning_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_instruction, 'tStartRefresh')  # time at next scr refresh
        Learning_instruction.setAutoDraw(True)
    if Learning_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_instruction.tStop = t  # not accounting for scr refresh
            Learning_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_instruction, 'tStopRefresh')  # time at next scr refresh
            Learning_instruction.setAutoDraw(False)
    
    # *Learning_3* updates
    if Learning_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Learning_3.frameNStart = frameN  # exact frame index
        Learning_3.tStart = t  # local t and not account for scr refresh
        Learning_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3, 'tStartRefresh')  # time at next scr refresh
        Learning_3.setAutoDraw(True)
    if Learning_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3.tStop = t  # not accounting for scr refresh
            Learning_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3, 'tStopRefresh')  # time at next scr refresh
            Learning_3.setAutoDraw(False)
    
    # *Learning_2* updates
    if Learning_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Learning_2.frameNStart = frameN  # exact frame index
        Learning_2.tStart = t  # local t and not account for scr refresh
        Learning_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2, 'tStartRefresh')  # time at next scr refresh
        Learning_2.setAutoDraw(True)
    if Learning_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2.tStop = t  # not accounting for scr refresh
            Learning_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2, 'tStopRefresh')  # time at next scr refresh
            Learning_2.setAutoDraw(False)
    
    # *Learning_1* updates
    if Learning_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Learning_1.frameNStart = frameN  # exact frame index
        Learning_1.tStart = t  # local t and not account for scr refresh
        Learning_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1, 'tStartRefresh')  # time at next scr refresh
        Learning_1.setAutoDraw(True)
    if Learning_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1.tStop = t  # not accounting for scr refresh
            Learning_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1, 'tStopRefresh')  # time at next scr refresh
            Learning_1.setAutoDraw(False)
    
    # *Learning_video* updates
    if Learning_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Learning_video.frameNStart = frameN  # exact frame index
        Learning_video.tStart = t  # local t and not account for scr refresh
        Learning_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_video, 'tStartRefresh')  # time at next scr refresh
        Learning_video.setAutoDraw(True)
    if Learning_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Learning_video.tStop = t  # not accounting for scr refresh
            Learning_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_video, 'tStopRefresh')  # time at next scr refresh
            Learning_video.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LearningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Learning"-------
for thisComponent in LearningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Learning_instruction.started', Learning_instruction.tStartRefresh)
thisExp.addData('Learning_instruction.stopped', Learning_instruction.tStopRefresh)
thisExp.addData('Learning_3.started', Learning_3.tStartRefresh)
thisExp.addData('Learning_3.stopped', Learning_3.tStopRefresh)
thisExp.addData('Learning_2.started', Learning_2.tStartRefresh)
thisExp.addData('Learning_2.stopped', Learning_2.tStopRefresh)
thisExp.addData('Learning_1.started', Learning_1.tStartRefresh)
thisExp.addData('Learning_1.stopped', Learning_1.tStopRefresh)
Learning_video.stop()
thisExp.addData('learning_video_file', learning)
toc = time()
thisExp.addData("main_task_end", toc)
thisExp.addData("real_timestamp_main_task_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("main_task_duration", (toc - tic))


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
