# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

Exercise 4

1. Write a function that returns its GC-content when a sequence is given
   GC_Content = (#G + #C) / length(seq)
2. SeqForEX4.txt contains 5 different DNA sequences with its corresponding
   headers, find a way to read in the 5 sequences alone and print them out, 
   respectively
3. Calculate the GC-content for all 5 sequences

*  Find the sequence with the highest GC-content, write its ID from header
   and its coresponding GC-content to a file named 'result.txt'
   

@author: Yuan
"""

################question 1#############################

def GCCalculator(seq):
    return float((seq.count('C') + seq.count('G')))/len(seq)

################question 2##############################
f = open('SeqForEX4.txt', 'r')

allSeq = list()
allID = list()

for line in f:
    if line.startswith('>'):
        allID.append(line[1:5])
    else:
        allSeq.append(line.strip())
        
for seq in allSeq:
    print seq
    
#################question 3############################
GCContents = list()

for seq in allSeq:
    GCContents.append(GCCalculator(seq))
    
print GCContents

#################************############################
maxValue = max(GCContents)
maxIndex = GCContents.index(maxValue)

f = open('result.txt','w')

f.write('%s    %.2f' % (allID[maxIndex],maxValue))

f.close()
    