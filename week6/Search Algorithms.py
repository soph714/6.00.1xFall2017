# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:24:05 2018

@author: Ted
"""

def linear_search(L, e):
    # overall complexity is O(n) - where n is len(L)
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
        return found
    
def search(L, e):
    # linear search on a sorted list
    # must only look until reach a number greater than e
    # O(len(L))
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def bisect_search1(L, e):
    '''
    list L must be sorted
    recursive method
    O(log len(L))
    copying the list in recursive call makes this more complex tho
    so actually is O(n log n)
    '''
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)
        
def bisect_search2(L, e):
    '''
    helper function added to bisectional search function. 
    cutting down half the search but not copying the list
    O(log n)
    '''
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False # nothing left to search
            else:
                return bisect_search_helper(L, e, low, mid-1)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)
            
import random            

def bogo_sort(L):
    # best case O(n) where n in len(L)
    # worst case... unbound!
    # assume having is_sorted(L) function
    while not is_sorted(L):
        random.shuffle(L)

def bubble_sort(L):
    # inner for loop is for doing comparisons
    # outer while loop is for doing multiple passes until no more swaps
    # O(n^2) where n is len(L)
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selection_sort(L):
    # outer loop executes len(L) times
    # inner loop executes len(L) - i times
    # O(n^2) where n is len(L)
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
        

def merge(left, right):
    # order O(n) where n = len(left) + len(right)
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
            
            
            
            
            