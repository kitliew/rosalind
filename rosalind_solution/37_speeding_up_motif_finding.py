# Problem
# A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].
#
# The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.
#
# Given: A DNA string s (of length at most 100 kbp) in FASTA format.
#
# Return: The failure array of s.
#
# Sample Dataset
# >Rosalind_87
# CAGCATGGTATCACAGCAGAG
# Sample Output
# 0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0

#CAGCATGGTATCACAGCAGAG
#000120000001212345300

import sys



def readfile(filename):
    with open(filename) as file:
        dna = file.read().strip().partition("\n")[-1].replace("\n","")
    return dna

def motif_finding(dna):
    # initiate answer array
    array_ans = [0]*len(dna)

    # iterate through every dna index
    for i in range(1, len(dna)):

    # find first match
        for j in range(i+1):

    # if right == left
            if dna[i:i+j+1] == dna[0:j+1]:
                # current array_ans     array_ans[i:i+j+1]
                ans = [max(x) for x in zip(array_ans[i:i+j+1], list(range(1,j+2)))]
                array_ans[i:i+j+1] = ans
            else:
                break
    return array_ans

if __name__ == "__main__":
    dna = readfile(sys.argv[1])
    print(*motif_finding(dna))

