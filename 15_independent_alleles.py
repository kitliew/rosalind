#!/usr/bin/env python3
import sys
import numpy
import math

"""
Input:
k-th generation
N Aa Bb organisms

Output:
Probability that at least N AaBb (heterozygous) organisms at k-th generation (not counting their mate)

Note:
Each organism always mate with Aa Bb.
Therefore, probability of getting AaBb is always 4/16 == 25%
"""

#combination/factorial
def combi(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def prob_heterozygous(k, N):
    prob_AaBb = 0.25

    prob_list = []
    total = 2**k
    for i in range(N, (total+1)):
        #true for AaBb  ; probT_AaBb = (prob_AaBb ** i)
        #non AaBb       ; probN_AaBb = (1-prob_AaBb) ** (total-i)
        #rearrange the above to get probability of AaBb; using combinatorial
        #then sum all the probability in list
        prob_list.append(combi(total, i) * (prob_AaBb**i) * ((1-prob_AaBb)**(total-i)))
    return sum(prob_list)

def main():
    for line in sys.stdin:
        a, b = line.strip().split()
        print(prob_heterozygous(int(a),int(b)))

if __name__=="__main__":
    main()

print(prob_heterozygous(2, 1))
