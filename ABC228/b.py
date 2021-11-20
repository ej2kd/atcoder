n, x = map(int, input().split())
a = list(map(int, input().split()))

known = set()
i = x
while i not in known:
    known.add(i)
    i = a[i - 1]

print(len(known))
