n, u = map(int, input().split())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
# n, u = 10 ** 4 - 2, 10**4 - 2
# x = [*range(1, 10**4)]
# b = [*range(1, 10**4)]
w = {}
facrez = 0
bsum = sum(b) / n
b1 = list(map(lambda alfa: bsum - alfa, b))
sumbx = sum(map(lambda i: i ** 2, b1))
for k in set(x):
    asum = x.count(k) / n
    a1 = list(map(lambda i: asum - int(i == k), x))
    ax = sum(map(lambda i: i ** 2, a1))
    ab = sum(map(lambda i: i[0] * i[1], zip(a1, b1)))
    if ab == 0 or ax == 0:
        w[k] = 0
    else:
        w[k] = ab / ((ax * sumbx) ** 0.5)
    # print(k)
for k in x:
    facrez += w[k]
print(facrez / n)
