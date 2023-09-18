import sys
input = sys.stdin.readline
def fun(s, n):
    if n < 1:
        return "-"
    string = 3 ** (n-1)
    str1, str2, str3 = s[:string], " " * string, s[string*2:]
    str1 = fun(str1, n - 1)
    str3 = fun(str3, n - 1)
    return str1 + str2 + str3
while True:
    try:
        n = int(input().rstrip())
        print(fun("-" * (3 ** n), n))
    except:
        exit()
# fun("--------- --------- ---------", 3)
# |-- fun("---------         ---------", 2)
# |   |-- fun("---   ---", 1)
# |   |   |-- fun("- -", 0)       # Level 4, Leaf node
# |   |   |-- fun("- -", 0)       # Level 4, Leaf node
# |   |-- fun("---   ---", 1)       
# |       |-- fun("- -", 0)       # Level 4, Leaf node
# |       |-- fun("- -", 0)       # Level 4, Leaf node
# |-- fun("---------         ---------", 2)           
#     |-- fun("---   ---", 1)       
#     |   |-- fun("- -", 0)       # Level 4, Leaf node
#     |   |-- fun("- -", 0)       # Level 4, Leaf node
#     |-- fun("---   ---", 1)       
#         |-- fun("- -", 0)       # Level 4, Leaf node
#         |-- fun("- -", 0)       # Level 4, Leaf node