n = int(input())
s1, s2, max_lead = 0, 0, (1, 0)
for i in range(n):
    p1, p2 = map(int, input().split())
    s1 += p1
    s2 += p2
    if (s1 > s2) and s1 - s2 > max_lead[1]:
        max_lead = (1, s1 - s2)
    elif (s2 > s1) and s2 - s1 > max_lead[1]:
        max_lead = (2, s2 - s1)
print('{} {}'.format(max_lead[0], max_lead[1]))