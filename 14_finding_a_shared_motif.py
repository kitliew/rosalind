import sys

"""
Input:
a collection of k DNA strings in FASTA format

Output:
Longest common substring of collection
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
    return sorted(samples)

def lcs(filename):
    strings = fasta_file(filename)
    short_string = strings[0]
    other_string = strings[1:]

    l = len(short_string)
    longest_string= ""

    for i in range(0, l):
        for j in range(l, i+len(longest_string), -1):
            s1 = short_string[i:j]

            matched_all = True
            for s2 in other_string:
                if s1 not in s2:
                    matched_all = False
                    break
            if matched_all:
                longest_string=s1
                break
    return longest_string

def main():
    filename=sys.argv[1]
    print(lcs(filename))

if __name__ == "__main__":
    main()
