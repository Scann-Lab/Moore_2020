#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on February 03, 2022, at 10:21
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2.10')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'DSP_Bold'  # from the Builder filename that created this script
expInfo = {'participant': '', 'run': '', 'group': '', 'version': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s_%s' % (expInfo['participant'], expName, expInfo['run'], expInfo['group'], expInfo['version'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Public\\Moore_fMRI\\DSP_PsychoPy\\DSP_Bold_lastrun.py',
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

# Initialize components for Routine "Alignment"
AlignmentClock = core.Clock()
Alignment_background = visual.Rect(
    win=win, name='Alignment_background',
    width=(2,2)[0], height=(2,2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Alignment_image = visual.ImageStim(
    win=win,
    name='Alignment_image', 
    image='Alignment.png', mask=None,
    ori=0, pos=(0, 0), size=[1.4,1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
Alignment_resp = keyboard.Keyboard()

# Initialize components for Routine "Button_check"
Button_checkClock = core.Clock()
Button_text = visual.TextStim(win=win, name='Button_text',
    text='Button check.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Index"
IndexClock = core.Clock()
Index_text = visual.TextStim(win=win, name='Index_text',
    text='Press the button under your index finger.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Index_resp = keyboard.Keyboard()

# Initialize components for Routine "Middle"
MiddleClock = core.Clock()
Middle_text = visual.TextStim(win=win, name='Middle_text',
    text='Press the button under your middle finger.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
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

# Initialize components for Routine "Stim_stuff"
Stim_stuffClock = core.Clock()
if expInfo['group'] == 'alt':
    learning = './DSP_Videos/Learning/Learning_Alternate.mp4'
elif expInfo['group'] == 'nor':
    learning = './DSP_Videos/Learning/Learning_Normal.mp4'
import xlrd

if expInfo['group'] == 'alt' and expInfo['version'] == 'A':
    Control_Alternate_A = 'Control_Alternate_A.xlsx'
    workbook = xlrd.open_workbook(Control_Alternate_A)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'alt' and expInfo['version'] == 'B':
    Control_Alternate_B = 'Control_Alternate_B.xlsx'
    workbook = xlrd.open_workbook(Control_Alternate_B)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'alt' and expInfo['version'] == 'C':
    Control_Alternate_C = 'Control_Alternate_C.xlsx'
    workbook = xlrd.open_workbook(Control_Alternate_C)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'alt' and expInfo['version'] == 'D':
    Control_Alternate_D = 'Control_Alternate_D.xlsx'
    workbook = xlrd.open_workbook(Control_Alternate_D)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'nor' and expInfo['version'] == 'A':
    Control_Normal_A = 'Control_Normal_A.xlsx'
    workbook = xlrd.open_workbook(Control_Normal_A)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'nor' and expInfo['version'] == 'B':
    Control_Normal_B = 'Control_Normal_B.xlsx'
    workbook = xlrd.open_workbook(Control_Normal_B)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'nor' and expInfo['version'] == 'C':
    Control_Normal_C = 'Control_Normal_C.xlsx'
    workbook = xlrd.open_workbook(Control_Normal_C)
    worksheet = workbook.sheet_by_index(0)
elif expInfo['group'] == 'nor' and expInfo['version'] == 'D':
    Control_Normal_D = 'Control_Normal_D.xlsx'
    workbook = xlrd.open_workbook(Control_Normal_D)
    worksheet = workbook.sheet_by_index(0)

control_videos = []

for rowx in range(1, 9):
    row = worksheet.row_values(rowx)
    control_videos.append(row[0])

if expInfo['run'] == '1':
    control_1 = control_videos[0]
    control_2 = control_videos[1]
elif expInfo['run'] == '2':
    control_1 = control_videos[2]
    control_2 = control_videos[3]
elif expInfo['run'] == '3':
    control_1 = control_videos[4]
    control_2 = control_videos[5]
elif expInfo['run'] == '4':
    control_1 = control_videos[6]
    control_2 = control_videos[7]

# Initialize components for Routine "Ready_scanner"
Ready_scannerClock = core.Clock()
from time import time
import datetime
Ready_scanner_text = visual.TextStim(win=win, name='Ready_scanner_text',
    text='Waiting for the scanner…',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Ready_scanner_resp = keyboard.Keyboard()

# Initialize components for Routine "Learning_1"
Learning_1Clock = core.Clock()
Learning_1_instruction = visual.TextStim(win=win, name='Learning_1_instruction',
    text='Spatial Video!\n\nLearn the layout.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Learning_1_3 = visual.TextStim(win=win, name='Learning_1_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Learning_1_2 = visual.TextStim(win=win, name='Learning_1_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Learning_1_1 = visual.TextStim(win=win, name='Learning_1_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Learning_1_video = visual.MovieStim3(
    win=win, name='Learning_1_video',
    noAudio = True,
    filename=learning,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-5.0,
    )
Learning_1_fixation_horz = visual.Line(
    win=win, name='Learning_1_fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Learning_1_fixation_vert = visual.Line(
    win=win, name='Learning_1_fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "Control_1"
Control_1Clock = core.Clock()
Control_1_instruction = visual.TextStim(win=win, name='Control_1_instruction',
    text='Color Video!\n\nDo the first and last balls match?',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Control_1_3 = visual.TextStim(win=win, name='Control_1_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Control_1_2 = visual.TextStim(win=win, name='Control_1_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Control_1_1 = visual.TextStim(win=win, name='Control_1_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Control_1_video = visual.MovieStim3(
    win=win, name='Control_1_video',
    noAudio = False,
    filename=control_1,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-6.0,
    )
Control_1_resp = keyboard.Keyboard()
Control_1_same_different_text = visual.TextStim(win=win, name='Control_1_same_different_text',
    text='Same or different color?',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Control_1_resp_recorded_text = visual.TextStim(win=win, name='Control_1_resp_recorded_text',
    text='Response recorded!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
Control_1_fixation_horz = visual.Line(
    win=win, name='Control_1_fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
Control_1_fixation_vert = visual.Line(
    win=win, name='Control_1_fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)

# Initialize components for Routine "Learning_2"
Learning_2Clock = core.Clock()
Learning_2_instruction = visual.TextStim(win=win, name='Learning_2_instruction',
    text='Spatial Video!\n\nLearn the layout.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Learning_2_3 = visual.TextStim(win=win, name='Learning_2_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Learning_2_2 = visual.TextStim(win=win, name='Learning_2_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Learning_2_1 = visual.TextStim(win=win, name='Learning_2_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Learning_2_video = visual.MovieStim3(
    win=win, name='Learning_2_video',
    noAudio = False,
    filename=learning,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-5.0,
    )
Learning_2_fixation_horz = visual.Line(
    win=win, name='Learning_2_fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Learning_2_fixation_vert = visual.Line(
    win=win, name='Learning_2_fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "Control_2"
Control_2Clock = core.Clock()
Control_2_instruction = visual.TextStim(win=win, name='Control_2_instruction',
    text='Color Video!\n\nDo the first and last balls match?',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Control_2_3 = visual.TextStim(win=win, name='Control_2_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Control_2_2 = visual.TextStim(win=win, name='Control_2_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Control_2_1 = visual.TextStim(win=win, name='Control_2_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Control_2_video = visual.MovieStim3(
    win=win, name='Control_2_video',
    noAudio = False,
    filename=control_2,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-6.0,
    )
Control_2_resp = keyboard.Keyboard()
Control_2_same_different_text = visual.TextStim(win=win, name='Control_2_same_different_text',
    text='Same or different color?',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Control_2_resp_recorded_text = visual.TextStim(win=win, name='Control_2_resp_recorded_text',
    text='Response recorded!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
Control_2_fixation_horz = visual.Line(
    win=win, name='Control_2_fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
Control_2_fixation_vert = visual.Line(
    win=win, name='Control_2_fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)

# Initialize components for Routine "Learning_3"
Learning_3Clock = core.Clock()
Learning_3_instruction = visual.TextStim(win=win, name='Learning_3_instruction',
    text='Spatial Video!\n\nLearn the layout.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Learning_3_3 = visual.TextStim(win=win, name='Learning_3_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Learning_3_2 = visual.TextStim(win=win, name='Learning_3_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Learning_3_1 = visual.TextStim(win=win, name='Learning_3_1',
    text='1',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Learning_3_video = visual.MovieStim3(
    win=win, name='Learning_3_video',
    noAudio = False,
    filename=learning,
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=-5.0,
    )
Learning_3_fixation_horz = visual.Line(
    win=win, name='Learning_3_fixation_horz',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Learning_3_fixation_vert = visual.Line(
    win=win, name='Learning_3_fixation_vert',
    start=(-(0.075, 0)[0]/2.0, 0), end=(+(0.075, 0)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Done_text = visual.TextStim(win=win, name='Done_text',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
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
    if expInfo['run'] > '1':
        continueRoutine = False    
    
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
            if tThisFlipGlobal > Button_text.tStartRefresh + 1-frameTolerance:
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
        if Index_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
        if Middle_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
tic = time()
thisExp.addData("main_task_start", tic)
thisExp.addData("real_timestamp_main_task_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
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

# ------Prepare to start Routine "Learning_1"-------
continueRoutine = True
routineTimer.add(81.000000)
# update component parameters for each repeat
tic_learning_1 = time()
thisExp.addData("Learning_1_start", tic_learning_1)
thisExp.addData("real_timestamp_learning_1_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
# keep track of which components have finished
Learning_1Components = [Learning_1_instruction, Learning_1_3, Learning_1_2, Learning_1_1, Learning_1_video, Learning_1_fixation_horz, Learning_1_fixation_vert]
for thisComponent in Learning_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Learning_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Learning_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Learning_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Learning_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Learning_1_instruction* updates
    if Learning_1_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_instruction.frameNStart = frameN  # exact frame index
        Learning_1_instruction.tStart = t  # local t and not account for scr refresh
        Learning_1_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_instruction, 'tStartRefresh')  # time at next scr refresh
        Learning_1_instruction.setAutoDraw(True)
    if Learning_1_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_instruction.tStop = t  # not accounting for scr refresh
            Learning_1_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_instruction, 'tStopRefresh')  # time at next scr refresh
            Learning_1_instruction.setAutoDraw(False)
    
    # *Learning_1_3* updates
    if Learning_1_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_3.frameNStart = frameN  # exact frame index
        Learning_1_3.tStart = t  # local t and not account for scr refresh
        Learning_1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_3, 'tStartRefresh')  # time at next scr refresh
        Learning_1_3.setAutoDraw(True)
    if Learning_1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_3.tStop = t  # not accounting for scr refresh
            Learning_1_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_3, 'tStopRefresh')  # time at next scr refresh
            Learning_1_3.setAutoDraw(False)
    
    # *Learning_1_2* updates
    if Learning_1_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_2.frameNStart = frameN  # exact frame index
        Learning_1_2.tStart = t  # local t and not account for scr refresh
        Learning_1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_2, 'tStartRefresh')  # time at next scr refresh
        Learning_1_2.setAutoDraw(True)
    if Learning_1_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_2.tStop = t  # not accounting for scr refresh
            Learning_1_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_2, 'tStopRefresh')  # time at next scr refresh
            Learning_1_2.setAutoDraw(False)
    
    # *Learning_1_1* updates
    if Learning_1_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_1.frameNStart = frameN  # exact frame index
        Learning_1_1.tStart = t  # local t and not account for scr refresh
        Learning_1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_1, 'tStartRefresh')  # time at next scr refresh
        Learning_1_1.setAutoDraw(True)
    if Learning_1_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_1.tStop = t  # not accounting for scr refresh
            Learning_1_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_1, 'tStopRefresh')  # time at next scr refresh
            Learning_1_1.setAutoDraw(False)
    
    # *Learning_1_video* updates
    if Learning_1_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_video.frameNStart = frameN  # exact frame index
        Learning_1_video.tStart = t  # local t and not account for scr refresh
        Learning_1_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_video, 'tStartRefresh')  # time at next scr refresh
        Learning_1_video.setAutoDraw(True)
    if Learning_1_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_video.tStop = t  # not accounting for scr refresh
            Learning_1_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_video, 'tStopRefresh')  # time at next scr refresh
            Learning_1_video.setAutoDraw(False)
    
    # *Learning_1_fixation_horz* updates
    if Learning_1_fixation_horz.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_fixation_horz.frameNStart = frameN  # exact frame index
        Learning_1_fixation_horz.tStart = t  # local t and not account for scr refresh
        Learning_1_fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Learning_1_fixation_horz.setAutoDraw(True)
    if Learning_1_fixation_horz.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_fixation_horz.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_fixation_horz.tStop = t  # not accounting for scr refresh
            Learning_1_fixation_horz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_fixation_horz, 'tStopRefresh')  # time at next scr refresh
            Learning_1_fixation_horz.setAutoDraw(False)
    
    # *Learning_1_fixation_vert* updates
    if Learning_1_fixation_vert.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_1_fixation_vert.frameNStart = frameN  # exact frame index
        Learning_1_fixation_vert.tStart = t  # local t and not account for scr refresh
        Learning_1_fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_1_fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Learning_1_fixation_vert.setAutoDraw(True)
    if Learning_1_fixation_vert.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_1_fixation_vert.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_1_fixation_vert.tStop = t  # not accounting for scr refresh
            Learning_1_fixation_vert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_1_fixation_vert, 'tStopRefresh')  # time at next scr refresh
            Learning_1_fixation_vert.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Learning_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Learning_1"-------
for thisComponent in Learning_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
toc_learning_1 = time()
thisExp.addData("learning_1_end", toc_learning_1)
thisExp.addData("real_timestamp_learning_1_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("learning_1_duration", (toc_learning_1 - tic_learning_1))
thisExp.addData('Learning_1_instruction.started', Learning_1_instruction.tStartRefresh)
thisExp.addData('Learning_1_instruction.stopped', Learning_1_instruction.tStopRefresh)
thisExp.addData('Learning_1_3.started', Learning_1_3.tStartRefresh)
thisExp.addData('Learning_1_3.stopped', Learning_1_3.tStopRefresh)
thisExp.addData('Learning_1_2.started', Learning_1_2.tStartRefresh)
thisExp.addData('Learning_1_2.stopped', Learning_1_2.tStopRefresh)
thisExp.addData('Learning_1_1.started', Learning_1_1.tStartRefresh)
thisExp.addData('Learning_1_1.stopped', Learning_1_1.tStopRefresh)
Learning_1_video.stop()
thisExp.addData('Learning_1_fixation_horz.started', Learning_1_fixation_horz.tStartRefresh)
thisExp.addData('Learning_1_fixation_horz.stopped', Learning_1_fixation_horz.tStopRefresh)
thisExp.addData('Learning_1_fixation_vert.started', Learning_1_fixation_vert.tStartRefresh)
thisExp.addData('Learning_1_fixation_vert.stopped', Learning_1_fixation_vert.tStopRefresh)
thisExp.addData('learning_video_file_1', learning)

# ------Prepare to start Routine "Control_1"-------
continueRoutine = True
# update component parameters for each repeat
componentStop = False
event.clearEvents(eventType = 'keyboard')
tic_control_1 = time()
thisExp.addData("control_1_start", tic_control_1)
thisExp.addData("real_timestamp_control_1_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
Control_1_resp.keys = []
Control_1_resp.rt = []
_Control_1_resp_allKeys = []
# keep track of which components have finished
Control_1Components = [Control_1_instruction, Control_1_3, Control_1_2, Control_1_1, Control_1_video, Control_1_resp, Control_1_same_different_text, Control_1_resp_recorded_text, Control_1_fixation_horz, Control_1_fixation_vert]
for thisComponent in Control_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Control_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Control_1"-------
while continueRoutine:
    # get current time
    t = Control_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Control_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (Control_1_resp.keys is not None and len(Control_1_resp.keys) > 0 and t > 66) or t >= 76:
        componentStop = True
    
    # *Control_1_instruction* updates
    if Control_1_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Control_1_instruction.frameNStart = frameN  # exact frame index
        Control_1_instruction.tStart = t  # local t and not account for scr refresh
        Control_1_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_instruction, 'tStartRefresh')  # time at next scr refresh
        Control_1_instruction.setAutoDraw(True)
    if Control_1_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_instruction.tStop = t  # not accounting for scr refresh
            Control_1_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_instruction, 'tStopRefresh')  # time at next scr refresh
            Control_1_instruction.setAutoDraw(False)
    
    # *Control_1_3* updates
    if Control_1_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Control_1_3.frameNStart = frameN  # exact frame index
        Control_1_3.tStart = t  # local t and not account for scr refresh
        Control_1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_3, 'tStartRefresh')  # time at next scr refresh
        Control_1_3.setAutoDraw(True)
    if Control_1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_3.tStop = t  # not accounting for scr refresh
            Control_1_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_3, 'tStopRefresh')  # time at next scr refresh
            Control_1_3.setAutoDraw(False)
    
    # *Control_1_2* updates
    if Control_1_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Control_1_2.frameNStart = frameN  # exact frame index
        Control_1_2.tStart = t  # local t and not account for scr refresh
        Control_1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_2, 'tStartRefresh')  # time at next scr refresh
        Control_1_2.setAutoDraw(True)
    if Control_1_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_2.tStop = t  # not accounting for scr refresh
            Control_1_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_2, 'tStopRefresh')  # time at next scr refresh
            Control_1_2.setAutoDraw(False)
    
    # *Control_1_1* updates
    if Control_1_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Control_1_1.frameNStart = frameN  # exact frame index
        Control_1_1.tStart = t  # local t and not account for scr refresh
        Control_1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_1, 'tStartRefresh')  # time at next scr refresh
        Control_1_1.setAutoDraw(True)
    if Control_1_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_1.tStop = t  # not accounting for scr refresh
            Control_1_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_1, 'tStopRefresh')  # time at next scr refresh
            Control_1_1.setAutoDraw(False)
    
    # *Control_1_video* updates
    if Control_1_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Control_1_video.frameNStart = frameN  # exact frame index
        Control_1_video.tStart = t  # local t and not account for scr refresh
        Control_1_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_video, 'tStartRefresh')  # time at next scr refresh
        Control_1_video.setAutoDraw(True)
    if Control_1_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_video.tStop = t  # not accounting for scr refresh
            Control_1_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_video, 'tStopRefresh')  # time at next scr refresh
            Control_1_video.setAutoDraw(False)
    
    # *Control_1_resp* updates
    waitOnFlip = False
    if Control_1_resp.status == NOT_STARTED and tThisFlip >= 66.0-frameTolerance:
        # keep track of start time/frame for later
        Control_1_resp.frameNStart = frameN  # exact frame index
        Control_1_resp.tStart = t  # local t and not account for scr refresh
        Control_1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_resp, 'tStartRefresh')  # time at next scr refresh
        Control_1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Control_1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Control_1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Control_1_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_1_resp.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_resp.tStop = t  # not accounting for scr refresh
            Control_1_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_resp, 'tStopRefresh')  # time at next scr refresh
            Control_1_resp.status = FINISHED
    if Control_1_resp.status == STARTED and not waitOnFlip:
        theseKeys = Control_1_resp.getKeys(keyList=['y', 'b'], waitRelease=False)
        _Control_1_resp_allKeys.extend(theseKeys)
        if len(_Control_1_resp_allKeys):
            Control_1_resp.keys = _Control_1_resp_allKeys[0].name  # just the first key pressed
            Control_1_resp.rt = _Control_1_resp_allKeys[0].rt
    
    # *Control_1_same_different_text* updates
    if Control_1_same_different_text.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Control_1_same_different_text.frameNStart = frameN  # exact frame index
        Control_1_same_different_text.tStart = t  # local t and not account for scr refresh
        Control_1_same_different_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_same_different_text, 'tStartRefresh')  # time at next scr refresh
        Control_1_same_different_text.setAutoDraw(True)
    if Control_1_same_different_text.status == STARTED:
        if bool(componentStop):
            # keep track of stop time/frame for later
            Control_1_same_different_text.tStop = t  # not accounting for scr refresh
            Control_1_same_different_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_same_different_text, 'tStopRefresh')  # time at next scr refresh
            Control_1_same_different_text.setAutoDraw(False)
    
    # *Control_1_resp_recorded_text* updates
    if Control_1_resp_recorded_text.status == NOT_STARTED and componentStop:
        # keep track of start time/frame for later
        Control_1_resp_recorded_text.frameNStart = frameN  # exact frame index
        Control_1_resp_recorded_text.tStart = t  # local t and not account for scr refresh
        Control_1_resp_recorded_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_resp_recorded_text, 'tStartRefresh')  # time at next scr refresh
        Control_1_resp_recorded_text.setAutoDraw(True)
    if Control_1_resp_recorded_text.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 76-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_resp_recorded_text.tStop = t  # not accounting for scr refresh
            Control_1_resp_recorded_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_resp_recorded_text, 'tStopRefresh')  # time at next scr refresh
            Control_1_resp_recorded_text.setAutoDraw(False)
    
    # *Control_1_fixation_horz* updates
    if Control_1_fixation_horz.status == NOT_STARTED and tThisFlip >= 76-frameTolerance:
        # keep track of start time/frame for later
        Control_1_fixation_horz.frameNStart = frameN  # exact frame index
        Control_1_fixation_horz.tStart = t  # local t and not account for scr refresh
        Control_1_fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Control_1_fixation_horz.setAutoDraw(True)
    if Control_1_fixation_horz.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 91-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_fixation_horz.tStop = t  # not accounting for scr refresh
            Control_1_fixation_horz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_fixation_horz, 'tStopRefresh')  # time at next scr refresh
            Control_1_fixation_horz.setAutoDraw(False)
    
    # *Control_1_fixation_vert* updates
    if Control_1_fixation_vert.status == NOT_STARTED and tThisFlip >= 76-frameTolerance:
        # keep track of start time/frame for later
        Control_1_fixation_vert.frameNStart = frameN  # exact frame index
        Control_1_fixation_vert.tStart = t  # local t and not account for scr refresh
        Control_1_fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_1_fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Control_1_fixation_vert.setAutoDraw(True)
    if Control_1_fixation_vert.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 91-frameTolerance:
            # keep track of stop time/frame for later
            Control_1_fixation_vert.tStop = t  # not accounting for scr refresh
            Control_1_fixation_vert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_1_fixation_vert, 'tStopRefresh')  # time at next scr refresh
            Control_1_fixation_vert.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Control_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Control_1"-------
for thisComponent in Control_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
toc_control_1 = time()
thisExp.addData("control_1_end", toc_control_1)
thisExp.addData("real_timestamp_control_1_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("control_1_duration", (toc_control_1 - tic_control_1))
thisExp.addData('Control_1_instruction.started', Control_1_instruction.tStartRefresh)
thisExp.addData('Control_1_instruction.stopped', Control_1_instruction.tStopRefresh)
thisExp.addData('Control_1_3.started', Control_1_3.tStartRefresh)
thisExp.addData('Control_1_3.stopped', Control_1_3.tStopRefresh)
thisExp.addData('Control_1_2.started', Control_1_2.tStartRefresh)
thisExp.addData('Control_1_2.stopped', Control_1_2.tStopRefresh)
thisExp.addData('Control_1_1.started', Control_1_1.tStartRefresh)
thisExp.addData('Control_1_1.stopped', Control_1_1.tStopRefresh)
Control_1_video.stop()
# check responses
if Control_1_resp.keys in ['', [], None]:  # No response was made
    Control_1_resp.keys = None
thisExp.addData('Control_1_resp.keys',Control_1_resp.keys)
if Control_1_resp.keys != None:  # we had a response
    thisExp.addData('Control_1_resp.rt', Control_1_resp.rt)
thisExp.addData('Control_1_resp.started', Control_1_resp.tStartRefresh)
thisExp.addData('Control_1_resp.stopped', Control_1_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Control_1_same_different_text.started', Control_1_same_different_text.tStartRefresh)
thisExp.addData('Control_1_same_different_text.stopped', Control_1_same_different_text.tStopRefresh)
thisExp.addData('Control_1_resp_recorded_text.started', Control_1_resp_recorded_text.tStartRefresh)
thisExp.addData('Control_1_resp_recorded_text.stopped', Control_1_resp_recorded_text.tStopRefresh)
thisExp.addData('Control_1_fixation_horz.started', Control_1_fixation_horz.tStartRefresh)
thisExp.addData('Control_1_fixation_horz.stopped', Control_1_fixation_horz.tStopRefresh)
thisExp.addData('Control_1_fixation_vert.started', Control_1_fixation_vert.tStartRefresh)
thisExp.addData('Control_1_fixation_vert.stopped', Control_1_fixation_vert.tStopRefresh)
thisExp.addData('control_video_file_1', control_1)
# the Routine "Control_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Learning_2"-------
continueRoutine = True
routineTimer.add(81.000000)
# update component parameters for each repeat
tic_learning_2 = time()
thisExp.addData("Learning_2_start", tic_learning_2)
thisExp.addData("real_timestamp_learning_2_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
# keep track of which components have finished
Learning_2Components = [Learning_2_instruction, Learning_2_3, Learning_2_2, Learning_2_1, Learning_2_video, Learning_2_fixation_horz, Learning_2_fixation_vert]
for thisComponent in Learning_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Learning_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Learning_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Learning_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Learning_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Learning_2_instruction* updates
    if Learning_2_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_instruction.frameNStart = frameN  # exact frame index
        Learning_2_instruction.tStart = t  # local t and not account for scr refresh
        Learning_2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_instruction, 'tStartRefresh')  # time at next scr refresh
        Learning_2_instruction.setAutoDraw(True)
    if Learning_2_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_instruction.tStop = t  # not accounting for scr refresh
            Learning_2_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_instruction, 'tStopRefresh')  # time at next scr refresh
            Learning_2_instruction.setAutoDraw(False)
    
    # *Learning_2_3* updates
    if Learning_2_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_3.frameNStart = frameN  # exact frame index
        Learning_2_3.tStart = t  # local t and not account for scr refresh
        Learning_2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_3, 'tStartRefresh')  # time at next scr refresh
        Learning_2_3.setAutoDraw(True)
    if Learning_2_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_3.tStop = t  # not accounting for scr refresh
            Learning_2_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_3, 'tStopRefresh')  # time at next scr refresh
            Learning_2_3.setAutoDraw(False)
    
    # *Learning_2_2* updates
    if Learning_2_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_2.frameNStart = frameN  # exact frame index
        Learning_2_2.tStart = t  # local t and not account for scr refresh
        Learning_2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_2, 'tStartRefresh')  # time at next scr refresh
        Learning_2_2.setAutoDraw(True)
    if Learning_2_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_2.tStop = t  # not accounting for scr refresh
            Learning_2_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_2, 'tStopRefresh')  # time at next scr refresh
            Learning_2_2.setAutoDraw(False)
    
    # *Learning_2_1* updates
    if Learning_2_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_1.frameNStart = frameN  # exact frame index
        Learning_2_1.tStart = t  # local t and not account for scr refresh
        Learning_2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_1, 'tStartRefresh')  # time at next scr refresh
        Learning_2_1.setAutoDraw(True)
    if Learning_2_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_1.tStop = t  # not accounting for scr refresh
            Learning_2_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_1, 'tStopRefresh')  # time at next scr refresh
            Learning_2_1.setAutoDraw(False)
    
    # *Learning_2_video* updates
    if Learning_2_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_video.frameNStart = frameN  # exact frame index
        Learning_2_video.tStart = t  # local t and not account for scr refresh
        Learning_2_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_video, 'tStartRefresh')  # time at next scr refresh
        Learning_2_video.setAutoDraw(True)
    if Learning_2_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_video.tStop = t  # not accounting for scr refresh
            Learning_2_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_video, 'tStopRefresh')  # time at next scr refresh
            Learning_2_video.setAutoDraw(False)
    
    # *Learning_2_fixation_horz* updates
    if Learning_2_fixation_horz.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_fixation_horz.frameNStart = frameN  # exact frame index
        Learning_2_fixation_horz.tStart = t  # local t and not account for scr refresh
        Learning_2_fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Learning_2_fixation_horz.setAutoDraw(True)
    if Learning_2_fixation_horz.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_fixation_horz.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_fixation_horz.tStop = t  # not accounting for scr refresh
            Learning_2_fixation_horz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_fixation_horz, 'tStopRefresh')  # time at next scr refresh
            Learning_2_fixation_horz.setAutoDraw(False)
    
    # *Learning_2_fixation_vert* updates
    if Learning_2_fixation_vert.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_2_fixation_vert.frameNStart = frameN  # exact frame index
        Learning_2_fixation_vert.tStart = t  # local t and not account for scr refresh
        Learning_2_fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_2_fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Learning_2_fixation_vert.setAutoDraw(True)
    if Learning_2_fixation_vert.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_2_fixation_vert.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_2_fixation_vert.tStop = t  # not accounting for scr refresh
            Learning_2_fixation_vert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_2_fixation_vert, 'tStopRefresh')  # time at next scr refresh
            Learning_2_fixation_vert.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Learning_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Learning_2"-------
for thisComponent in Learning_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
toc_learning_2 = time()
thisExp.addData("learning_2_end", toc_learning_2)
thisExp.addData("real_timestamp_learning_2_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("learning_2_duration", (toc_learning_2 - tic_learning_2))
thisExp.addData('Learning_2_instruction.started', Learning_2_instruction.tStartRefresh)
thisExp.addData('Learning_2_instruction.stopped', Learning_2_instruction.tStopRefresh)
thisExp.addData('Learning_2_3.started', Learning_2_3.tStartRefresh)
thisExp.addData('Learning_2_3.stopped', Learning_2_3.tStopRefresh)
thisExp.addData('Learning_2_2.started', Learning_2_2.tStartRefresh)
thisExp.addData('Learning_2_2.stopped', Learning_2_2.tStopRefresh)
thisExp.addData('Learning_2_1.started', Learning_2_1.tStartRefresh)
thisExp.addData('Learning_2_1.stopped', Learning_2_1.tStopRefresh)
Learning_2_video.stop()
thisExp.addData('Learning_2_fixation_horz.started', Learning_2_fixation_horz.tStartRefresh)
thisExp.addData('Learning_2_fixation_horz.stopped', Learning_2_fixation_horz.tStopRefresh)
thisExp.addData('Learning_2_fixation_vert.started', Learning_2_fixation_vert.tStartRefresh)
thisExp.addData('Learning_2_fixation_vert.stopped', Learning_2_fixation_vert.tStopRefresh)
thisExp.addData('learning_video_file_2', learning)

# ------Prepare to start Routine "Control_2"-------
continueRoutine = True
# update component parameters for each repeat
componentStop = False
event.clearEvents(eventType = 'keyboard')
tic_control_2 = time()
thisExp.addData("control_2_start", tic_control_2)
thisExp.addData("real_timestamp_control_2_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
Control_2_resp.keys = []
Control_2_resp.rt = []
_Control_2_resp_allKeys = []
# keep track of which components have finished
Control_2Components = [Control_2_instruction, Control_2_3, Control_2_2, Control_2_1, Control_2_video, Control_2_resp, Control_2_same_different_text, Control_2_resp_recorded_text, Control_2_fixation_horz, Control_2_fixation_vert]
for thisComponent in Control_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Control_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Control_2"-------
while continueRoutine:
    # get current time
    t = Control_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Control_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (Control_2_resp.keys is not None and len(Control_2_resp.keys) > 0 and t > 66) or t >= 76:
        componentStop = True
    
    # *Control_2_instruction* updates
    if Control_2_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Control_2_instruction.frameNStart = frameN  # exact frame index
        Control_2_instruction.tStart = t  # local t and not account for scr refresh
        Control_2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_instruction, 'tStartRefresh')  # time at next scr refresh
        Control_2_instruction.setAutoDraw(True)
    if Control_2_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_instruction.tStop = t  # not accounting for scr refresh
            Control_2_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_instruction, 'tStopRefresh')  # time at next scr refresh
            Control_2_instruction.setAutoDraw(False)
    
    # *Control_2_3* updates
    if Control_2_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Control_2_3.frameNStart = frameN  # exact frame index
        Control_2_3.tStart = t  # local t and not account for scr refresh
        Control_2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_3, 'tStartRefresh')  # time at next scr refresh
        Control_2_3.setAutoDraw(True)
    if Control_2_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_3.tStop = t  # not accounting for scr refresh
            Control_2_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_3, 'tStopRefresh')  # time at next scr refresh
            Control_2_3.setAutoDraw(False)
    
    # *Control_2_2* updates
    if Control_2_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Control_2_2.frameNStart = frameN  # exact frame index
        Control_2_2.tStart = t  # local t and not account for scr refresh
        Control_2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_2, 'tStartRefresh')  # time at next scr refresh
        Control_2_2.setAutoDraw(True)
    if Control_2_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_2.tStop = t  # not accounting for scr refresh
            Control_2_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_2, 'tStopRefresh')  # time at next scr refresh
            Control_2_2.setAutoDraw(False)
    
    # *Control_2_1* updates
    if Control_2_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Control_2_1.frameNStart = frameN  # exact frame index
        Control_2_1.tStart = t  # local t and not account for scr refresh
        Control_2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_1, 'tStartRefresh')  # time at next scr refresh
        Control_2_1.setAutoDraw(True)
    if Control_2_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_1.tStop = t  # not accounting for scr refresh
            Control_2_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_1, 'tStopRefresh')  # time at next scr refresh
            Control_2_1.setAutoDraw(False)
    
    # *Control_2_video* updates
    if Control_2_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Control_2_video.frameNStart = frameN  # exact frame index
        Control_2_video.tStart = t  # local t and not account for scr refresh
        Control_2_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_video, 'tStartRefresh')  # time at next scr refresh
        Control_2_video.setAutoDraw(True)
    if Control_2_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_video.tStop = t  # not accounting for scr refresh
            Control_2_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_video, 'tStopRefresh')  # time at next scr refresh
            Control_2_video.setAutoDraw(False)
    
    # *Control_2_resp* updates
    waitOnFlip = False
    if Control_2_resp.status == NOT_STARTED and tThisFlip >= 66.0-frameTolerance:
        # keep track of start time/frame for later
        Control_2_resp.frameNStart = frameN  # exact frame index
        Control_2_resp.tStart = t  # local t and not account for scr refresh
        Control_2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_resp, 'tStartRefresh')  # time at next scr refresh
        Control_2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Control_2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Control_2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Control_2_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Control_2_resp.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_resp.tStop = t  # not accounting for scr refresh
            Control_2_resp.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_resp, 'tStopRefresh')  # time at next scr refresh
            Control_2_resp.status = FINISHED
    if Control_2_resp.status == STARTED and not waitOnFlip:
        theseKeys = Control_2_resp.getKeys(keyList=['y', 'b'], waitRelease=False)
        _Control_2_resp_allKeys.extend(theseKeys)
        if len(_Control_2_resp_allKeys):
            Control_2_resp.keys = _Control_2_resp_allKeys[0].name  # just the first key pressed
            Control_2_resp.rt = _Control_2_resp_allKeys[0].rt
    
    # *Control_2_same_different_text* updates
    if Control_2_same_different_text.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Control_2_same_different_text.frameNStart = frameN  # exact frame index
        Control_2_same_different_text.tStart = t  # local t and not account for scr refresh
        Control_2_same_different_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_same_different_text, 'tStartRefresh')  # time at next scr refresh
        Control_2_same_different_text.setAutoDraw(True)
    if Control_2_same_different_text.status == STARTED:
        if bool(componentStop):
            # keep track of stop time/frame for later
            Control_2_same_different_text.tStop = t  # not accounting for scr refresh
            Control_2_same_different_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_same_different_text, 'tStopRefresh')  # time at next scr refresh
            Control_2_same_different_text.setAutoDraw(False)
    
    # *Control_2_resp_recorded_text* updates
    if Control_2_resp_recorded_text.status == NOT_STARTED and componentStop:
        # keep track of start time/frame for later
        Control_2_resp_recorded_text.frameNStart = frameN  # exact frame index
        Control_2_resp_recorded_text.tStart = t  # local t and not account for scr refresh
        Control_2_resp_recorded_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_resp_recorded_text, 'tStartRefresh')  # time at next scr refresh
        Control_2_resp_recorded_text.setAutoDraw(True)
    if Control_2_resp_recorded_text.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 76-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_resp_recorded_text.tStop = t  # not accounting for scr refresh
            Control_2_resp_recorded_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_resp_recorded_text, 'tStopRefresh')  # time at next scr refresh
            Control_2_resp_recorded_text.setAutoDraw(False)
    
    # *Control_2_fixation_horz* updates
    if Control_2_fixation_horz.status == NOT_STARTED and tThisFlip >= 76-frameTolerance:
        # keep track of start time/frame for later
        Control_2_fixation_horz.frameNStart = frameN  # exact frame index
        Control_2_fixation_horz.tStart = t  # local t and not account for scr refresh
        Control_2_fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Control_2_fixation_horz.setAutoDraw(True)
    if Control_2_fixation_horz.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 91-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_fixation_horz.tStop = t  # not accounting for scr refresh
            Control_2_fixation_horz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_fixation_horz, 'tStopRefresh')  # time at next scr refresh
            Control_2_fixation_horz.setAutoDraw(False)
    
    # *Control_2_fixation_vert* updates
    if Control_2_fixation_vert.status == NOT_STARTED and tThisFlip >= 76-frameTolerance:
        # keep track of start time/frame for later
        Control_2_fixation_vert.frameNStart = frameN  # exact frame index
        Control_2_fixation_vert.tStart = t  # local t and not account for scr refresh
        Control_2_fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Control_2_fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Control_2_fixation_vert.setAutoDraw(True)
    if Control_2_fixation_vert.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 91-frameTolerance:
            # keep track of stop time/frame for later
            Control_2_fixation_vert.tStop = t  # not accounting for scr refresh
            Control_2_fixation_vert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Control_2_fixation_vert, 'tStopRefresh')  # time at next scr refresh
            Control_2_fixation_vert.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Control_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Control_2"-------
for thisComponent in Control_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
toc_control_2 = time()
thisExp.addData("control_2_end", toc_control_2)
thisExp.addData("real_timestamp_control_2_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("control_2_duration", (toc_control_2 - tic_control_2))
thisExp.addData('Control_2_instruction.started', Control_2_instruction.tStartRefresh)
thisExp.addData('Control_2_instruction.stopped', Control_2_instruction.tStopRefresh)
thisExp.addData('Control_2_3.started', Control_2_3.tStartRefresh)
thisExp.addData('Control_2_3.stopped', Control_2_3.tStopRefresh)
thisExp.addData('Control_2_2.started', Control_2_2.tStartRefresh)
thisExp.addData('Control_2_2.stopped', Control_2_2.tStopRefresh)
thisExp.addData('Control_2_1.started', Control_2_1.tStartRefresh)
thisExp.addData('Control_2_1.stopped', Control_2_1.tStopRefresh)
Control_2_video.stop()
# check responses
if Control_2_resp.keys in ['', [], None]:  # No response was made
    Control_2_resp.keys = None
thisExp.addData('Control_2_resp.keys',Control_2_resp.keys)
if Control_2_resp.keys != None:  # we had a response
    thisExp.addData('Control_2_resp.rt', Control_2_resp.rt)
thisExp.addData('Control_2_resp.started', Control_2_resp.tStartRefresh)
thisExp.addData('Control_2_resp.stopped', Control_2_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Control_2_same_different_text.started', Control_2_same_different_text.tStartRefresh)
thisExp.addData('Control_2_same_different_text.stopped', Control_2_same_different_text.tStopRefresh)
thisExp.addData('Control_2_resp_recorded_text.started', Control_2_resp_recorded_text.tStartRefresh)
thisExp.addData('Control_2_resp_recorded_text.stopped', Control_2_resp_recorded_text.tStopRefresh)
thisExp.addData('Control_2_fixation_horz.started', Control_2_fixation_horz.tStartRefresh)
thisExp.addData('Control_2_fixation_horz.stopped', Control_2_fixation_horz.tStopRefresh)
thisExp.addData('Control_2_fixation_vert.started', Control_2_fixation_vert.tStartRefresh)
thisExp.addData('Control_2_fixation_vert.stopped', Control_2_fixation_vert.tStopRefresh)
thisExp.addData('control_video_file_2', control_2)
# the Routine "Control_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Learning_3"-------
continueRoutine = True
routineTimer.add(81.000000)
# update component parameters for each repeat
tic_learning_3 = time()
thisExp.addData("Learning_3_start", tic_learning_3)
thisExp.addData("real_timestamp_learning_3_start", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
# keep track of which components have finished
Learning_3Components = [Learning_3_instruction, Learning_3_3, Learning_3_2, Learning_3_1, Learning_3_video, Learning_3_fixation_horz, Learning_3_fixation_vert]
for thisComponent in Learning_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Learning_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Learning_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Learning_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Learning_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Learning_3_instruction* updates
    if Learning_3_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_instruction.frameNStart = frameN  # exact frame index
        Learning_3_instruction.tStart = t  # local t and not account for scr refresh
        Learning_3_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_instruction, 'tStartRefresh')  # time at next scr refresh
        Learning_3_instruction.setAutoDraw(True)
    if Learning_3_instruction.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_instruction.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_instruction.tStop = t  # not accounting for scr refresh
            Learning_3_instruction.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_instruction, 'tStopRefresh')  # time at next scr refresh
            Learning_3_instruction.setAutoDraw(False)
    
    # *Learning_3_3* updates
    if Learning_3_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_3.frameNStart = frameN  # exact frame index
        Learning_3_3.tStart = t  # local t and not account for scr refresh
        Learning_3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_3, 'tStartRefresh')  # time at next scr refresh
        Learning_3_3.setAutoDraw(True)
    if Learning_3_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_3.tStop = t  # not accounting for scr refresh
            Learning_3_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_3, 'tStopRefresh')  # time at next scr refresh
            Learning_3_3.setAutoDraw(False)
    
    # *Learning_3_2* updates
    if Learning_3_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_2.frameNStart = frameN  # exact frame index
        Learning_3_2.tStart = t  # local t and not account for scr refresh
        Learning_3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_2, 'tStartRefresh')  # time at next scr refresh
        Learning_3_2.setAutoDraw(True)
    if Learning_3_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_2.tStop = t  # not accounting for scr refresh
            Learning_3_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_2, 'tStopRefresh')  # time at next scr refresh
            Learning_3_2.setAutoDraw(False)
    
    # *Learning_3_1* updates
    if Learning_3_1.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_1.frameNStart = frameN  # exact frame index
        Learning_3_1.tStart = t  # local t and not account for scr refresh
        Learning_3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_1, 'tStartRefresh')  # time at next scr refresh
        Learning_3_1.setAutoDraw(True)
    if Learning_3_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_1.tStop = t  # not accounting for scr refresh
            Learning_3_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_1, 'tStopRefresh')  # time at next scr refresh
            Learning_3_1.setAutoDraw(False)
    
    # *Learning_3_video* updates
    if Learning_3_video.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_video.frameNStart = frameN  # exact frame index
        Learning_3_video.tStart = t  # local t and not account for scr refresh
        Learning_3_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_video, 'tStartRefresh')  # time at next scr refresh
        Learning_3_video.setAutoDraw(True)
    if Learning_3_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_video.tStop = t  # not accounting for scr refresh
            Learning_3_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_video, 'tStopRefresh')  # time at next scr refresh
            Learning_3_video.setAutoDraw(False)
    
    # *Learning_3_fixation_horz* updates
    if Learning_3_fixation_horz.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_fixation_horz.frameNStart = frameN  # exact frame index
        Learning_3_fixation_horz.tStart = t  # local t and not account for scr refresh
        Learning_3_fixation_horz.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_fixation_horz, 'tStartRefresh')  # time at next scr refresh
        Learning_3_fixation_horz.setAutoDraw(True)
    if Learning_3_fixation_horz.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_fixation_horz.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_fixation_horz.tStop = t  # not accounting for scr refresh
            Learning_3_fixation_horz.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_fixation_horz, 'tStopRefresh')  # time at next scr refresh
            Learning_3_fixation_horz.setAutoDraw(False)
    
    # *Learning_3_fixation_vert* updates
    if Learning_3_fixation_vert.status == NOT_STARTED and tThisFlip >= 66-frameTolerance:
        # keep track of start time/frame for later
        Learning_3_fixation_vert.frameNStart = frameN  # exact frame index
        Learning_3_fixation_vert.tStart = t  # local t and not account for scr refresh
        Learning_3_fixation_vert.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Learning_3_fixation_vert, 'tStartRefresh')  # time at next scr refresh
        Learning_3_fixation_vert.setAutoDraw(True)
    if Learning_3_fixation_vert.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Learning_3_fixation_vert.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            Learning_3_fixation_vert.tStop = t  # not accounting for scr refresh
            Learning_3_fixation_vert.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Learning_3_fixation_vert, 'tStopRefresh')  # time at next scr refresh
            Learning_3_fixation_vert.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Learning_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Learning_3"-------
for thisComponent in Learning_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
toc_learning_3 = time()
thisExp.addData("learning_3_end", toc_learning_3)
thisExp.addData("real_timestamp_learning_3_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("learning_3_duration", (toc_learning_3 - tic_learning_3))
thisExp.addData('Learning_3_instruction.started', Learning_3_instruction.tStartRefresh)
thisExp.addData('Learning_3_instruction.stopped', Learning_3_instruction.tStopRefresh)
thisExp.addData('Learning_3_3.started', Learning_3_3.tStartRefresh)
thisExp.addData('Learning_3_3.stopped', Learning_3_3.tStopRefresh)
thisExp.addData('Learning_3_2.started', Learning_3_2.tStartRefresh)
thisExp.addData('Learning_3_2.stopped', Learning_3_2.tStopRefresh)
thisExp.addData('Learning_3_1.started', Learning_3_1.tStartRefresh)
thisExp.addData('Learning_3_1.stopped', Learning_3_1.tStopRefresh)
Learning_3_video.stop()
thisExp.addData('Learning_3_fixation_horz.started', Learning_3_fixation_horz.tStartRefresh)
thisExp.addData('Learning_3_fixation_horz.stopped', Learning_3_fixation_horz.tStopRefresh)
thisExp.addData('Learning_3_fixation_vert.started', Learning_3_fixation_vert.tStartRefresh)
thisExp.addData('Learning_3_fixation_vert.stopped', Learning_3_fixation_vert.tStopRefresh)
thisExp.addData('learning_video_file_3', learning)

# ------Prepare to start Routine "Done"-------
continueRoutine = True
# update component parameters for each repeat
toc = time()
thisExp.addData("main_task_end", toc)
thisExp.addData("real_timestamp_main_task_end", datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S.%f'))
thisExp.addData("main_task_duration", (toc - tic))

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
