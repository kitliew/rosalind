# Problem
# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.
#
# Given: A DNA string of length at most 1 kbp in FASTA format.
#
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
# =================================================================================================================================================
# Sample Dataset
# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT
# Sample Output
# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4
# =================================================================================================================================================

import sys

def fasta_file(filename):
    with open(filename) as file:
        individual = file.read().partition("\n")[-1].strip().replace("\n", "")
    return individual

def reverse_complement(dna):
    rev = str.maketrans("ACGT", "TGCA")
    dna_r = dna.translate(rev)[::-1]
    return dna_r

def reverse_palindromes(dna):
    results = []
    for i in range(len(dna)):
        for j in range(4, 13, 2):
            if i + j > len(dna):
                break
            s1 = dna[i:i+j]
            s2 = reverse_complement(s1)
            if s1 == s2:
                results.append([i + 1, j])
    return results

if __name__=="__main__":
    sequence = fasta_file(sys.argv[1])
    results = reverse_palindromes(sequence)
    for i in results:
        print(*i)
