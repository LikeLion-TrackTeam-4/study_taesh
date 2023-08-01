# https://www.acmicpc.net/problem/14891

# 1,2,3,4 번 톱니바퀴가 있음. 8개의 톱니가 있으며 각 톱니에는 n극 (0), 또는 s극(1)이 있음.
# 5번째줄 입력에는 회전 횟수, 그 이후 입력은 회전할 톱니바퀴와 회전 방향 (시계 : 1, 반시계 -1)이 입력됨.
# 만약 회전하는 톱니바퀴의 톱니와 인접한 톱니바퀴의 톱니가 다르면 같이 회전함. 단, 반대방향으로 회전.
# ex) 1번 회전 시 1번의 오른쪽 톱니와 2번의 오른쪽 톱니가 다르면 회전한다.
# 모든 회전이 끝난 후, 각각의 톱니바퀴의 12시방향 톱니가 1이면 점수를 얻는다 (1번 1점 / 2번 2점 / 3번 4점 / 4번 5점)


class Gear:
    def __init__(self, cogs):
        self.cogs = cogs
        self.top = self.cogs[0]
        self.left = self.cogs[6]
        self.right = self.cogs[2]

    def __str__(self):
        return f"{self.cogs}, top : {self.top}, left : {self.left}, right : {self.right}"

    def set_top_left_right(self):
        self.top = self.cogs[0]
        self.left = self.cogs[6]
        self.right = self.cogs[2]

    def rotate(self, a):
        if a == '1':
            temp = self.cogs[7]
            self.cogs[7] = self.cogs[6]
            self.cogs[6] = self.cogs[5]
            self.cogs[5] = self.cogs[4]
            self.cogs[4] = self.cogs[3]
            self.cogs[3] = self.cogs[2]
            self.cogs[2] = self.cogs[1]
            self.cogs[1] = self.cogs[0]
            self.cogs[0] = temp
        elif a == '-1':
            temp = self.cogs[0]
            self.cogs[0] = self.cogs[1]
            self.cogs[1] = self.cogs[2]
            self.cogs[2] = self.cogs[3]
            self.cogs[3] = self.cogs[4]
            self.cogs[4] = self.cogs[5]
            self.cogs[5] = self.cogs[6]
            self.cogs[6] = self.cogs[7]
            self.cogs[7] = temp
        self.set_top_left_right()


def opposite(a):
    if a == '1':
        return '-1'
    else:
        return '1'


# 입력 및 확인 부분
def main():
    score = 0
    gear1 = Gear(list(input()))
    gear2 = Gear(list(input()))
    gear3 = Gear(list(input()))
    gear4 = Gear(list(input()))
    rotate_num = int(input())
    how_to = []
    for i in range(rotate_num):
        how_to.append(input().split())

    # print(gear1)
    # print(gear2)
    # print(gear3)
    # print(gear4)
    # print(rotate_num)
    # print(how_to)
    # 입력 및 확인 부분

    for i in range(rotate_num):
        if how_to[i][0] == '1':
            # print("1 시작")
            if gear1.right != gear2.left:
                gear1.rotate(how_to[i][1])
                if gear2.right != gear3.left:
                    gear2.rotate(opposite(how_to[i][1]))
                    if gear3.right != gear4.left:
                        gear3.rotate(how_to[i][1])
                        gear4.rotate(opposite(how_to[i][1]))
                    else:
                        gear3.rotate(how_to[i][1])
                else:
                    gear2.rotate(opposite(how_to[i][1]))
            else:
                gear1.rotate(how_to[i][1])

        elif how_to[i][0] == '2':
            # print("2 시작")
            if gear1.right != gear2.left:
                gear1.rotate(opposite(how_to[i][1]))
            if gear2.right != gear3.left:
                gear2.rotate(how_to[i][1])
                if gear3.right != gear4.left:
                    gear3.rotate(opposite(how_to[i][1]))
                    gear4.rotate(how_to[i][1])
                else:
                    gear3.rotate(opposite(how_to[i][1]))
            else:
                gear2.rotate(how_to[i][1])

        elif how_to[i][0] == '3':
            # print("3 시작")
            if gear3.right != gear4.left:
                gear4.rotate(opposite(how_to[i][1]))
            if gear2.right != gear3.left:
                gear3.rotate(how_to[i][1])
                if gear1.right != gear2.left:
                    gear1.rotate(how_to[i][1])
                    gear2.rotate(opposite(how_to[i][1]))
                else:
                    gear2.rotate(opposite(how_to[i][1]))
            else:
                gear3.rotate(how_to[i][1])

        elif how_to[i][0] == '4':
            # print("4 시작")
            if gear3.right != gear4.left:
                gear4.rotate(how_to[i][1])
                if gear2.right != gear3.left:
                    gear3.rotate(opposite(how_to[i][1]))
                    if gear1.right != gear2.left:
                        gear1.rotate(opposite(how_to[i][1]))
                        gear2.rotate(how_to[i][1])
                    else:
                        gear2.rotate(how_to[i][1])
                else:
                    gear3.rotate(opposite(how_to[i][1]))
            else:
                gear4.rotate(how_to[i][1])
        # print(how_to[i][1])
        # print(gear1)
        # print(gear2)
        # print(gear3)
        # print(gear4)

    if gear1.top == '1':
        score += 1
    if gear2.top == '1':
        score += 2
    if gear3.top == '1':
        score += 4
    if gear4.top == '1':
        score += 8

    print(score)


main()
