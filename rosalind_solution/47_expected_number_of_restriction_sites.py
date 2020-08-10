# Problem
# Say that you place a number of bets on your favorite sports teams. If their chances of winning are 0.3, 0.8, and 0.6, then you should expect on average to win 0.3 + 0.8 + 0.6 = 1.7 of your bets (of course, you can never win exactly 1.7!)
#
# More generally, if we have a collection of events A1,A2,…,An, then the expected number of events occurring is Pr(A1)+Pr(A2)+⋯+Pr(An) (consult the note following the problem for a precise explanation of this fact). In this problem, we extend the idea of finding an expected number of events to finding the expected number of times that a given string occurs as a substring of a random string.
#
# Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
#
# Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
#
# Sample Dataset
# 10
# AG
# 0.25 0.5 0.75
# Sample Output
# 0.422 0.563 0.422

import sys

def readfile(filename):
    with open(filename) as file:
        contents = file.read().strip().split("\n")
    n = int(contents[0])
    s = contents[1]
    i = [float(i) for i in contents[2].split()]
    return n,s,i

def enor(filename):
    n, s, i = readfile(filename)
    occurrence = n - len(s) + 1
    AT = s.count("A") + s.count("T")
    GC = s.count("G") + s.count("C")
    p_array = []
    for j in i:
        prob_AT = ((1-j)/2)**AT
        prob_GC = (j/2)**GC
        prob = prob_AT*prob_GC * occurrence
        p_array.append("%0.3f" %prob)
    return p_array

print(*enor(sys.argv[1]))