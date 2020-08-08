# Problem
# In “Counting Subsets”, we saw that the total number of subsets of a set S containing n elements is equal to 2n.
#
# However, if we intend to count the total number of subsets of S having a fixed size k, then we use the combination statistic C(n,k), also written (nk).
#
# Given: Positive integers n and m with 0≤m≤n≤2000.
#
# Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).
#
# Sample Dataset
# 6 3
# Sample Output
# 42


import sys
from math import factorial

def read_file(filename):
    with open(filename) as file:
        n, m = file.read().strip().split()
    return int(n),int(m)

def alter_splice(filename):
    n,m = read_file(filename)
    subsets = 0
    for k in range(m, n + 1):
        subsets += (factorial(n) // (factorial(k) * factorial(n - k)))
    return subsets % 1000000

print(alter_splice(sys.argv[1]))
