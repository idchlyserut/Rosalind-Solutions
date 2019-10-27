# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:33:37 2019

@author: User
"""


def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1
 
    return dh

if __name__ == "__main__":


    large_dataset = open('C:/Users/User/3D Objects/Bio prog/rosalind_hamm.txt').read()

    s, t = large_dataset.split()
    dist = hamming_distance(s, t)

    print (dist)