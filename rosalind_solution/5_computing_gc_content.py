def gc_content(sequence):
    return((sequence.count("G") + sequence.count("C")) / len(sequence))

def read_FASTA_strings(filename):
    """return a list of FASTA strings"""
    with open(filename) as file:
        return file.read().split(">")[1:]       #split at ">", ignore 1st ">"

def read_FASTA_entries(filename):
    """return a list of tuple
    [](FASTA_info, "blank", sequence)]"""
    return [seq.partition("\n") for seq in read_FASTA_strings(filename)]

#output as list:
def read_FASTA_sequence(filename):
    """return a list of list
    [[FASTA_info, sequence]]"""
    return[[seq[0], seq[2].replace("\n", "")]           #1st item of tuple and 3rd item of tuple with newline removed
            for seq in read_FASTA_entries(filename)]

def gc_FASTA(filename):
    """return a list of list
    [[FASTA_info, gc_percentage]]"""
    return [[seq[0], gc_content(seq[1])]
            for seq in read_FASTA_sequence(filename)]

def gc_max(filename):
    """return FASTA_info, gc_content"""
    dictionary = dict(gc_FASTA(filename))
    gc_list = []
    for seq in gc_FASTA(filename):
        gc_list.append(seq[1])
    highest_gc = max(gc_list)               #find highest gc from list
    for name, value in dictionary.items():
        if value == highest_gc:             #find FASTA_info with given max value
            return name, value

print(gc_max("test_fasta.txt"))


#REVISION AFTER 5 month
"""
def gc_content(sequence):
    return((sequence.count("G") + sequence.count("C")) / len(sequence))

def read_fasta_file(filename):
    with open(filename) as file:
        indi_samp = file.read().strip().split(">")[1:]      #return [(NAME\nSEQUENCE), (NAME\nSEQUENCE)]
        name, gc = "", 0
        for item in indi_samp:
            a, b, c = item.partition("\n")                  #return "NAME", "\n", "SEQUENCE"
            if gc_content(c.replace("\n", "")) > gc:
                name = a
                gc = gc_content(c.replace("\n", ""))
    return name, gc
    #return a, c.replace("\n", "")

print(read_fasta_file("test_fasta.txt"))
"""
