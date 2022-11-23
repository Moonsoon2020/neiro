# -*- coding: utf-8 -*-
import math
import random

def dot1(first, second):
    a = []
    for j in range(len(first[0])):
        b = []
        for i in first:
            b.append(i[j])
        a.append(b)
    first = a
    a = []

    for i in range(len(first)):
        c = []
        for f in range(len(second)):
            b = []
            k = 0
            for j in second:
                b.append(second[k][f] * first[i][k])
                k += 1
            c.append(sum(b))
        a.append(c)
    return a

def persi(first, second):
    b = []
    for i in range(len(first)):
        a = []
        for j in range(len(first[0])):
            a.append(first[i][j] * second[i][j])
        b.append(a)
    return b

def dot(first, second):
    a = []
    for i in first:
        d = []
        for q, v in list(zip(i, second)):
            d.append([q * g for g in v])
        a.append([sum(h) for h in zip(*d)])
    return a


def nonlinmy(x, deriv=False):
    if (deriv == True):
        return [[f * (1 - f) for f in pp] for pp in x]
    return [[1 / (math.exp(-f) + 1) for f in pp] for pp in x]


n = int(input())
rez = []
for i in range(2 ** n):
    rez.append([int(input())])
# ввод значений при разных функциях тип при 0
# 0 одно, при 0 1 другое или тоже системе пофиг
# Пример ввода:
# 2
# 0
# 1
# 1
# 0
# тип для 0 0 -> 0; 0 1 -> 1; 1 0 -> 1; 1 1 -> 0
maska = []
for i in range(2 ** n):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (n - len(bet)) + bet
    maska.append(bet)
x = maska
y = rez
hidses = 2 ** n
vvod = n
alfa = 0.5
# случайно инициализируем веса, в среднем - 0
mysyn0 = [[2 * random.random() - 1 for j in range(hidses)] for i in range(vvod)]
mysyn1 = [[2 * random.random() - 1] for i in range(hidses)]

for j in range(6000):

    # проходим вперёд по слоям 0, 1 и 2
    myl0 = x
    myl1 = nonlinmy(dot(myl0, mysyn0))
    myl2 = nonlinmy(dot(myl1, mysyn1))
    # как сильно мы ошиблись относительно нужной величины
    l2_error_my = [[y[i][0] - myl2[i][0]] for i in range(len(myl2))]
    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta_my = dot(l2_error_my, nonlinmy(myl2, deriv=True))
    # как сильно значения l1 влияют на ошибки в l2?
    l1_error_my = dot(l2_delta_my, [[i[0] for i in mysyn1]])
    l1_delta_my = persi(l1_error_my, nonlinmy(myl1, deriv=True))
    mysyn1 = [[round(i[0] + j[0], 7)] for i, j in list(zip(mysyn1, dot(myl1, [[alfa * i[0]] for i in l2_delta_my])))]
    mysyn0 = [[i + j * alfa for i, j in list(zip(mysyn0[k], dot1(myl0, l1_delta_my)[k]))] for k in range(len(mysyn0))]
# тут малясь системного вывода, а следом вывод всего и коэффициенты уверенности
for i in range(2 ** vvod):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (vvod - len(bet)) + bet
    l0 = bet
    myl0 = bet
    myl1 = nonlinmy(dot([myl0], mysyn0))
    myl2 = nonlinmy(dot(myl1, mysyn1))
    print(round(myl2[0][0]), myl2[0][0])
print(mysyn0)
print(mysyn1)