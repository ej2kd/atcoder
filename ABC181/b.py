"""
B - Trapezoid Sum
https://atcoder.jp/contests/abc181/tasks/abc181_b
args: int
return: sum of ints
"""

N = int(input())
lst = [list(map(int, input().split())) for lst in range(N)]
result = 0
for i in range(len(lst)):
    result += int((len(range(lst[i][0], lst[i][1]+1)) * (lst[i][0] + lst[i][1])) / 2)
print(result)