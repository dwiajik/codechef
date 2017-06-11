t = int(input())

z = []
for i in range(t):
    n = int(input())
    zeros = 0
    for j in range(15):
        j += 1
        zeros += int(n / int(5 ** j))
    z.append(zeros)

for i in z:
    print(i)