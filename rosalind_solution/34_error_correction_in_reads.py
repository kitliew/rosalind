# Problem
# As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly.
#
# Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
#
# s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
# s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
# Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
#
# Sample Dataset
# >Rosalind_52
# TCATC
# >Rosalind_44
# TTCAT
# >Rosalind_68
# TCATC
# >Rosalind_28
# TGAAA
# >Rosalind_95
# GAGGA
# >Rosalind_66
# TTTCA
# >Rosalind_33
# ATCAA
# >Rosalind_21
# TTGAT
# >Rosalind_18
# TTTCC
# Sample Output
# TTCAT->TTGAT
# GAGGA->GATGA
# TTTCC->TTTCA

import sys

def readfile(filename):
    dnas = []
    with open(filename) as file:
        contents = file.read().strip().split(">")[1:]
        for content in contents:
            dnas.append(content.partition("\n")[-1].replace("\n", ""))
    return dnas

def rev_compliment(dna):
    rev = str.maketrans("ACGT", "TGCA")
    result = dna.translate(rev)[::-1]
    return result

def countings(filename):
    collection = {}
    dna_list = readfile(filename)
    for dna in dna_list:
        r_dna = rev_compliment(dna)
        if dna in collection:
            collection[dna] += 1
        elif r_dna in collection:
            collection[r_dna] += 1
        else:
            collection[dna] = 1
    # occur once
    old_read = []
    # occur twice
    new_read = []
    for dna, numb in collection.items():
        if numb >= 2:
            new_read.append(dna)
        else:
            old_read.append(dna)
    return old_read, new_read

def pairing(filename):
    old_read, new_read = countings(filename)
    new_read = [rev_compliment(n) for n in new_read] + new_read
    result = {}

    for old in old_read:
        for new in new_read:
            current_max_score = len(old)
            for index in range(0, len(new)):
                if old[index] == new[index]:
                    current_max_score -= 1
            if current_max_score == 1:
                result[old] = new
                break
    return result

if __name__ == "__main__":
    filename = sys.argv[1]
    for old, new in pairing(filename).items():
        print("{}->{}".format(old,new))