def cnt_pnt_mutation(filename):
    with open(filename) as file:
        count = 0
        lines = file.readlines()
        seq1 = lines[0]
        seq2 = lines[1]
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
        return count

print(cnt_pnt_mutation("rosalind_hamm.txt"))


#method 2
def pnt_mutation(filename):
    with open(filename) as file:
        lines = file.readlines()
        return sum([a != b for a, b in zip(lines[0],lines[1])])

print(pnt_mutation("rosalind_hamm.txt"))
