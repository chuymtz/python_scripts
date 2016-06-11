# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

Solution 1

Execute the first line of the code (highlight and hit F9),
this will define a string 'seq'

1. Print the sequence alone (without header '6404|')
2. Print the sequence alone, all in lower-case
3. Print the index of substring 'GAAC' (first occurrence only)
4. Make it a RNA sequence and print it out (change every T to U)
5. Add 'CAGACACGC' to the end of the sequence and print it out

@author: yuanwang
"""

seq = '6404|CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGC'

################################################################
newSeq = seq[5:]

print newSeq        # question 1

print newSeq.lower()  # question 2

print newSeq.find('GAAC') # quetion 3

print newSeq.replace('T','U') # question 4
 
print newSeq + 'CAGACACGC'   #question 5