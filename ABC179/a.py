"""
A - Plural Form
https://atcoder.jp/contests/abc179/tasks/abc179_a
"""

S = input()
print(S + 'es' if S[-1] == 's' else S + 's')