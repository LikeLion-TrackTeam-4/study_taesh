import copy

n = int(input())
cost_list = []
for i in range(n):
    cost_list.append(list(map(int, input().split())))

# print(type(cost_list[0][0]))
cost_sum = 0
exc = 99
for i in range(n):
    temp_list = copy.deepcopy(cost_list[i])
    if i == 0:
        cost_sum = cost_sum + min(temp_list)
        exc = temp_list.index(min(temp_list))
    else:
        temp_list.pop(exc)
        cost_sum = cost_sum + min(temp_list)
        # 만약 다음 으로 작은 값과의 차 가
        # 다음 집의 차보다 작다면 바꾸자
        if exc == 1:
            if temp_list.index(min(temp_list)) == 1:
                exc = 2
            else:
                exc = 0
        elif exc == 0:
            exc = temp_list.index(min(temp_list)) + 1
        else:
            exc = temp_list.index(min(temp_list))
    print("----", exc, "----")

print(cost_sum)
