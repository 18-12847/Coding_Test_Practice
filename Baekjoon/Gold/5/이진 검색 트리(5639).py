import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def postorder(start, end):
    if start > end: #시작 인덱스가 끝 인덱스보다 크면 이진 탐색 트리가 아니므로 종료
        return
	#오른쪽 서브트리가 없을 경우를 대비해서 end + 1로 설정하면 mid가 end보다 큰 상태로 재귀가 호출되고
    mid = end + 1 #위의 조건문에 걸려서 함수가 종료된다
    for i in range(start + 1, end + 1): #해당 리스트에서 루트(start(0)번째) 다음부터 끝까지 반복하다가
        if tree[start] < tree[i]: #루트(start(0)번째) 보다 큰 값이 있으면 mid를 해당 인덱스로 저장하고 종료
            mid = i
            break
    postorder(start + 1, mid - 1) #왼쪽 서브 트리 범위는 루트 다음부터 mid전까지
    postorder(mid, end) #오른쪽 서브 트리 범위는 mid부터 끝까지
    print(tree[start])

tree = []
while True:
    try:
        tree.append(int(input().rstrip()))
    except:
        break
postorder(0, len(tree) - 1) #리스트 범위 내에서 실행하기 위함