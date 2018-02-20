# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:12:49 2017

@author: Ted
"""

def satisfiesF(L):
    
   rec_list=[]

   for i in range(0,len(L)):
     if(f(L[i])==False):
        rec_list.append(L[i])
        
   for j in rec_list:
       L.remove(j)

   return len(L)

# print satisfiesF(L)
run_satisfiesF(L, satisfiesF)


