import sys
from os import path

FILE = False # If needed change during submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

n = get_int() # Number of test cases



# Write Solution Here:
done = False
for i in range(1, n):
    if (n-i) % 2 == 0 and i % 2 == 0:
        sys.stdout.write("YES")        
        done = True
        break
if not done:
    sys.stdout.write("NO")