import requests
import re
import sys
import concurrent.futures

# Problem
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
#
# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
#
# http://www.uniprot.org/uniprot/uniprot_id
# Alternatively, you can obtain a protein sequence in FASTA format by following
#
# http://www.uniprot.org/uniprot/uniprot_id.fasta
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
#
# Given: At most 15 UniProt Protein Database access IDs.
#
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
#
# Sample Dataset
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST
# Sample Output
# B5ZC00
# 85 118 142 306 395
# P07204_TRBM_HUMAN
# 47 115 116 382 409
# P20840_SAG1_YEAST
# 79 109 135 248 306 348 364 402 485 501 614

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
