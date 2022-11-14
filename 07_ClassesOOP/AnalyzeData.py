#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:54:15 2022

@author: johnserences
"""

# import
import numpy as np


# define our class
class AnalyzeData:
    
    # init the object
    def __init__( self, params ):
        
        # a variable pi that belongs to this instance of the object.
        self.pi = 3.141592
        
        self.d2r = self.pi / 180
        
        self.file_name = params.get('file_name','')
        
        
    # a method for loading eeg data
    def load_data(self, file_name):
        
        eeg = np.load(file_name)
        
        print('Data loaded...')
            
        data = eeg['data']
        sr = eeg['sr']
        tx = eeg['tx']
        cond_labels = eeg['cond_labels']
        
        return data, sr, tx, cond_labels
    
    # a method for loading eeg data
    def load_data2(self):
        
        eeg = np.load(self.file_name)
        
        print('Data loaded...')
            
        self.data = eeg['data']
        self.sr = eeg['sr']
        self.tx = eeg['tx']
        self.cond_labels = eeg['cond_labels']
    
    def mean_time(self, data):
        
        self.mt_data = np.mean(data, axis = 2)
        
    # mean across rows of a 2D data set...
    def mean_rows(self, data):
        
        return np.mean(data, axis = 0)
    
    # mean across rows of a 2D data set...
    def mean_rows2(self):
        
        self.mr_data = np.mean(self.data, axis = 0)


    
    def mean_cols(self, data):
        
        return np.mean(data, axis=1)
    
    
    # take a list of angles in degrees and return in rads...
    def gen_degs_rads(self, angs, steps):
        
        d = np.linspace(angs[0], angs[1], steps)
        
        r = d * self.d2r
        
        return r
        
        
        
        
        
        
        
    
    
        
    
        
        
    
    
    
    

