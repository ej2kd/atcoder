"""
A x B + C
https://atcoder.jp/contests/abc179/tasks/abc179_c
"""

N = int(input())
cnt = 0

for a in range(1, N):
    cnt += int((N - 1) / a)

print(cnt)