"""
Product Max
https://atcoder.jp/contests/abc178/tasks/abc178_b
"""

a, b, c, d = map(int, input().split())
result = [a * c, a * d, b * c, b * d]

print(max(result))