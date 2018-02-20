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
    in this case O(len(L1)*len(L2))
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


def intersect(L1, L2):
    '''
    another example of quadratic complexity algorithm O
    first nested loops takes len(L1)*len(L2)
    '''
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res


def g(n):
    '''
    assumes n >= 0
    example of O(n^2) 
    '''
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x
    
def genSubsets(L):
    '''
    very clever code to get all possible combos of a list
    example of exponential complexity - O(2^n)
    '''
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) #all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element
    return smaller+new # combine those with last element and those without
    
    
    
def h(n):
    """
    assume n as int >= 0
    adds digits of a number together
    algorithm is linear O(len(s)) but in terms of n...
    but actually O(log n) due to length of string.
    """
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer


def fib_iter(n):
    '''
    the top if, elif and else are constant O(1)
    the for loop is linear, O(n)
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_1
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii


def fib_recur(n):
    '''
    assumes n an int >= 0
    the recursive returns makes this an exponential order O(2^n)
    if we utilize dictionaries to remember previous calls we can keep the elegance of this code...
    while lowering the computational order to linear O(n)
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

def sum_list(L):
    '''
    input is a list
    Order is O(len(L)) or O(n)
    '''
    total = 0
    for e in L:
        total = total + e
    return total












