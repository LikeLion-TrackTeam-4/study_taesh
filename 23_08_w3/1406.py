class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


text = input()
head = Node(None)
cursor = Node('^')
cursor.left = head
head.right = cursor
exNode = head

for c in text:
    newNode = Node(c)
    newNode.left = exNode
    newNode.right = cursor
    exNode.right = newNode
    exNode = newNode
    cursor.left = newNode

ord_n = int(input())

for i in range(ord_n):
    # 명령어 입력받아서 구분해서 실행하기
    ord = input()
    ords = ord.split()
    if ords[0] == 'L':
        if cursor.left.left.value is None:
            continue
        if cursor.right is None:
            print("@@!#@!#")
            node1 = cursor.left.left
            node2 = cursor.left
            node1.right = cursor
            cursor.left = node1
            cursor.right = node2
            node2.left = cursor
            node2.right = None
            continue
        node1 = cursor.left.left
        node2 = cursor.left
        node3 = cursor.right
        node1.right = cursor
        node2.left = cursor
        node2.right = node3
        node3.left = node2
        cursor.left = node1
        cursor.right = node2
    elif ords[0] == 'D':
        if cursor.right is None:
            continue
        # head 때문에 왼쪽이 없을일 없음.
        if cursor.right.right is None:
            node1 = cursor.left
            node2 = cursor.right
            node1.right = node2
            node2.left = node1
            node2.right = cursor
            cursor.left = node2
            cursor.right = None
            continue
        node1 = cursor.left
        node2 = cursor.right
        node3 = cursor.right.right
        node1.right = node2
        node2.left = node1
        node2.right = cursor
        node3.left = cursor
        cursor.left = node2
        cursor.right = node3
    elif ords[0] == 'B':
        if cursor.left.left.value is None:
            continue
        node1 = cursor.left.left
        node1.right = cursor
        cursor.left = node1
    elif ords[0] == 'P':
        newNode = Node(ords[1])
        node1 = cursor.left
        newNode.left = node1
        newNode.right = cursor
        node1.right = newNode
        cursor.left = newNode
    print(cursor.left.value)
asd = head.right

while asd.right is not None:
    print(asd.value, end='')
    asd = asd.right
