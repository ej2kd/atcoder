n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

total_score = [sum(p[i]) for i in range(len(p))]
sorted_lst = sorted(total_score, reverse=True)

for i in range(len(total_score)):
    if total_score[i] + 300 < sorted_lst[k-1]:
        print("No")
    else:
        print("Yes")
