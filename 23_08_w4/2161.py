# (7) 1 2 3 4 5 6 7
# 1 - 345672
# 3 - 56724
# 5 - 7246
# 7 - 462
# 4 - 26
# 2 - 6

num = int(input())
num_list = []
for i in range(num):
    num_list.append(i+1)

while len(num_list) > 1:
    print(num_list.pop(0), end=" ")
    num_list.append(num_list.pop(0))

print(num_list[0])
