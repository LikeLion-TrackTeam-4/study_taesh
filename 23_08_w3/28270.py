# 1.                    1.
#   2.                      1.
#     3.                2.  
#   2.        형태를         1.
#                           2.  형태로 바꾸자
# 입력은 깊이 우선 탐색

def main():
    nums = int(input())
    lists = input().split()
    # print(lists)

    stack = []
    ans = []

    for i in range(nums):
        if len(lists) != nums:
            print(-1)
            return
        if lists[0] != '1':
            print(-1)
            return
        if i < nums - 1 and lists[i] != lists[i + 1] and int(lists[i]) != int(lists[i + 1]) - 1 and int(lists[i]) < int(
                lists[i + 1]) + 1:
            print(-1)
            return
        # 입력값 체크 ----
        rem = -1
        for j in stack:
            if lists[i] < j:
                rem = j
        while rem in stack:
            stack.remove(rem)

        if lists[i] not in stack:
            ans.append(1)
            stack.append(lists[i])
            # print('1삽입')
        elif lists[i] in stack:
            # print(stack, lists[i], stack.count(lists[i]))
            ans.append(stack.count(lists[i])+1)
            stack.append(lists[i])
            # print(stack.count(lists[i])-1, ' 삽입1')

    print(*ans)

main()
