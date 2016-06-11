# -*- coding: utf-8 -*-
"""
Python Workshop 01/30/2015

Exercise 3

Execute the first line of code, which generates a variable "seq", which is
a DNA sequence

1. Count the number of 'C's in the sequence and print it out
2. Calculate its 'GC-content' and print it out
   GC-content = (#G + #C) / sequence length
3. Print out its conplementary chain sequence
   (A to T, T to A, C to G, G to T)
*  Transcribe the sequence to mRNA (T to U) and then translate it to protein
** Stop translating at 'STOP' codon or
** Neglect all 'STOP' codons

@author: yuanwang
"""

seq = 'AGTTTTGAGAAACCTAGAGATCCATCGTGACCTGCCCCGGTTTTACAAGCCCCTCCATATACATTGGCCGATTAAAAGTCCACCCCATTGGCTTCCGCTGGATAGTCGTTAGAACCTGGATAAAAGCCGACTAGCTCTAAGCGCTCGCCGGCAACACGGAAGTGGCATTCCTGGTACGCGACGATTAGGACCACCGGAGCAGTCTACAGTTGCGCGCGCATGTACGGCAATGCGATTGAATTAGCAGTGTGTAATAAACAATATGAGGAGTTCTTGCCGACGAGTTTCCCTTATTTGTGTCTCGGCTAGCGTTCAACACGATCACGTTCGATGTACTAGGAGGGTTAGGTTTATCTGGGCTTGTCGAGACTCAATTTGCGATTGTTCGTTAACATTTAGCCAAAGGCCCCGCAAAATGCGGAGCGTCCGGGGTTACAGCCGCGTGTGTCCTGGTTTCTGCAATCGCCAGACGGCCAAAAAAAGAATACTTGGGTTAGCTTCAGGTGAAGGCAAATATAATTGAACGTTGGTTATGATTCGGTCATTGATCGCATGCCCCTCATCCCATTGAGAGGTGGAATCTTAATAATCAGTCAAAACATCGCGAGGAAGCTATCAGGCAACACGGGCTGCGCTCGCGAGGAATATACTCGATCCGGCTTAAAGGACAACATCAGGACTGATCGACTCGCTGCAGTGACGATGTAGTCCTTGTCCAACGCTGGGCACAATGACGAGTGAAAGTCATAAACTGGTGTCTCGTCGAGAAATGTAGTCTACACGTCCCCACTGCCCTAGACAATAAGGACTGTTGTCGGGAACAAGATCCGGATCGGCTCGGATTCACCGCTCGGAGCAAGTCTGCTCAACGAATATCCATCGGCGCATTAG'

#######question 1################

numC = 0

for i in seq:
    if i == 'C':
        numC += 1
        
print 'The number of C is %d' % numC

#######question 2################

numCG = 0

for i in seq:
    if i == 'C' or i == 'G':
        numCG += 1

GCcontent = float(numCG)/len(seq)        
print 'GC-content : %.2f' %GCcontent

#######question 3################
newSeq = ''

for i in seq:
    if i == 'A':
        newSeq = newSeq + 'T'
    elif i == 'T':
        newSeq = newSeq + 'A'
    elif i == 'C':
        newSeq = newSeq + 'G'
    else:
        newSeq = newSeq + 'C'
        
print '------Conplementary Sequence----'
print newSeq

##### ********** ################

CodonTable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
              "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
              "UAU":"Y", "UAC":"Y", "UAG":"STOP", "UAA":"STOP",
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

mRNA = seq.replace('T', 'U')

translation1 = ''
translation2 = ''

for i in range(0,len(mRNA),3):
    if CodonTable[mRNA[i:i+3]] == 'STOP':
        break
    else:
        translation1 = translation1 + CodonTable[mRNA[i:i+3]]
        
print '-' * 20
print translation1

for i in range(0,len(mRNA),3):
    if CodonTable[mRNA[i:i+3]] == 'STOP':
        continue
    else:
        translation2 = translation2 + CodonTable[mRNA[i:i+3]]
        
print '-' * 20
print translation2
print '-' * 20


