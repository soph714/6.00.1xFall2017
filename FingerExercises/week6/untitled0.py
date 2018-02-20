# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:19:59 2018

@author: Ted
"""

def fact_iter(n):
    """ assumes n an int >= 0
        is a linear complexity algorithm
    """
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

def intToStr(i):
    # example of a O(log(i)) complexity algorithm
    
    
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    return result

def addDigits(s):
    # example of a linear complex algorithm: O(s)
    
    # constant
    val = 0
    # variable in length of s
    for c in s:
        #constant
        val += int(c)
    #constant
    return val

def fact_recur(n):
    '''
    assumes n>= 0
    complexity: O(n)
    if timed it runs a bit slower than iterative version due to fnc calls. 
    '''
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1)
    

def isSubset(L1, L2):
    '''
    example of quadratic complexity algorithm O(n^c)
    '''
    
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True



