# Problem
# For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
#
# By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.
#
# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
#
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
#
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
#
# Sample Dataset
# >Rosalind_56
# ATTAGACCTG
# >Rosalind_57
# CCTGCCGGAA
# >Rosalind_58
# AGACCTGCCG
# >Rosalind_59
# GCCGGAATAC
# Sample Output
# ATTAGACCTGCCGGAATAC

#!/usr/bin/env python3

import sys

def read_fasta(filename):
    sample_dataset = {}
    with open(filename) as file:
        contents = file.read().split(">")[1:]
        return [content.partition("\n")[-1].replace("\n", "") for content in contents]

def find_overlaps(arr, acc=""):
    if len(arr)==0:
        return acc
    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)
    else:
        for i in range(len(arr)):
            x = arr[i]
            for j in range(len(x)//2):
                k = len(x) - j
                if acc.startswith(x[j:]):
                    arr.pop(i)
                    return find_overlaps(arr, x[:j] + acc)
                if acc.endswith(x[:k]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + x[k:])


if __name__=="__main__":
    test = read_fasta(sys.argv[1])
    print(find_overlaps(test))
