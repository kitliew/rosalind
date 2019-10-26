# Problem
# A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.
#
# Given: A positive integer n≤6.
#
# Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
#
# Sample Dataset
# 2
# Sample Output
# 8
# -1 -2
# -1 2
# 1 -2
# 1 2
# -2 -1
# -2 1
# 2 -1
# 2 1

import sys
import itertools

def permute_list(number):
    sign = list(itertools.product(" -", repeat = number))
    numbers = list(itertools.permutations(range(1,number+1)))
    number_list = []
    for i in sign:
        for j in numbers:
            test = list(zip(i,j))
            str_permutation = ["".join([str(a) for a in k]) for k in test]
            str_permutation = [int(a) for a in str_permutation]
            number_list.append(str_permutation)
    return number_list

if __name__ == "__main__":
    number = 0
    for x in sys.stdin:
        number = int(x)
    ans = permute_list(number)
    print(len(ans))
    for an in ans:
        print(*an)