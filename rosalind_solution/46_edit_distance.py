# Problem
# Given two strings s and t (of possibly different lengths), the edit distance dE(s,t) is the minimum number of edit operations needed to transform s into t, where an edit operation is defined as the substitution, insertion, or deletion of a single symbol.
#
# The latter two operations incorporate the case in which a contiguous interval is inserted into or deleted from a string; such an interval is called a gap. For the purposes of this problem, the insertion or deletion of a gap of length k still counts as k distinct edit operations.
#
# Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
#
# Return: The edit distance dE(s,t).
#
# Sample Dataset
# >Rosalind_39
# PLEASANTLY
# >Rosalind_11
# MEANLY
# Sample Output
# 5

# Levenshtein's edit distance algorithm
import sys
import numpy as np

def readfile(filename):
    with open(filename) as file:
        contents = file.read().split(">")[1:]
        contents = [single.partition("\n")[-1].strip().replace("\n","") for single in contents]
    return sorted(contents)

def leven(filename):
    # Initialize matrix M.
    s, t = readfile(filename)
    M = np.zeros((len(s)+1,len(t)+1), dtype=int)
    for i in range(1,len(s)+1):
        M[i][0]= i
    for i in range(1,len(t)+1):
        M[0][i]= i

    # Compute each entry of M.
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1] == t[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)
    return M[len(s)][len(t)]


print(leven(sys.argv[1]))