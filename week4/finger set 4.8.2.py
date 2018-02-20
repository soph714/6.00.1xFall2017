# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:47:48 2017

@author: Ted
"""



#def fancy_divide(numbers,index):
#    try:
#        denom = numbers[index]
#        for i in range(len(numbers)):
#            numbers[i] /= denom
#    except IndexError:
#        print("-1")
#    else:
#        print("1")
#    finally:
#        print("0")
        
def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)