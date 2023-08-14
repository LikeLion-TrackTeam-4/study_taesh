# https://www.acmicpc.net/problem/1065

# 주어진 숫자보다 작은 수 중에 한수( 그 숫자의 각각 자릿수를 떼서 등차수열인가 판별 )의 개수 찾기

##

val = int(input())

num = 0

if val < 100:
    print(val)
else:
    num += 99
    cnt = 100
    temp = val
    nums = []
    while True:
        if temp >= 10:
            nums.insert(0, temp % 10)
            temp = int(temp / 10)
        else:
            nums.insert(0, temp)
            break
    diff = 0
    for i in nums:
        pass
#       리스트화한 숫자들 넘어가면서 diff 갱신해서 달라지면 break 지금 리스트화 부분까지 while문 씌워야함


