import sys
from os import path
from itertools import permutations
from collections import Counter
import math

FILE = True # If needed change during submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

n = get_int() # Number of test cases

# Write Solution Here:
final_result = []
for tests in range(n):
    length = get_int()
    word = list(get_string())
    c = Counter(word)
    
    mi = float('inf')
    new = ""
    
    
    for uniq in c:
        for i in range(length):
            test = word[:]
            test[i] = uniq
            t = mi
            mi = min(mi, (math.factorial(length))/(math.factorial(length-len(c))))
            if t != mi:        
                new = "".join(test)
    
    final_result.append(new)
    


for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')