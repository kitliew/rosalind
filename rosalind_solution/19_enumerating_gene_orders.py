import sys
# Problem
# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#
# Given: A positive integer n≤7.
#
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
#
# Sample Dataset
# 3
# Sample Output
# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

import sys

# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l


if __name__=="__main__":
    for number in sys.stdin.readline(1):
        numbers = [x for x in range(1, int(number)+1)]
        test=permutation(numbers)
        print(len(test))
        for i in test:
            print(*i)











"""
if __name__=="__main__":
    number = sys.stdin
"""
