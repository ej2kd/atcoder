n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

result = max(max(a), max(b))

x = 0
y = 0

while x < n and y < m:
    result = min(result, abs(a[x] - b[y]))
    if (a[x] > b[y]):
        y += 1
    else:
        x += 1

print(result)
