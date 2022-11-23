n, k = map(int, input().split())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
# n, k = 10 ** 4 - 2, 1
# x = '1' * (10 ** 4-3) + '2'
# b = [*range(1, 10**4)]
w = {}
libs = {}
facrez = 0
bsum = sum(b) / len(b)
b1 = list(map(lambda alfa: bsum - alfa, b))
bx = [i ** 2 for i in b1]
sumbx = sum(bx)
for k in x:
    if k in w.keys():
        facrez += w[k]
    else:
        a = [1 if i == k else 0 for i in x]
        asum = sum(a) / len(a)
        a1 = list(map(lambda alfa: asum - alfa, a))
        ax = []
        for i in a1:
            ax.append(i ** 2)
        ab = [i * j for i, j in zip(a1, b1)]
        rez = sum(ab) / ((sum(ax) * sumbx) ** 0.5)
        w[k] = rez
        facrez += rez
print(facrez / n)