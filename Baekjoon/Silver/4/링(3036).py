from fractions import Fraction
import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    s = Fraction(lst[i] / lst[0]).limit_denominator()
    print(f"{s.denominator}/{s.numerator}")