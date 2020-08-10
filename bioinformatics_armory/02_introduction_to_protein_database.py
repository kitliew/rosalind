# Problem
# The UniProt Knowledgebase can be found here.
#
# You can see a complete description of a protein by entering its UniProt access ID into the site's query field. Equivalently, you may simply insert its ID (uniprot_id) directly into a UniProt hyperlink as follows:
#
# http://www.uniprot.org/uniprot/uniprot_id
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
#
# Swiss-Prot holds protein data as a structured .txt file. You can obtain it by simply adding .txt to the link:
#
# http://www.uniprot.org/uniprot/uniprot_id.txt
# Given: The UniProt ID of a protein.
#
# Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
#
# Sample Dataset
# Q5SLP9
# Sample Output
# DNA recombination
# DNA repair
# DNA replication

import sys
from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw(sys.stdin)

record = SwissProt.read(handle)

test = [item for item in record.cross_references if item[0] == "GO"]
result = [item[2].replace("P:","") for item in test if item[2].startswith("P:")]

print(result)