#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:35:45 2017

@author: sbowie
"""

# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

def rabbits(n):
    n_minus_3 = 0
    n_minus_2 = 0
    n_minus_1 = 0
    n_0 = 0
    n_plus_1 = 1
    for i in range (0,n):
        n_minus_3,n_minus_2,n_minus_1,n_0,n_plus_1 = n_minus_2,n_minus_1,n_0,n_plus_1,n_0 + n_plus_1 - n_minus_3
    return n_0
    
'''
slower recursive version
def rabbits(n):
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)
'''

print rabbits(10)
#>>> 35

s = ""
for i in range(1,12):
    s = s + str(rabbits(i)) + " "
print s
#>>> 1 1 2 3 5 7 11 16 24 35 52

print rabbits(30)