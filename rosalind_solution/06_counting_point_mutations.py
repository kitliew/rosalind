# Problem
#
# Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
#
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
# Return: The Hamming distance dH(s,t).
#
# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
#
# Sample Output
# 7

import sys

def cnt_pnt_mutation(filename):
    with open(filename) as file:
        count = 0
        lines = file.readlines()
        seq1 = lines[0]
        seq2 = lines[1]
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
        return count

print(cnt_pnt_mutation(sys.argv[1]))

"""
#method 2
def pnt_mutation(filename):
    with open(filename) as file:
        lines = file.readlines()
        return sum([a != b for a, b in zip(lines[0],lines[1])])

print(pnt_mutation("rosalind_hamm.txt"))
"""
