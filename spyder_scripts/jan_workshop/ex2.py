# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

Exercise 2

Execute the following code for generating a dictionary for RNA translation
table and a list with random RNA fragments. (select and hit F9)

1. Add following entries into the CodonTable:
   GGG : G
   UAA : STOP
2. Print the number of entries in CodonTable, which should be 64
3. Add 'AAC' and 'GAA' to RNAs
4. Translate index 0, 2, 5 in RNAs into amino acids (using CodonTable), print
   the results out, respectively

@author: yuanwang
"""

CodonTable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAG":"STOP",
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
              "GGU":"G", "GGC":"G", "GGA":"G", }
              
RNAs = ['CUC', 'GUU', 'GGG', 'UAA', 'AGU']