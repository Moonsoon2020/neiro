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
        b.append(first * second[i])
    return b

def dot(first, second):
    a = []
    for i in range(len(second)):
        a.append(first[i] * second[i])
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
for i in range(2 ** (n - 1)):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (n - len(bet)) + bet
    maska.append(bet + [1])
x = maska
y = rez
hidses = 2 ** n
vvod = n
alfa = 0.05
# случайно инициализируем веса, в среднем - 0
mysyn0 = [2 * random.random() - 1 for i in range(vvod + 1)]
mysyn1 = [2 * random.random() - 1 for i in range(vvod + 1)]
itv = [10000, mysyn0, mysyn1]
for j in range(6000):
    error = 10000
    for i in range(len(x)):
        # проходим вперёд по слоям 0, 1 и 2
        myl0 = x[i]
        myl1 = nonlinmy(dot(myl0, mysyn0))
        myl2 = sum(nonlinmy(dot(myl1, mysyn1)))
        # как сильно мы ошиблись относительно нужной величины
        l2_error_my = myl2 - y[i]

        # в какую сторону нужно двигаться?
        # если мы были уверены в предсказании, то сильно менять его не надо
        l2_delta_my = l2_error_my * (myl2 * (1-myl2))
        # как сильно значения l1 влияют на ошибки в l2?
        l1_error_my = persi(l2_delta_my, mysyn1)
        l1_delta_my = dot(l1_error_my, nonlinmy(myl1, deriv=True))
        mysyn1 = [i + l2_delta_my * alfa for i in mysyn1]
        mysyn0 = [i + j * alfa for i, j in zip(mysyn0, l1_delta_my)]
        print(mysyn1)
        print(mysyn0)
    if itv[0] > error:
        itv = [error, mysyn0, mysyn1]

# тут малясь системного вывода, а следом вывод всего и коэффициенты уверенности
mysyn0 = itv[1]
mysyn1 = itv[2]
for i in range(2 ** vvod):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (vvod - len(bet)) + bet
    l0 = bet
    myl0 = bet + [1]
    myl1 = nonlinmy(dot(myl0, mysyn0))
    myl2 = sum(nonlinmy(dot(myl1, mysyn1)))
    print(round(myl2), myl2)
print(2)
