import sys
input = sys.stdin.readline
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = (len(arr) + 1) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    merged = []
    idx_arr1 = idx_arr2 = 0
    while idx_arr1 < len(arr1) and idx_arr2 < len(arr2):
        if arr1[idx_arr1] < arr2[idx_arr2]:
            merged.append(arr1[idx_arr1])
            ans.append(arr1[idx_arr1])
            idx_arr1 += 1
        else:
            merged.append(arr2[idx_arr2])
            ans.append(arr2[idx_arr2])
            idx_arr2 += 1

    merged.extend(arr1[idx_arr1:])
    ans.extend(arr1[idx_arr1:])
    merged.extend(arr2[idx_arr2:])
    ans.extend(arr2[idx_arr2:])
    return merged

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
merge_sort(arr)
print(ans[k-1] if len(ans) >= k else -1)

# merge_sort(0, 4) : input [4, 5, 1, 3, 2]
# ├─ merge_sort(0, 2) : input [4, 5, 1]
# │  ├─ merge_sort(0, 1) : input [4, 5]
# │  │  ├─ merge_sort(0, 0) : input [4]
# │  │  └─ merge_sort(1, 1) : input [5]
# │  │  └─ merge(0, 0, 1) : output [4, 5]
# │  └─ merge_sort(2, 2) : input [1]
# │  └─ merge(0, 1, 2) : output [1, 4, 5]
# └─ merge_sort(3, 4) : input [3, 2]
#    ├─ merge_sort(3, 3) : input [3]
#    └─ merge_sort(4, 4) : input [2]
#    └─ merge(3, 3, 4) : output [2, 3]
# └─ merge(0, 2, 4) : output [1, 2, 3, 4, 5]

# Dividing [4, 5, 1, 3, 2] into arr1 : [4, 5, 1] and arr2 : [3, 2]
# Dividing [4, 5, 1] into arr1 : [4, 5] and arr2 : [1]
# Dividing [4, 5] into arr1 : [4] and arr2 : [5]
# Merging [4] and [5] into [4, 5]
# Merging [4, 5] and [1] into [1, 4, 5]
# Dividing [3, 2] into arr1 : [3] and arr2 : [2]
# Merging [3] and [2] into [2, 3]
# Merging [1, 4, 5] and [2, 3] into [1, 2, 3, 4, 5]
# arr : [1, 2, 3, 4, 5]
# ans : [4, 5, 1, 4, 5, 2, 3, 1, 2, 3, 4, 5]