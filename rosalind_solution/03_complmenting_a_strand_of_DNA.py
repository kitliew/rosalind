# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#
# Given: A DNA string s of length at most 1000 bp.
#
# Return: The reverse complement sc of s.
#
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT


import sys

def complement_strand(filename):
    with open(filename) as file:
        sequence = file.read().strip().replace("\n", "")
        seq = sequence[::-1]
        change_DNA = str.maketrans("ACGT", "TGCA")
        print(seq.translate(change_DNA))

complement_strand(sys.argv[1])
