# -*- coding: utf-8 -*-
"""
Spyder Editor

Re-write the scripts for the functional localizer
"""

import pandas as pd
import os
import fnmatch

seqDir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'localizer','sequences')

sequences = [os.path.join(seqDir,f) for f in os.listdir(seqDir) if fnmatch.fnmatch(f,'*.csv')]

idStems = ['11','12','22','21']

for sequence in sequences:

    
    df = pd.read_csv(sequence)
    df = df.iloc[0:244,:].copy()
    df.fillna('null_block',inplace=True)
    df['img_name'][df['block_type'] == 'null_block'] = 'null_block.bmp'
    
        
    originalSeqName = sequence.split('\\')[-1]
    originalSeqID = originalSeqName.split('subj')[1][1:4]
    
    for i in idStems:
        newSeqID = originalSeqName.split('_')[0] + '_subj' + i + originalSeqID + '_' + originalSeqName.split('_')[2]
        newSeqID = os.path.join(seqDir,newSeqID)
    
        df.to_csv(os.path.join(seqDir,newSeqID),index=False)
    
    
    
    
    
    
    
    
    