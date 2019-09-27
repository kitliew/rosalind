#!/usr/bin/env python3

# Problem
# Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).
#
# Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.
#
# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
#
# Sample Dataset
# A C G T
# 2
# Sample Output
# AA
# AC
# AG
# AT
# CA
# CC
# CG
# CT
# GA
# GC
# GG
# GT
# TA
# TC
# TG
# TT

import sys

def permutation(string, prefix, k):
    # k = remaining characters for permutation
    # if k == length_string, return
    if k == 0:
        print(prefix)
        return
    for i in range(len(string)):
        new_prefix = prefix + string[i]

        permutation(string, new_prefix, k-1)

with open(sys.argv[1]) as file:
    content = file.readlines()
    string = content[0].strip().split()
    length = int(content[1].strip())
    permutation(string, "", length)
