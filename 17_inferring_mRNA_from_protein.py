import sys

string = """UUU F      CUU L      AUU I      GUU V
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


traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))
rna_all = traL[1::2]
rna = set(rna_all)
tracount = {a: rna_all.count(a) for a in rna_all}

def decode(coded):
    result = 3
    for i in range(0, len(coded)):
        result *= tracount[coded[i:i+1]]
    return result

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        seq = file.read().strip()
        print(decode(seq))
