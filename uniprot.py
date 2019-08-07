import requests
import re
import sys
import concurrent.futures


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
    for m in re.finditer(r'(?=N[^P][ST][^P])', protein):        #r"PRE(?=POST)  Matches if POST matches after PRE. Doesn't consume any string
        loc_list.append(m.start()+1)
    if len(loc_list) != 0:
        print(str(ID) + "\n" + ' '.join(str(x) for x in loc_list))

def main():
    ID = [str(x.strip()) for x in sys.stdin]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(find_iloc_protein_motif, ID)


if __name__ == "__main__":
    main()
