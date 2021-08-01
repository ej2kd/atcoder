N = int(input())
a_list = list(map(int, input().split()))
count = [0 for _ in range(401)]

for a in a_list:
    count[a + 200] += 1

ans = 0

for i in range(401):
    for j in range(i, 401):
        ans += count[i] * count[j] * (abs((i - 200) - (j - 200))) ** 2

print(ans)