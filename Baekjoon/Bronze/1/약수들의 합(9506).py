import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    lst = [str(i) for i in range(1, n) if not n % i]
    if n != sum(map(int, lst)):
        print(f"{n} is NOT perfect.")
    else:
        print(f'{n} = {" + ".join(lst)}')