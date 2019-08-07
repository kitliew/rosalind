#!/usr/bin/env python3

import sys



content = sys.stdin
k = 1
m = 1
n = 1
total = k + m + n
for line in content:
    k,m,n = line.strip().split()

k = int(k)
m = int(m)
n = int(n)

#k=2
#m=2
#n=2
#total = k+m+n
# k = dominant
# m = hetero
# n = recessive
# total = k + m + n


#100% getting dominant offspring
def test(k,m,n):
    kk = (k/total) * (k-1)/(total-1)
    km = (k/total) * (m/(total-1)) + ((m/total) * (k/(total-1)))
    kn = (k/total) * (n/(total-1)) + ((n/total) * (k/(total-1)))

    #75% getting dominant offspring
    mm = (m/total) * (m-1)/(total-1)

    #50% getting recessive
    mn = (m/total) * (n/(total-1)) + (n/total) * (m/(total-1))

    #getting recessive only
    nn = (n/total) * (n-1)/(total-1)
    return(kk + km + kn + (0.75*mm) + (0.5*mn))

print(test(k,m,n))


"""
#universe function
def firstlaw(k,m,n):
   N = float(k+m+n)
   return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))
"""
