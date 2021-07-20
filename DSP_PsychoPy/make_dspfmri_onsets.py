# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:16:37 2021

@author: smwei
"""

import os
import glob
import pandas as pd
import numpy as np

# Find the directory containing this file
baseDir = os.path.dirname(os.path.realpath(__file__))

# Where are the data
dataDir = os.path.join(baseDir,'data')

# Where should the output go
outputDir = os.path.join(baseDir,'onsets')

# list of input files
inputFiles = glob.glob(os.path.join(dataDir,'*.csv'))


def generateOnsets(inputFile,outputDir):
    """ Create separate onsets files for four conditions for the functional localizer.
    
    Inputs: 
        inputFile - CSV output from the functional localizer Psychopy script
        outputDir - directory (to be made if none exists) to store onsets files
    Outputs: 
        events - Pandas DataFrame consisting of onsets, durations, and condition. (Excludes null blocks)
        
    """
    
    # Using input filename to generate output directory and file name stem
    

    subj = 'sub-dspfmri' + inputFile.split('\\')[-1][0:5]
    run = 'run-0' + inputFile.split('\\')[-1][6:7]
    
    outputStem = subj + '_task-dspfmri_' + run

    print(f'Making subj specific directory by subj name: {subj}')
    
        
        
    subjOutputDir = os.path.join(outputDir,subj)
    if not os.path.exists(subjOutputDir):
        os.mkdir(subjOutputDir)

    
    # Read in file name
    df = pd.read_csv(inputFile)
    
    # We need to turn this DF into an events file with: 
        # - onset
        # - duration
        # - trialType (instructions, response, learning_vid, control_vid)
        
    
    
    
    parseDF = pd.DataFrame(columns={'instructions_begin','instructions_end',
                                 'response_begin','response_end',
                                 'vid_begin','vid_end',
                                 'vid_file','vid_type','env_type','layout_route',
                                 'response','same_or_diff_spheres','response_time'})
    
    for i in ['Learning','Control']:
        for j in ['1','2','3']:
            
            if i=='Control' and j=='3':
                continue
            
            stem = i + '_' + j + '_'
            # Select all columns with the stem name and reset index to match that
            vid = df.filter(regex=(stem)).dropna(thresh=1).copy()
            origIndex = vid.index[0]
            vid.index = [stem[:-1]]

            # All vids have these: Instructions start, instructions end, and video end
            thisVid = pd.DataFrame(columns={'instructions_begin','instructions_end',
                                 'response_begin','response_end',
                                 'vid_begin','vid_end',
                                 'vid_file','vid_type','env_type','layout_route',
                                 'response','same_or_diff_spheres','response_time'})

            
            # For control videos, we need a few more things
            if 'Control' in stem:
                
                # Video begin is the same as instructions end
                thisVid['instructions_begin'] = vid[stem + 'instruction.started']
                thisVid['instructions_end'] = vid[stem + '1.stopped']
                thisVid['vid_begin'] = vid[stem + '1.stopped']
                thisVid['vid_end'] = vid[stem + 'resp.started']
                thisVid['response_begin'] = vid[stem + 'resp.started']
                thisVid['response_end'] = vid[stem + 'resp.stopped']
                
                thisVid['response_time'] = vid[stem + 'same_different_text.stopped'] - vid[stem + 'same_different_text.started']
    
                # Translate the responses into what they mean. 
                # If there's no response, delete response time.
                
                if vid.loc[stem[:-1],stem + 'resp.keys'] == 'y':
                    thisVid['response'] = 'same'
                elif vid.loc[stem[:-1],stem + 'resp.keys'] == 'b':
                    thisVid['response'] = 'different'
                else:
                    thisVid['response'] = 'none_recorded'
                    thisVid['response_time'] = np.nan
                
                thisVid['vid_type'] = 'control_vid'
                thisVid['vid_file'] = df.loc[origIndex,'video_file'] 
                
                thisVid['env_type'] = df.loc[origIndex,'environment'] 
                thisVid['layout_route'] = df.loc[origIndex,'route'] + '_' + str(int(df.loc[origIndex,'control_video']))
                
                thisVid['same_or_diff_spheres'] = df.loc[origIndex,'same_or_different']
            
            else:
                
                # Video begin is the same as instructions end
                thisVid['instructions_begin'] = vid[stem + 'instruction.started']
                thisVid['instructions_end'] = vid[stem + '1.stopped']
                thisVid['vid_begin'] = vid[stem + '1.stopped']
                thisVid['vid_end'] = vid[stem + 'fixation_horz.started']
                
                thisVid['vid_type'] = 'learning_vid'
                thisVid['vid_file'] = df['learning_video_file_' + j].dropna().squeeze()
                
                if 'Alt' in thisVid.loc[stem[:-1],'vid_file']:
                    thisVid['env_type'] = 'alternate'
                else:
                    thisVid['env_type'] = 'normal'
            
            
            parseDF = parseDF.append(thisVid)
        
            # CHECK FOR MAXIMAL INCORRECT RESPONSES HERE! 
    
    
    # Some initial time prior to events so we can find the min event in the csv
    initTime = df['Ready_scanner_text.started'].dropna().squeeze()
    
    # Grab the minimum time in the parseDF that is greater than the initTime
    findMin = parseDF.min(numeric_only=True)
    init = [x for x in findMin if x > initTime]
    init = min(init)
    
    # Times are relative to the first presentation of instructions
    print(f'Initial onset at {init:.2f}')
    
    instructions_events = pd.DataFrame(columns={'onset','duration','trial_type'})
    response_events = pd.DataFrame(columns={'onset','duration','trial_type','response_time'})
    video_events = pd.DataFrame(columns={'onset','duration','trial_type'})
    
    instructions_events['onset'] = parseDF.instructions_begin - init
    instructions_events['duration'] = parseDF.instructions_end - parseDF.instructions_begin
    instructions_events['trial_type'] = 'instructions'

    response_events['onset'] = parseDF.response_begin - init
    response_events['duration'] = parseDF.response_end - parseDF.response_begin
    response_events['trial_type'] = 'response'
    response_events['same_or_diff'] = parseDF.same_or_diff_spheres
    response_events['response_time'] = parseDF.response_time
    response_events['response'] = parseDF.response
    response_events['correct'] = parseDF.same_or_diff_spheres == parseDF.response
    
    response_events.dropna(thresh=3,inplace=True)
    
    video_events['onset'] = parseDF.vid_begin - init
    video_events['duration'] = parseDF.vid_end - parseDF.vid_begin
    video_events['trial_type'] = parseDF.vid_type
    video_events['env_type'] = parseDF.env_type
    video_events['vid_file'] = parseDF.vid_file
    
    events = pd.concat([instructions_events,response_events,video_events])
    events.sort_values(by='onset',inplace=True)
    
    #full file as events file.
    events.to_csv(os.path.join(subjOutputDir,outputStem + '_events.tsv'),sep='\t',index=False,line_terminator="\n")
    
    # Save each condition as a separate onset.
    for condition in ['instructions','response','learning_vid','control_vid']:
        temp = events[['onset','duration','trial_type']]
        temp = temp[temp['trial_type'].str.match(condition)].copy()
        temp['strength'] = 1
        temp.drop(columns='trial_type',inplace=True)
        temp.to_csv(os.path.join(subjOutputDir,outputStem + '_condition-' + condition +'_onsets.tsv'),sep='\t',index=False,line_terminator="\n",header=False)
    
    return events

    
for file in inputFiles: 
    events = generateOnsets(file,outputDir)

