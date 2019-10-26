# Problem
# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).
#
# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#
# Return: The transition/transversion ratio R(s1,s2).
#
# Sample Dataset
# >Rosalind_0209
# GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
# AGTACGGGCATCAACCCAGTT
# >Rosalind_2200
# TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
# GGTACGAGTGTTCCTTTGGGT
# Sample Output
# 1.21428571429

import sys

def read_file(filename):
    dna = []
    with open(filename) as file:
        contents = file.read().split(">")[1:]
        for content in contents:
            dna.append(content.partition("\n")[-1].replace("\n",""))
    return dna

def trans_and_trans(filename):
    dna1, dna2 = read_file(filename)
    # transition A to G, C to T
    transition = 0
    # transversion A to T, A to C, G to C, G to T
    transversion = 0
    # mutation index
    mutate1 = ""
    mutate2 = ""
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            mutate1 += dna1[i]
            mutate2 += dna2[i]
            if (dna1[i] in ("C", "T")) and (dna2[i] in ("C", "T")):
                transition += 1
            elif (dna1[i] in ("A", "G")) and (dna2[i] in ("G", "A")):
                transition += 1
            else:
                transversion += 1
        else:
            mutate1 += "-"
            mutate2 += "-"
# show mutations
#    print(mutate1)
#    print(mutate2)
    return transition/transversion


test = trans_and_trans(sys.argv[1])
print(test)
