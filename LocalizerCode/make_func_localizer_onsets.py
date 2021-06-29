# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 15:16:37 2021

@author: smwei
"""

import os
import glob
import pandas as pd
import warnings

# Find the directory containing this file
baseDir = os.path.dirname(os.path.realpath(__file__))

# Where are the data
dataDir = os.path.join(baseDir,'data')

# Where should the output go
outputDir = os.path.join(baseDir,'onsets')

# list of input files
inputFiles = glob.glob(os.path.join(dataDir,'*.csv'))


def generateOnsets(inputFile):
    """ Create separate onsets files for four conditions for the functional localizer.
    
    Inputs: 
        inputFile - CSV output from the functional localizer Psychopy script
    
    Outputs: 
        events - Pandas DataFrame consisting of onsets, durations, and condition. (Excludes null blocks)
        
    """
    
    # Using input filename to generate output directory and file name stem
    
    if 'subj' in inputFile:
        subj = inputFile.split('\\')[-1][4:9]
        run = inputFile.split('\\')[-1][13:17]
        
        outputStem = subj + '_' + run
    
        print(f'Making subj specific directory by subj name: {outputStem}')
        
    else:
        outputStem = inputFile.split('\\')[-1][:-4]
        
        print(f'Directory created by file name. Subj # not found: {outputStem}')
        
        
    subjOutputDir = os.path.join(outputDir,outputStem)
    if not os.path.exists(subjOutputDir):
        os.mkdir(subjOutputDir)

    
    # Read in file name
    df = pd.read_csv(inputFile)
    
    # Sanity check input CSV as being complete
    if len(df) <= 246:
        warnings.warn(f'Data incomplete ({len(df)} trials found in {inputFile}')
    
    if len(df) == 0:
        return 
    
    # Each onset is the image.started time of the block_start row
    onset = df[df['block_type']=='block_start'].reset_index()['image.started']
    
    # Each duration is the image.stopped time of the block_end row
    duration  = df[df['block_type']=='block_end'].reset_index()['image.stopped'].astype('float')
    
    # Grab conditions from block_start
    trial_type = df[df['block_type']=='block_start'].reset_index()['condition']
    
    # Times are relative to the first image, so all onsets and durations need to be relative to that.
    init = onset[0]
    print(f'Initial onset at {init:.2f}')
    
    onset = onset - init
    duration = duration - init
    
    if any(duration) > 12:
        print('Duration over 12s occurred - something wrong with {inputfile}')
    
    # This would throw an error if it wasn't true
    if len(onset) == len(duration) and len(duration) == len(trial_type):
    
        events = pd.DataFrame({'onset' : onset,
                               'duration' : duration,
                               'trial_type' : trial_type})
        
        
        for condition in ['scrambled','objects','scenes','faces']:
            events[events['trial_type']==condition].to_csv(os.path.join(subjOutputDir,condition+'_onsets.tsv'),sep='\t',index=False)
        
        return events
    
    else: 
        warnings.warn(f'Data incomplete: Onsets, duration, and conditions are not the same length for {inputFile}.')

for file in inputFiles: 
    events = generateOnsets(file)
    
    