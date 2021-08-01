"""
C - Collinearity
https://atcoder.jp/contests/abc181/tasks/abc181_c
args: int
return: string('Yes' or 'No')
"""

N = int(input())
p = [list(map(int, input().split())) for p in range(N)]

result = 'No'

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a = p[i]
            b = p[j]
            c = p[k]
            x1 = b[0] - a[0]
            y1 = b[1] - a[1]
            x2 = c[0] - b[0]
            y2 = c[1] - b[1]
            if y2 * x1 == y1 * x2:
                result = 'Yes'
print(result)
