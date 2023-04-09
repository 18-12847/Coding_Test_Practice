tot = 0
while True:
    try:
        a = int(input())
        tot += a
    except:
        print(tot)
        break