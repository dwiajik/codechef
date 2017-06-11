T = int(input())
results = []
for i in range(T):
    results.append(sum(map(int, input().split())))
for result in results:
    print(result)