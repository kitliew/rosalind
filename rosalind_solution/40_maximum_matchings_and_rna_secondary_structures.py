# Problem
#
# Figure 1. The bonding graph of s = UAGCGUGAUCAC (left) has a perfect matching of basepair edges, but this is not the case for t = CAGCGUGAUCAC (right), in which one symbol has been replaced.
#
# Figure 2. A maximum matching (highlighted in red) is shown in each of the three graphs above. You can verify that no other matching can contain more edges. (Courtesy: Miym, Wikimedia Commons User)
#
# Figure 3. A red maximum matching of basepair edges in the bonding graph for t = CAGCGUGAUCAC.
# The graph theoretical analogue of the quandary stated in the introduction above is that if we have an RNA string s that does not have the same number of occurrences of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the bonding graph of s cannot possibly possess a perfect matching among its basepair edges. For example, see Figure 1; in fact, most bonding graphs will not contain a perfect matching.
#
# In light of this fact, we define a maximum matching in a graph as a matching containing as many edges as possible. See Figure 2 for three maximum matchings in graphs.
#
# A maximum matching of basepair edges will correspond to a way of forming as many base pairs as possible in an RNA string, as shown in Figure 3.
#
# Given: An RNA string s of length at most 100.
#
# Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
#
# Sample Dataset
# >Rosalind_92
# AUGCUUC
# Sample Output
# 6

import sys

def readfile(filename):
    with open(filename) as file:
        dna = file.read().strip().partition("\n")[-1].replace("\n","")
    return dna

def factorial(low, high):
    answer = 1
    for i in range(high-low+1,high+1):
        answer = answer * i
    return answer

def matching(dna):
    count_dic = {}
    for i in set("ACGU"):
        count_dic[i] = dna.count(i)
    max_AU = max(count_dic["A"], count_dic["U"])
    min_AU = min(count_dic["A"], count_dic["U"])
    max_CG = max(count_dic["C"], count_dic["G"])
    min_CG = min(count_dic["C"], count_dic["G"])
    answer_AU = factorial(min_AU,max_AU)
    answer_CG = factorial(min_CG,max_CG)
    return answer_AU * answer_CG

test = readfile(sys.argv[1])
test1 = matching(test)
print(test1)