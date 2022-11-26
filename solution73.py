n, u = map(int, input().split())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
w = {}
libs = {}
facrez = 0
bsum = sum(b) / n
b1 = list(map(lambda alfa: bsum - alfa, b))
sumbx = sum(map(lambda o: o ** 2, b1)) ** 0.5
for i in range(len(x)):
    if x[i] in libs.keys():
        libs[x[i]].append(i)
    else:
        libs[x[i]] = [i]
for q, k in libs.items():
    asum = len(k) / n
    a1 = [asum] * n
    ax = asum ** 2 * n
    for i in k:
        a1[i] -= 1
        ax -= asum ** 2
        ax += (asum - 1) ** 2
    if ax == 0:
        w[q] = 0
    else:
        ab = sum(map(lambda c: c[0] * c[1], zip(a1, b1)))
        w[q] = ab / ((ax ** 0.5) * sumbx)
        facrez += w[q] * len(k)
print(facrez / n)
