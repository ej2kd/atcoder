n = int(input())
A = list(map(int, input().split()))

s = 0
sq = 0

for i in A:
    s += i
    sq += i ** 2
print(n * sq - s ** 2)