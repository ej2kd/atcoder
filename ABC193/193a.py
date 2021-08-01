"""
A: Discount
args: strings
return: float
"""

A, B = map(int, input().split())
print(100 * (1 - (B / A)))