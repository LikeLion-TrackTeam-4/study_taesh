# https://www.acmicpc.net/problem/1476

# E (1 ~ 15) S (1 ~ 28) M (1 ~ 19) 로 년도를 나타낸다.
# 예를들어 15년이면 ESM : 15 15 15, 16년이면 ESM : 1 15 15 이다.
# 즉 이는, 년도를 Y라고 할때, ESM : Y%15 Y%28 Y%19라 할 수 있다.
# 단 단순히 % 계산시 Y%15가 0 이면 0이 표시 되어 버리므로 예외처리 해준다.

def main():
    E, S, M = input().split()
    E, S, M = int(E), int(S), int(M)
    if E == 15:
        E = 0
    if S == 28:
        S = 0
    if M == 19:
        M = 0
    cnt = 1

    while True:
        if cnt % 15 == E and cnt % 28 == S and cnt % 19 == M:
            ans = cnt
            break
        cnt += 1

    print(ans)


main()
