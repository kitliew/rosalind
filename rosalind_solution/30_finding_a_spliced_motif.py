# Problem
# A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).
#
# As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.
#
# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
#
# Sample Dataset
# >Rosalind_14
# ACGTACGTGACG
# >Rosalind_18
# GTA
# Sample Output
# 3 8 10

import sys

def read_file(filename):
    dna = []
    with open(filename) as file:
        contents = file.read().split(">")[1:]
        for content in contents:
            dna.append(content.partition("\n")[-1].replace("\n",""))
    return dna

def spliced_motif(filename):
    target, subseq = read_file(filename)
    print(target,subseq)
    start = 0
    location = []
    for i in subseq:
        for j in range(start, len(target)):
            if i == target[j]:
                location.append(j+1)
                start = j+1
                break
            else:
                continue
    return location

print(*spliced_motif(sys.argv[1]))