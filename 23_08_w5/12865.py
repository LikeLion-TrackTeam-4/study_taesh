import copy
from typing import List

def main():
    n, k = input().split()
    n, k = int(n), int(k)

    object_list = []
    for i in range(n):
        v, w = input().split()
        v, w = int(v), int(w)
        object_list.append([v, w])

    # for i in range(n):
    #     object_list[i].append(object_list[i][1] / object_list[i][0])

    print(object_list)

    for i in range(n):
        # copy_list = copy.deepcopy(object_list)
        # copy_list.pop(i)
        # weight = k
        # weight = weight - object_list[i][0]
        #
        # print(copy_list, weight)
        # less_list = []
        # for j in copy_list:
        #     if j[0] <= weight:
        #         less_list.append(j)
        # # if less_list:
        ...

def dp(lists: List, weight: int):
    new_list = []
    for i in lists:
        if i[0] <= weight:
            new_list.append(i)
