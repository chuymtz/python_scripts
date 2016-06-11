# -*- coding: utf-8 -*-
"""
Python Workshop 01/30/2015

@author: yuanwang

"""

for i in range(0,10):
    if i >= 8:
        break
    else:
        print i
#############################################################        
        
for i in range(0,10):
    if i % 2 == 0:
        continue
    else:
        print i

############################################################

CodonTable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAG":"STOP", "UAA":"Stop",
              "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
              "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
              "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
              "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
              "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
              "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
              "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
              "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
              "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
              "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
              "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
              "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
              "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
              
RNAs = ['CCU', 'UAC', 'UAG', 'CAU', 'AAU']

finalTranslation = ''

for rna in RNAs:
    if CodonTable[rna] == 'STOP':
        break
    else:
        finalTranslation = finalTranslation + CodonTable[rna]
print finalTranslation
#############################################################

finalTranslation = ''

for rna in RNAs:
    if CodonTable[rna] == 'STOP':
        continue
    else:
        finalTranslation = finalTranslation + CodonTable[rna]
print finalTranslation