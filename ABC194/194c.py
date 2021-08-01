n = int(input())
A = list(map(int, input().split()))
result = 0

lst_1 = list(range(1, n))
for i in lst_1:
    lst_2 = list(range(i))
    for j in lst_2:
        result += (A[i] - A[j]) ** 2

print(result)