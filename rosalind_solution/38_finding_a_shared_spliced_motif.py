# Problem
# A string u is a common subsequence of strings s and t if the symbols of u appear in order as a subsequence of both s and t. For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".
#
# Analogously to the definition of longest common substring, u is a longest common subsequence of s and t if there does not exist a longer common subsequence of the two strings. Continuing our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".
#
# Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
#
# Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
#
# Sample Dataset
# >Rosalind_23
# AACCTTGG
# >Rosalind_64
# ACACTGTGA
# Sample Output
# AACTGG

# there are mathematic solution/Longest common subsequence(LCS)
# more advance would be smith-waterman-algorithm

import sys

def readfile(filename):
    with open(filename) as file:
        contents = file.read().strip().split(">")[1:]
        dna = [content.partition("\n")[-1].replace("\n","") for content in contents]
    return sorted(dna)

def find_spliced(dna1, dna2):
    array = [[0 for k in range(len(dna2)+1)] for l in range(len(dna1)+1)]
    for i in range(len(dna1)):
        for j in range(len(dna2)):
            if dna1[i] == dna2[j]:
                array[i+1][j+1] = array[i][j] + 1
            else:
                array[i+1][j+1] = max(
                    array[i+1][j],     # left side
                    array[i][j+1])      # above

    spliced_motif = ""
    x,y = len(dna1), len(dna2)
    while x * y !=0:
        if array[x][y] == array[x-1][y]:
            x-=1
        elif array[x][y] == array[x][y-1]:
            y-=1
        else:
            spliced_motif = dna1[x-1] + spliced_motif
            x-=1
            y-=1
    return spliced_motif


if __name__=="__main__":
    dna1, dna2 = readfile(sys.argv[1])
    print(find_spliced(dna1,dna2))