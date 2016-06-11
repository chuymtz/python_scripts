# -*- coding: utf-8 -*-
"""
Python Workshop 1/30/2015

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