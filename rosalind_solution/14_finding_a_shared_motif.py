#!/usr/bin/env python3

# Problem
# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
#
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".
#
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
#
# Sample Dataset
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
# Sample Output
# AC

import sys

"""
Input:
a collection of k DNA strings in FASTA format

Output:
Longest common substring of collection
"""

def fasta_file(filename):
    #only need to collect a list of DNA string
    samples=[]
    with open(filename) as file:
        #separate each entries  return list
        individual = file.read().split(">")[1:]
        #separate name and DNA string within entries    return list of DNA string
        for i in individual:
            dna = i.partition("\n")[-1].strip().replace("\n", "")
            samples.append(dna)
    return sorted(samples)

def lcs(filename):
    strings = fasta_file(filename)
    short_string = strings[0]
    other_string = strings[1:]

    l = len(short_string)
    longest_string= ""

    for i in range(0, l):
        for j in range(l, i+len(longest_string), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_string:
                if s1 not in s2:
                    matched_all = False
                    break
            if matched_all:
                longest_string=s1
                break
    return longest_string

def main():
    filename=sys.argv[1]
    print(lcs(filename))

if __name__ == "__main__":
    main()
