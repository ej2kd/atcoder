"""
B: Play Snuke
args: ints
return: int(-1 if false)
"""

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

result = []
for i in range(len(lst)):
    Ai = lst[i][0]
    Pi = lst[i][1]
    Xi = lst[i][2]
    if (Ai >= Xi):
        result.append(-1)
    else:
        result.append(Pi)

if max(result) > 0:
    print(min([i for i in result if i > 0]))
else:
    print(-1)