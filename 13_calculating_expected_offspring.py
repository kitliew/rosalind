import sys

"""
#INPUT:
#6 non-negative integers < 20k
#Represent number of couples in each genotype pairing:

AA AA   AA AA AA AA 100
AA Aa   AA Aa AA Aa 100
AA aa   Aa Aa Aa Aa 100
Aa Aa   AA Aa aA aa 75
Aa aa   Aa Aa aa aa 50
aa aa   aa aa aa aa 0


#OUTPUT:
#expected number of offspring dissplaying the dominant phenotype
#every couple has exactly 2 offspring
"""

def offspring(a,b,c,d,e,f):
    return (a*2)+ (b*2)+ (c*2)+ (d*1.5)+ (e*1)+ (f*0)

for line in sys.stdin:
    a,b,c,d,e,f = map(int, line.split())
    print(offspring(a,b,c,d,e,f))
