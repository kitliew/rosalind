#!/usr/bin/env python3

# Problem
#
# Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
#
# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
#
# Given: Positive integers n≤100 and m≤20.
#
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
#
# Sample Dataset
# 6 3
# Sample Output
# 4

import sys

#TWO WAYS OF DOING

#FIRST WAY  (counting)
#current = sum from list[:-1]
#make current as past = list[1:]
def fib1(n, k=1):
    a,b = 1,1
    lst = [1,1]
    for i in range(2,n):
        a,b = b, k*a+b
        lst.append(b)
    return lst

def fib_death(m,n, k=1):
    a,b = fib(m,k), sum(fib(m,k)[:-1])
    for i in range(m, n-1):
        a.append(b)
        a,b = a[1:], sum(a[1:-1])
    return b


#SECOND WAY OF DOING
#keeping track of rabbits ages

def fib(n, m=1):
    #draw an array/plan
    ages = [1] + [0]*(m-1)
    for i in range(n-1):
        #first index(1month old rabbit) is sum from 2nd index onwards(2month old onwards will reproduce)
        #all other index move up by one except last index(oldest rabbit which is dying)
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

for line in sys.stdin:
    a,b = line.strip().split()
    a,b = int(a), int(b)
    print(fib(a, m=b))
