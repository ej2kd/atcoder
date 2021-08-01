# atcoder

# 標準入力
## 1行1列

```python
# str
s = input()
# int
s = int(input())
```

## 1行n列

```python
# str
s1, s2 = input().split()
# int
x, y, z = map(int, input().split())
```

## n行m列

```python
# int
lst = list(map(int, input().split()))
# ソートして格納
sorted_lst = sorted(list(map(int, input().split())))
# 2次元配列として格納
N = int(input())
lst = [list(map(int, input().split())) for lst in range(N)]
# 別のリストとして格納
Input:
N
x1 x2 x3 ... x4
y1 y2 y3 ... y4

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

Input:
N
a1 b1
a2 b2
...
an bn

N = int(input())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*ab)]
```
