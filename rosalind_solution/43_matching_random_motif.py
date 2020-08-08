# Problem
# Our aim in this problem is to determine the probability with which a given motif (a known promoter, say) occurs in a randomly constructed genome. Unfortunately, finding this probability is tricky; instead of forming a long genome, we will form a large collection of smaller random strings having the same length as the motif; these smaller strings represent the genome's substrings, which we can then test against our motif.
#
# Given a probabilistic event A, the complement of A is the collection Ac of outcomes not belonging to A. Because Ac takes place precisely when A does not, we may also call Ac "not A."
#
# For a simple example, if A is the event that a rolled die is 2 or 4, then Pr(A)=13. Ac is the event that the die is 1, 3, 5, or 6, and Pr(Ac)=23. In general, for any event we will have the identity that Pr(A)+Pr(Ac)=1.
#
# Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
#
# Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
#
# Sample Dataset
# 90000 0.6
# ATAGCCGA
# Sample Output
# 0.689

import sys

def read_file(filename):
    with open(filename) as file:
        length, gc, dna = file.read().strip().split()
    return int(length), float(gc), dna

def mrm(filename):
    length, gc, dna = read_file(filename)
    gc_p = (gc/2)**(dna.count("G") + dna.count("C"))
    at_p = ((1-gc)/2) **(dna.count("A") + dna.count("T"))
    total_p = gc_p * at_p
    prob = 1 - ((1 - total_p)** length)
    return prob

print("%.3f" %mrm(sys.argv[1]))