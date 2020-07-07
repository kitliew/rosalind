# Problem
# For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the proportion of corresponding symbols that differ between s1 and s2.
#
# For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings), we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).
#
# Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
#
# Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
#

example = """>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
"""

def read_fasta(content):
    content = content.strip().split(">")[1:]
    id = []
    dna = []
    for entry in content:
        i, j = entry.partition("\n")[::2]
        id.append(i)
        dna.append(j.replace("\n",""))
    return id, dna

def count_point_mutation(dna1,dna2):
    return "%.5f" % (sum([a!=b for (a,b) in zip(dna1,dna2)])/len(dna1))

def test(content):
    id, dna = read_fasta(content)
    for i in range(len(dna)):
        row = []
        for j in range(len(dna)):
            row.append(count_point_mutation(dna[i],dna[j]))
        print(*row)

print(read_fasta(example))
print(test(example))