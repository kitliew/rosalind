#!/usr/bin/env python3

# Problem
# A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).
#
# A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.
#
# Given: A positive integer n≤10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
#
# Sample Dataset
# 5
# 5 1 4 2 3
# Sample Output
# 1 2 3
# 5 4 2

import sys

def lis(d):
	'Return one of the L.I.S. of list d'
	l = []
	for i in range(len(d)):
		l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) + [d[i]])
	return max(l, key=len)


def r_lis(d):
	'Return one of the L.I.S. of list d'
	l = []
	for i in range(len(d)):
		l.append(max([l[j] for j in range(i) if l[j][-1] > d[i]] or [[]], key=len) + [d[i]])
	return max(l, key=len)

with open(sys.argv[1]) as file:
	content = file.readlines()
	max_length = int(content[0].strip())
	number_array = [int(x) for x in content[1].strip().split()]
	print(*lis(number_array))
	print(*r_lis(number_array))


"""
def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [None] * N
    M = [None] * (N + 1)
    L = 0
    for i in range(N):
        print("current index: ", i)
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] < X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i
        print("P", P)
        print("M", M)
        if (newL > L):
            L = newL
        print(L)

    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        print(i,k, M[L])
        S.append(X[k])
        k = P[k]
    return S[::-1]

print(longest_increasing_subsequence([3,2,6,4,5,1]))
"""
