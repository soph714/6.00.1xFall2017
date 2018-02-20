# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:16:49 2017

@author: SopherT
"""

class fraction (object):
    def __init__ (self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__ (self, other):
        numerNew = other.getDenom() * self.getNumer() \ + other.getNumer() * self.getDemon()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)