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
    for i in range(0, len(coded), 3):
        if traDict[coded[i:i+3]] != "Stop":
            result += traDict[coded[i:i+3]]
        else:
            break
    return result

def dna_to_prot(dna):
    result = []
    # represent 3 ORF
    for x in range(3):
        seq = dna[x:]
    # position where start codon is found
        current_pos = 0
    # scanning through seq (window sliding), starting from previous codon found (pos + 1)
        for i in range(current_pos, len(seq), 3):
            if seq[i:i+3] == "ATG":
                result.append(decode(seq[i:]))
    return result

def rev_comple(dna):
    rev = str.maketrans("ACGT", "TGCA")
    dna_r = dna.translate(rev)[::-1]
    return dna_r

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        dna = file.read().strip().split("\n")[-1].replace("\n","")
        dna_r = rev_comple(dna)
        result = dna_to_prot(dna) + dna_to_prot(dna_r)
        for i in set(result):
            print(i)
