n, k = map(int, input().split())

divisible = 0

for i in range(n):
    t = int(input())
    if t % k == 0:
        divisible += 1

print(divisible)