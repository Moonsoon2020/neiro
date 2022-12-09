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
    for i in range(len(second)):
        b.append(first[i] * second[i])
    return b

def dot2(first, second):
    b = []
    for i in range(len(second)):
        b.append(first * second[i])
    return b

def dot(first, second):
    a = []
    for i in range(len(second[0])):
        b = []
        for j in range(len(second)):
            b.append(first[i] * second[j][i])
        a.append(sum(b))
    return a


def nonlinmy(x, deriv=False):
    a = []
    if (deriv == True):
        return [f * (1 - f) for f in x]
    for f in x:
        if 1000 > abs(f) > 0:
            a.append(1 / (math.exp(-f) + 1))
        else:
            a.append(0)
    return a


n = int(input())
rez = []
for i in range(2 ** n):
    rez.append(int(input()))
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
    maska.append(bet + [1])
x = maska
y = rez
hidses = 2 ** n
vvod = n
alfa = 0.1
# случайно инициализируем веса, в среднем - 0
mysyn0 = [[2 * random.random() - 1 for i in range(vvod + 1)] for j in range(vvod)]
mysyn1 = [2 * random.random() - 1 for i in range(vvod + 1)]
my_error = 100
vs1 = 0
vs0 = 0
for j in range(6000):
    error = 0
    l2_delta_my = 0
    l1_delta_my = [0] * (vvod + 1)
    for i in range(len(x)):
        # проходим вперёд по слоям 0, 1 и 2
        myl0 = x[i]
        myl1 = nonlinmy(dot(myl0, mysyn0))
        myl2 = sum(nonlinmy(persi(myl1, mysyn1)))
        # как сильно мы ошиблись относительно нужной величины
        l2_error_my = myl2 - y[i]
        error += abs(l2_error_my)
        # в какую сторону нужно двигаться?
        # если мы были уверены в предсказании, то сильно менять его не надо
        l2_delta_my += l2_error_my * (myl2 * (1-myl2))
        # как сильно значения l1 влияют на ошибки в l2?
        l1_error_my = dot2(l2_delta_my, mysyn1)
        l1_delta_my = [i[0] + i[1] for i in list(zip(l1_delta_my, persi(l1_error_my, nonlinmy(myl1, deriv=True))))]
    if error < my_error:
        my_error = error
        vs0 = mysyn0
        vs1 = mysyn1
    mysyn1 = [i + l2_delta_my * alfa for i in mysyn1]
    mysyn0 = [[i[j] + l1_delta_my[j] * alfa for j in range(len(l1_delta_my))] for i in mysyn0]
    print(l1_delta_my)
    print(l2_delta_my)

# тут малясь системного вывода, а следом вывод всего и коэффициенты уверенности
mysyn0 = vs0
mysyn1 = vs1
print(mysyn1)
print(mysyn0)
for i in range(2 ** vvod):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (vvod - len(bet)) + bet
    l0 = bet
    myl0 = bet + [1]
    myl1 = [1 if i > 0 else 0 for i in nonlinmy(dot(myl0, mysyn0))]
    myl2 = 1 if sum(nonlinmy(persi(myl1, mysyn1))) > 0 else 0
    print(round(myl2), myl2)
print(2)
for i in range(2 ** vvod):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (vvod - len(bet)) + bet
    l0 = bet
    myl0 = bet + [1]
    myl1 = nonlinmy(dot(myl0, mysyn0))
    myl2 = sum(nonlinmy(persi(myl1, mysyn1)))
    print(round(myl2), myl2)