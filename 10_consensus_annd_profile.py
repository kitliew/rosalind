#!/usr/bin/env python3
import sys

"""
Output:
#count ACGT at each index
#return consensus(highest nucleotide) at each index

Input:
#10 DNA strings of equal length
#FASTA format
"""


def fasta_file(filename):
    #only need to collect a list of DNA string
    samples=[]
    with open(filename) as file:
        #separate each entries  return list
        individual = file.read().split(">")[1:]
        #separate name and DNA string within entries    return list of DNA string
        for i in individual:
            dna = i.partition("\n")[-1].strip().replace("\n", "")
            samples.append(dna)
    return samples

def count_index(filename):
    #getting list of DNA string
    samples = fasta_file(filename)
    #group DNA string index together
    test = list(zip(*samples))
    #for each index group, count ACGT
    A_count = []
    C_count = []
    G_count = []
    T_count = []
    for i in test:
        A_count.append(i.count("A"))
        C_count.append(i.count("C"))
        G_count.append(i.count("G"))
        T_count.append(i.count("T"))
    return A_count,C_count, G_count, T_count

def consensus(filename):
    samples = fasta_file(filename)
    test = list(zip(*samples))
    #prepare a list of highest index to store
    consensus = []
    for i in test:
        #making a dict with nucleotide as key; number of occurance as value
        #counter position is crucial. will reset counter at each index(during iterate)
        counter = {}
        for x in "ACGT":
            counter[x] = i.count(x)
        largest=0
        best = ""
        for c,v in counter.items():
            #if value is larger than 0 or current value stored
            if v > largest:
                largest = v
                best = c
        consensus.append(best)
    #return a string of DNA
    return("".join(consensus))

def main():
    filename = sys.argv[1]
    A,C,G,T = count_index(filename)
    print(consensus(filename))
    print("A:", *A)
    print("C:", *C)
    print("G:", *G)
    print("T:", *T)

if __name__ == "__main__":
    main()
