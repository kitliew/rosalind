#!/usr/bin/env python3

# Problem
# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
#
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
#
# Given: A DNA string s of length at most 1 kbp in FASTA format.
#
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
#
# Sample Dataset
# >Rosalind_99
# AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
# Sample Output
# MLLGSFRLIPKETLIQVAGSSPCNLS
# M
# MGMTPRLGLESLLE
# MTPRLGLESLLE

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

def decode(coded):
    result = ""
    for i in range(0, len(coded) - (len(coded) % 3), 3):
        test = traDict[coded[i:i+3]]
        if test == "Stop":
            return result
        else:
            result += traDict[coded[i:i+3]]

def dna_to_prot(dna):
    result = []
    # represent 3 ORF
    for x in range(3):
        for i in range(x, len(dna) - (len(dna) %3), 3):
            if dna[i:i+3] == "ATG":
                _aa = decode(dna[i:])
                result += [_aa] if _aa is not None else []
    return result

def rev_comple(dna):
    rev = str.maketrans("ACGT", "TGCA")
    dna_r = dna.translate(rev)[::-1]
    return dna_r

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        dna = file.read().strip().partition("\n")[-1].replace("\n","")
        dna_r = rev_comple(dna)
        result = dna_to_prot(dna) + dna_to_prot(dna_r)
        for i in set(result):
            print(i)
