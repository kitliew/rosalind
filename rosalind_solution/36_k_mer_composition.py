# Problem
# For a fixed positive integer k, order all possible k-mers taken from an underlying alphabet lexicographically.
#
# Then the k-mer composition of a string s can be represented by an array A for which A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic order) appears in s.
#
# Given: A DNA string s in FASTA format (having length at most 100 kbp).
#
# Return: The 4-mer composition of s.
#
# Sample Dataset
# >Rosalind_6431
# CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
# CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
# TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
# AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
# GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
# CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
# CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
# Sample Output
# 4 1 4 3 0 1 1 5 1 3 1 2 2 1 2 0 1 1 3 1 2 1 3 1 1 1 1 2 2 5 1 3 0 2 2 1 1 1 1 3 1 0 0 1 5 5 1 5 0 2 0 2 1 2 1 1 1 2 0 1 0 0 1 1 3 2 1 0 3 2 3 0 0 2 0 8 0 0 1 0 2 1 3 0 0 0 1 4 3 2 1 1 3 1 2 1 3 1 2 1 2 1 1 1 2 3 2 1 1 0 1 1 3 2 1 2 6 2 1 1 1 2 3 3 3 2 3 0 3 2 1 1 0 0 1 4 3 0 1 5 0 2 0 1 2 1 3 0 1 2 2 1 1 0 3 0 0 4 5 0 3 0 2 1 1 3 0 3 2 2 1 1 0 2 1 0 2 2 1 2 0 2 2 5 2 2 1 1 2 1 2 2 2 2 1 1 3 4 0 2 1 1 0 1 2 2 1 1 1 5 2 0 3 2 1 1 2 2 3 0 3 0 1 3 1 2 3 0 2 1 2 2 1 2 3 0 1 2 3 1 1 3 1 0 1 1 3 0 2 1 2 2 0 2 1 1

import sys

def readfile(filename):
    with open(filename) as file:
        dna = file.read().strip().partition("\n")[-1].replace("\n","")
    return dna

def removeNestlist(lst):
    if type(lst) != list:
        k_mer_list.append(lst)
    for i in lst:
        if type(lst) == list:
            removeNestlist(i)

def permutation(string, prefix, k):
    # k = remaining characters for permutation
    # if k == length_string, return
    if k == 0:
        return prefix

    answer = []

    for i in range(len(string)):
        new_prefix = prefix + string[i]

        answer.append(permutation(string, new_prefix, k-1))

    return answer

def k_mer_composit(dna, target):
    count = 0
    for i in range(len(dna)-len(target)+1):
        if dna[i:i+len(target)] == target:
            count += 1
    return count

if __name__ == "__main__":
    # product/permutation of DNA with 4 kmer
    k_mer_list = []
    _dna, _k_mer = "ACGT", 4
    test1 = permutation(_dna, "", _k_mer)
    # remove nested list
    removeNestlist(test1)

    dna = readfile(sys.argv[1])
    test2 = [k_mer_composit(dna,i) for i in k_mer_list]
    print(*test2)
