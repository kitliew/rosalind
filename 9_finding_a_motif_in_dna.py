s1= "GATATATGCATATACTT"
s2= "ATAT"

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print(i+1)
