w, b = input().split()
w, b = int(w), float(b)

# w, b = map(int, input().split())

if w % 5 == 0 and b >= w + 0.5:
    print('{0:.2f}'.format(b - w - 0.5))
else:
    print('{0:.2f}'.format(b))