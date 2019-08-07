import requests
import re
import sys

#Note that re MODULE FUNCTIONS are mostly NON-OVERLAPPED.
#regex module have optional argument overlapped=True

"""
input:
15 UniProt access IDs

Output:
ID
location of motif found
"""

def uniprot_url(IDs):
    """navigate to protein url in FASTA format"""
    base_url = "http://www.uniprot.org/uniprot/"
    url = base_url + IDs + ".fasta"
    return str(url)

def url_content(ID):
    """retrieve ID and protein sequence from FASTA"""
    response = requests.get(uniprot_url(ID))
    text = response.text
    protein = text.partition("\n")[-1].replace("\n", "")
    return ID, protein

def find_protein_motif(ID):
    """find possible protein motif in protein sequence"""
    id, protein = url_content(ID)
    all_target=re.findall(r'(?=N[^P][ST][^P])', protein)
    return list(all_target)

def find_iloc_protein_motif(ID):
    """return exact location of all protein_motif found in string (0+1)"""
    loc_list=[]
    id, protein = url_content(ID)
    for m in re.finditer("N[^P][ST][^P]", protein):
        loc_list.append(m.start()+1)
    return loc_list

def main():
    for line in sys.stdin:
        test = find_iloc_protein_motif(str(line.strip()))
        if len(test) != 0:
            print(line.strip())
            print(*test)

if __name__ == "__main__":
    main()
