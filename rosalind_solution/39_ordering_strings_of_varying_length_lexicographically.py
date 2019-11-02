# Problem
# Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t′=t[1:m]. We have two cases:
#
# If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
# Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ (e.g., APPLET<LexARTS because APPL<LexARTS).
# Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
#
# Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
#
# Sample Dataset
# D N A
# 3
# Sample Output
# D
# DD
# DDD
# DDN
# DDA
# DN
# DND
# DNN
# DNA
# DA
# DAD
# DAN
# DAA
# N
# ND
# NDD
# NDN
# NDA
# NN
# NND
# NNN
# NNA
# NA
# NAD
# NAN
# NAA
# A
# AD
# ADD
# ADN
# ADA
# AN
# AND
# ANN
# ANA
# AA
# AAD
# AAN
# AAA

import sys

def readfile(filename):
    with open(filename) as file:
        contents = file.readlines()
    return contents[0].replace("\n","").replace(" ",""), int(contents[1])


def partial_product(string, prefix, number):
    if number == 0:
        return prefix
    for i in range(len(string)):
        new_prefix = prefix + string[i]
        print(new_prefix)
        new_string = string[:i] + string[i:]
        partial_product(new_string, new_prefix, number-1)

if __name__ == "__main__":
    dna, number = readfile(sys.argv[1])
    test = partial_product(dna,"", number)
