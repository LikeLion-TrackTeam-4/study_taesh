# GCF ACDEB 처럼 입력될 때, 합이 가장 크게 만들어지기 위해서 각각의 알파벳에 0~9 를 할당하기.
# 0~9는 각각 한번씩만 사용. 즉 입력문자의 알파벳 종류는 최대 10개

# 각 입력을 알파벳 단위로 분리하여 자릿수에 따라 가중치를 계산. ex) ACBQ -> A 1000 C 100 B 10 Q 1
# 가중치가 큰 순서대로 9부터 할당. 그리고 계산.

numbers_lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

str_lists = []

cnt = int(input())
for i in range(cnt):
    str_lists.append(input())

alph_weight = {}

for i in range(cnt):
    list_var = list(str_lists[i])
    weight = 1
    while list_var:
        c = list_var.pop()
        if c not in alph_weight:
            alph_weight[c] = weight
        else:
            alph_weight[c] = alph_weight[c] + weight
        weight = weight * 10

changer = {}
for i in sorted(alph_weight.items(), key=lambda x: x[1], reverse=True):
    changer[i[0]] = numbers_lists.pop()

nums_for_sum = []
for i in str_lists:
    for j in i:
        i = i.replace(j, str(changer[j]))
    nums_for_sum.append(int(i))

print(sum(nums_for_sum))