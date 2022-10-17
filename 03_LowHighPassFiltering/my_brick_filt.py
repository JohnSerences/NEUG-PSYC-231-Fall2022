
import numpy as np

def define_filt(fx, filt_freq, type_filt):
    
    '''
    fx = freq axis
    filt_freq = cutoff point in freq space
    type_filt = 'lp' or 'hp'
    
    '''

    cut_pnt = np.flatnonzero( fx == filt_freq )[ 0 ]
    
    brick = np.zeros( len(fx) )
    
    if type_filt == 'lp':
        brick[0:cut_pnt] = 1
        
    elif type_filt == 'hp':
        brick[cut_pnt:] = 1
        
    else:
        raise ValueError('You passed in bad input for type_filt (lp or hp)')
        
    return brick


def apply_filt(input_sig, filt):
    
    '''
    input_sig = time domain signal to filter
    filt = brick wall filter (output of define_filt)
    '''
    
    fft_sig = np.fft.rfft( input_sig )
    
    return np.fft.irfft(fft_sig * filt)
    
    
    
