"""
A - Heavy Rotation
https://atcoder.jp/contests/abc181/tasks/abc181_a
args: int
return: string('White' or 'Black')
"""

N = int(input())
print('Black') if N % 2 else print('White')