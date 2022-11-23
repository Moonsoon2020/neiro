n, k = map(int, input().split())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
w = {}
facrez = 0
for k in x:
    p = [1 if i == k else 0 for i in x]
    z = ''.join(map(str, p))
    if z in w.keys():
        facrez += w[z]
    else:
        a = p
        asum = sum(a) / len(a)
        bsum = sum(b) / len(b)
        a1 = list(map(lambda alfa: asum - alfa, a))
        b1 = list(map(lambda alfa: bsum - alfa, b))
        ax = []
        for i in a1:
            ax.append(i ** 2)
        bx = []
        for i in b1:
            bx.append(i ** 2)
        ab = [i * j for i, j in zip(a1, b1)]
        rez = sum(ab) / ((sum(ax) * sum(bx)) ** 0.5)
        w[z] = rez
        facrez += rez
print(facrez / n)