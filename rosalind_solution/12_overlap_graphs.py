import sys

"""
#INPUT:
#DNA strings in FASTA format
#O3 == 3 nucleotides match

#OUTPUT:
#sample name
"""
filename = sys.argv[1]

def fasta(filename):
    collection = {}
    with open(filename) as file:
        samples = file.read().strip().split(">")[1:]
        for i in samples:
            a,b = i.partition("\n")[::2]
            collection[a] = b.replace("\n", "")
    return collection

for current, suffix in fasta(filename).items():
    for target, preffix in fasta(filename).items():
        if current != target:
            if suffix[-3:] == preffix[:3]:
                print(current, target)
