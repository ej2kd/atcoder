"""
C: Unexpressed
args: int
return: int
"""

N = int(input())
nums = range(1, N+1)
lst = []
upper = int(N ** (1/2))

memo = {}

for a in range(2, upper+1):
    b = 2
    while a ** b <= N:
        x = a ** b
        if (x not in memo) and (x in nums):
            lst.append(x)
            memo[x] = x
        b += 1

print(len(nums) - len(lst))