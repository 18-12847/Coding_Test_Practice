import sys
from itertools import product
input = sys.stdin.readline
father = input().split()
mother = input().split()
pro = sorted(set(father+mother))
for i in product(pro, repeat = 2):
    print(*i)