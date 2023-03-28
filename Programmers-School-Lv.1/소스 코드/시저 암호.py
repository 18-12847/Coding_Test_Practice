def solution(s, n):
    ans = []
    for i in range(len(s)):
        if ord(s[i]) == 32:
            ans.append(" ")
        elif 64 < ord(s[i]) < 91 and 64 < ord(s[i]) + n < 91:
            ans.append(chr(ord(s[i]) + n))
        elif 64 < ord(s[i]) < 91 and ord(s[i]) + n > 90:
            ans.append(chr(ord(s[i]) + n - 26))
        elif 96 < ord(s[i]) < 123 and 96 < ord(s[i]) + n < 123:
            ans.append(chr(ord(s[i]) + n))
        elif ord(s[i]) + n > 122:
            ans.append(chr(ord(s[i]) + n - 26))
    return "".join(ans)