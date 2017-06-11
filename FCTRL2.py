t = int(input())
factorials = []
for i in range(t):
    x = 1
    n = int(input())
    for j in range(n):
        j += 1
        x *= j
    factorials.append(x)
for f in factorials:
    print(f)
