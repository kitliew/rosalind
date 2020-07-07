import sys
import itertools

# reference: https://cseweb.ucsd.edu/classes/wi05/cse206b/notes/L3.pdf
# https://github.com/erexhepa/Rosalind/blob/master/042_REAR.py
#
# Problem
# A reversal of a permutation creates a new permutation by inverting some interval of the permutation; (5,2,3,1,4), (5,3,4,1,2), and (4,1,2,3,5) are all reversals of (5,3,2,1,4). The reversal distance between two permutations π and σ, written drev(π,σ), is the minimum number of reversals required to transform π into σ (this assumes that π and σ have the same length).
#
# Given: A collection of at most 5 pairs of permutations, all of which have length 10.
#
# Return: The reversal distance between each permutation pair.
#
# Sample Dataset
# 1 2 3 4 5 6 7 8 9 10
# 3 1 5 2 7 4 9 6 10 8
#
# 3 10 8 2 5 4 7 1 6 9
# 5 2 3 1 7 4 10 8 6 9
#
# 8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4
#
# 3 9 10 4 1 8 6 7 5 2
# 2 9 8 5 1 7 3 4 6 10
#
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10
# Sample Output
# 9 4 5 7 0
#
# def read_file(filename):
#     with open(filename) as file:
#         content = file.readlines()
#         content = [numbers.replace("\n","").split(" ") for numbers in content]
#         pairs = zip(content[::3], content[1::3])
#     return pairs
#
# def arrange(pair):
#     counter = 0
#     new_string = pair[0]
#     for i in range(len(pair[1])):
#         target = new_string.index(pair[1][i])
#         if pair[1][i] != new_string[i]:
#             counter += 1
#             new_string = new_string[0:i] + new_string[i:target+1][::-1] + new_string[target+1:]
#     return counter
#
# def SimpleReversalSort(filename):
#     ans = []
#     tup_lis = read_file(filename)
#     for pairs in tup_lis:
#         print(pairs)
#         ans.append(arrange(pairs))
#     return ans

def file_read(filename):
    """return a list of pair_in_list, [[[1,2],[3,4]] , [[5,6],[7,8]]]"""
    # different from the reference source which generate map object. (Map object can only iterate over once)
    with open(filename) as file:
        content = [pair.split("\n") for pair in file.read().strip().split("\n\n")]
        for index,pair in enumerate(content):
            content[index] = [list(map(int, single.split())) for single in pair]
    return content

def breakpoint_count(number_list):
    """Adding 0 and n+1 to the number list.
    Sum of breakpoint, adjecent numbers abs(n - n+1)
    """
    number_list = [0] + list(number_list) + [len(number_list)+1]
    return sum(map(lambda x, y: abs(x - y) != 1, number_list[1:], number_list[:-1]))

def breakpoint_index(number_list):
    """Return index of breakpoints in number_list"""
    number_list = [0] + list(number_list) + [len(number_list) + 1]
    ans = itertools.compress(range(len(number_list)-1), map(lambda x, y: abs(x - y) != 1, number_list[1:], number_list[:-1]))
    return list(ans)

def better_greedy_breakpoint(perm1, perm2):
    to_identity = {value: i + 1 for i, value in enumerate(perm2)}
    normalized_perm = [to_identity[value] for value in perm1]

    # Quick lambda function to reverse a region in the permutation.
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]

    # Initialize Variables
    normalized_perm = tuple(normalized_perm)
    current_perms = [normalized_perm]
    min_breaks = breakpoint_count(normalized_perm)
    dist = 0

    # Run the greedy BFS breakpoint reduction sorting.
    while min_breaks>0:
        new_perms = []
        dist += 1
        # Iterate over all combinations of breakpoint indices for all  current minimal permutations.
        for perm in current_perms:
            for rev_ind in itertools.product(breakpoint_index(perm), repeat=2):
                # Store some temporary variables for the given iteration.
                temp_perm = tuple(rev_perm(perm, rev_ind[0], rev_ind[1] - 1))
                temp_breaks = breakpoint_count(temp_perm)

                # Done we have no breakpoints.
                if temp_breaks == 0:
                    return dist

                # Create a new dictionary and update the minimum number of breakpoints if we've found a reduction.
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = [temp_perm]

                # Add to the dictionary if the current breakpoints match the minimum number.
                elif temp_breaks == min_breaks:
                    new_perms.append(temp_perm)

        current_perms = new_perms

    else:
        return 0

content = file_read(sys.argv[1])

min_dists = [str(min(better_greedy_breakpoint(p1, p2),better_greedy_breakpoint(p2,p1))) for p1, p2 in content]
print(*min_dists)




