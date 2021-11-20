s, t, x = map(int, input().split())

if s <= t and s <= x < t:
    print("Yes")
elif s > t and (s <= x <= 23 or 0 <= x < t):
    print("Yes")
else:
    print("No")