import sys
print(sys.version)


def complement_strand(sequence):
    seq = sequence[::-1]
    change_DNA = str.maketrans("ACGT", "TGCA")
    print(seq.translate(change_DNA))

complement_strand("AAAACCCGGT")
