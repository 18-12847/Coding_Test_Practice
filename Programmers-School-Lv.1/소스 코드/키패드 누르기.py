def solution(numbers, hand):
    if hand == "right":
        hand = "R"
    else:
        hand = "L"
    ans = []
    dic = {0:0, 1:1, 2:2, 3:1, 4:2, 5:3, 6:2, 7:3, 8:4, 9:3, 10:4}
    left, right = 10, 12
    for i in numbers:
        if i in [1, 4, 7]:
            ans.append("L")
            left = i
        elif i in [3, 6, 9]:
            ans.append("R")
            right = i
        elif i in [2, 5, 8]:
            if dic[abs(i-left)] > dic[abs(i-right)]:
                ans.append("R")
                right = i
            elif dic[abs(i-left)] == dic[abs(i-right)]:
                if hand == "R":
                    ans.append("R")
                    right = i
                else:
                    ans.append("L")
                    left = i
            else:
                ans.append("L")
                left = i
        elif i == 0:
            if dic[abs(11-left)] > dic[abs(11-right)]:
                ans.append("R")
                right = 11
            elif dic[abs(11-left)] == dic[abs(11-right)]:
                if hand == "R":
                    ans.append("R")
                    right = 11
                else:
                    ans.append("L")
                    left = 11            
            else:
                ans.append("L")
                left = 11
    return "".join(ans)