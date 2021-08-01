"""
B - Billiards
https://atcoder.jp/contests/abc183/tasks/abc183_b
args: 4 ints
return: int
"""

sx, sy, gx, gy = map(float, input().split())
print((sx * gy + gx * sy) / (sy + gy))