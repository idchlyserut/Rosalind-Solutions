# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s="TGTACCCCCTACCCCCTACCCCCTAATAGAATACCCCCATACCCCCAGGTACCCCCTACCCCCTTAATACCCCCCTACCCCCGCCGTTACCCCCTTACCCCCATACCCCCACGCTGTACCCCCATCTACCCCCAGTACCCCCTACCCCCGCCACCTACCCCCTACCCCCTACTACCCCCGATACCCCCCGTACCCCCTGGTACCCCCCGTACCCCCTACCCCCTACTACCCCCTTACCCCCTACCCCCATCGTGTTTACCCCCGCTGCTACCCCCACTACCCCCCGAAACATACCCCCTACCCCCTACCCCCCTACCCCCCAGATACCCCCTACCCCCTCTACCCCCCTTACCCCCGTACCCCCAAAAGGCATACCCCCGTACCCCCCTACCCCCAGCGTACCCCCAATTTCTACCCCCGAACTCTACCCCCCCTACCCCCCCCGGCTTACTACCCCCTCATACCCCCCTAATATACCCCCACTACCCCCTACCCCCTTACCCCCTACCCCCTCTACCCCCGTACCCCCTCTACCCCCCTGTACCCCCTACCCCCTACCCCCTTTACCCCCCTACCCCCTGGTACCCCCTATACCCCCATACCCCCTACCCCCCCTTCGCTACCCCCTACCCCCATGTACCCCCATACCCCCGTGTTACCCCCAGTCTCTACCCCCATACCCCCTCGTAATTACCCCCTACCCCCTGATACCCCCTTACCCCCTTACCCCCGTACCCCCGTACCCCCATTCTACCCCCTACCCCCTTTACCCCCTTACCCCCCGCGCTACGGACTACCCCCTACCCCCTCACCACATACCCCCGGGTTACCCCCCCTACCCCCTTTACCCCCCCGGTACCCCCAACTACCCCCTTACCCCCTAACTACCCCCCGACGAGAGATTACCCCCCTAACCTATACCCCC"
t ="TACCCCCTA"
occur = s.count(t)
res = [i for i  in range(len(s)) if s.startswith(t,i-1)] 
print (res)
