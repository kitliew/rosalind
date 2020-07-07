#!/usr/bin/env python3

# Problem
# In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
#
# The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.
#
# Given: A protein string P of length at most 1000 aa.
#
# Return: The total weight of P. Consult the monoisotopic mass table.
#
# Sample Dataset
# SKADYEK
# Sample Output
# 821.392
#
"""Given a protein string P of length at most 1000aa. Return total weight of P."""

import sys


#data
weighted_alphabet = """
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
"""
elements = weighted_alphabet.split()
alphabet = elements[::2]
weight = elements[1::2]
dic_weight_alphabet = dict(zip(alphabet,weight))

def weighted_table(aa):
    return(float(dic_weight_alphabet[aa]))

def protein_weight(aa_string):
    total_weight = 0
    for char in aa_string:
        total_weight += weighted_table(char)
    return total_weight

def main():
    aa_file = sys.argv[1]
    with open(aa_file) as ff:
        aa_string=ff.read().strip()
        print(protein_weight(aa_string))

if __name__ == "__main__":
    main()
