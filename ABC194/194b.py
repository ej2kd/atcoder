n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
sums = []

for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            sums.append(lst[i][0] + lst[j][1])
        else:
            sums.append(max(lst[i][0], lst[j][1]))

print(min(sums))