# Problem
# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
#
# Sample Dataset
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
# Sample Output
# MVYIADKQHVASREAYGHMFKVCA

import sys

_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

rna_dna = str.maketrans("U", "T")
_table = _table.translate(rna_dna)
traL =  _table.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

def fasta_file(filename):
    samples=[]
    with open(filename) as file:
        individual = file.read().split(">")[1:]
        for i in individual:
            dna = i.partition("\n")[-1].strip().replace("\n", "")
            samples.append(dna)
    return samples

def decode(coded):
    result = ""
    for i in range(0, len(coded) - (len(coded) % 3), 3):
        if i + 3 > len(coded):
            break
        if traDict[coded[i:i+3]] != "Stop":
            result += traDict[coded[i:i+3]]
        else:
            break
    return result

def splicing(seq):
    dna = seq[0]
    target = seq[1:]
    for i in target:
        dna = dna.replace(i,"")
    return dna

if __name__=="__main__":
    sequences = fasta_file(sys.argv[1])
    dna = splicing(sequences)
    protein = decode(dna)
    print(protein)
