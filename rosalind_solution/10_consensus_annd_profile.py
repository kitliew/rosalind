#!/usr/bin/env python3
#
# Problem
# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
#
# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
#
# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
#
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
#
# Sample Dataset
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

import sys
import pprint
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
    return samples

def count_index(filename):
    #getting list of DNA string
    samples = fasta_file(filename)
    #group DNA string index together
    test = list(zip(*samples))
    #for each index group, count ACGT
    DNA = sorted(set("ACGT"))
    cnt = {}
    for x in DNA:
        cnt[x] = []
    consensus = ""
    for i in test:
        highest_count = 0
        highest_DNA = ""
        for j in DNA:
            score = i.count(j)
            cnt[j].append(score)
            if score > highest_count:
                highest_count = score
                highest_DNA = j
            else:
                continue
        consensus+=highest_DNA
    print(consensus)
    for c,v in cnt.items():
        print("{}:".format(c), *v)

count_index(sys.argv[1])
