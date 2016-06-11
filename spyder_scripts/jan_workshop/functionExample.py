# -*- coding: utf-8 -*-
"""
Python Workshop 01/30/2015

Function Example

@author: yuanwang
"""

def areaCalculator(a,b):
    area = a * b
    return area
    
print areaCalculator(3,4)



def ACounter(seq):
    return float(seq.count('A'))/len(seq)
    

print ACounter('AGCCTGGAACCTGGA')