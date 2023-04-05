a = input()
ans = ""
for i in a:
    if i.isupper():
        ans += i.lower()
    elif i.islower():
        ans += i.upper()
print(ans)