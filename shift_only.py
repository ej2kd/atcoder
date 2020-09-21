# n = int(input())
# a = list(map(int, input().split()))
# count = 0

# while all(i % 2 == 0 for i in a):
#     a = [i / 2 for i in a]
#     count += 1
# print(count)

n = int(input())
nums = [int(i) for i in input().split()]
cnt = 0
 
while True:
    if [i for i in nums if i % 2]:
        break
    nums = [i // 2 for i in nums]
    cnt += 1
 
print(cnt)
