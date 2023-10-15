import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
# lst는 높이 0에서 256까지 각 높이에 대한 블록의 개수를 저장하는 리스트
# 처음에는 모든 높이에 대해 0개의 블록이 있으므로 모든 요소를 0으로 초기화
lst = [0] * 257 
# 입력받은 지형의 블록 높이에 대한 개수를 lst에 저장
for _ in range(n):
    for i in map(int, input().split()):
        lst[i] += 1
# tot_block은 지형 전체의 블록 수
# lst[i] * i는 높이 i에 대한 블록의 총 개수이므로 이를 모두 합하면 지형 전체의 블록 수
tot_block = sum([i * lst[i] for i in range(257)])
# min_t는 지금까지 찾은 최소 시간, ans는 그 때의 높이
# 초기값은 각각 무한대와 0으로 설정
min_t, ans = float("inf"), 0 
# 0부터 256까지의 모든 높이에 대해 시도
for height in range(257): 
    add_time, rm_time = 0, 0
    for i in range(257):
        # 높이 i에서 목표 높이 height로 변경하는 데 필요한 시간을 계산
        # 높이를 줄이는 경우 시간은 (i - height) * 2 * lst[i], 높이를 늘리는 경우 시간은 (height - i) * lst[i]
        if i > height:
            add_time += (i - height) * 2 * lst[i]
        else:
            rm_time += (height - i) * lst[i]
    # tot_time은 높이 height에 대한 총 시간
    tot_time = add_time + rm_time
    # tot_block + b는 현재 사용 가능한 블록의 총 수
    # height * n * m은 목표 높이 height에 대해 필요한 블록의 총 수
    # 사용 가능한 블록의 수가 필요한 블록의 수보다 크거나 같은 경우에만 높이 height가 가능
    if tot_block + b >= height * n * m: 
        # 만약 새로 계산한 tot_time이 min_t보다 작거나 (또는 같고 높이가 더 높은 경우) ans를 업데이트
        if tot_time < min_t or (tot_time == min_t and height > ans): 
            min_t = tot_time
            ans = height
print(min_t, ans)