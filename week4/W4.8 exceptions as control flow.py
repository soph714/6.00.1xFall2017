# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:22:03 2017

@author: Ted
"""

def get_ratios(L1, L2):
    """
        by: tjs for edX MITx 6.00.1x course fall 2017
        Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i]
    """
    
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('Nan')) #Nan = not a number
        except:
            raise ValueError ('get_ratios called with bad arg')
    return ratios
