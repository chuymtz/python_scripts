# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

for loop examples

@author: yuanwang
"""

for i in range(0,10):
    print i
########################################################################    

for i in range(0,10,2):
    print i
########################################################################
    
CodonTable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
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
              
RNAs = ['CCU', 'UAC', 'ACU', 'CAU', 'AAU']

finalTranslation = ''

for rna in RNAs:
    finalTranslation = finalTranslation + CodonTable[rna]
    
print finalTranslation
    