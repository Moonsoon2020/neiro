# import numpy as np
#
# # n = int(input())
# # rez = list(map(int, [input() for i in range(2 ** n)]))
# # maska = []
# # for i in range(2 ** n):
# #     bet = [int(i) for i in str(bin(i))[2:]]
# #     bet = [0] * (n - len(bet)) + bet
# #     maska.append(bet)
#
#
# def relu(x):
#     return (x > 0) * x  # returns x if x > 0
#     # return 0 otherwise
#
#
# def relu2deriv(output):
#     return output > 0  # returns 1 for input > 0
#     # return 0 otherwise
#
#
# alpha = 0.1 # * n
#
# hidden_size = 4
# streetlights = np.array( [[ 1, 0, 1 ],
#                           [ 0, 1, 1 ],
#                           [ 0, 0, 1 ],
#                           [ 1, 1, 1 ] ] )
#
# walk_vs_stop = np.array([[ 1, 1, 0, 0]]).T
#
# weights_0_1 = 2 * np.random.random((3, hidden_size)) - 1
# weights_1_2 = 2 * np.random.random((hidden_size, 1)) - 1
#
# for iteration in range(1000):
#     layer_2_error = 0
#     for i in range(len(streetlights)):
#         layer_0 = streetlights[i:i + 1]
#         layer_1 = relu(np.dot(layer_0, weights_0_1))
#         layer_2 = np.dot(layer_1, weights_1_2)
#         layer_2_error += np.sum((layer_2 - walk_vs_stop[i:i + 1]) ** 2)
#
#         layer_2_delta = (walk_vs_stop[i:i + 1] - layer_2)
#         layer_1_delta = layer_2_delta.dot(weights_1_2.T) * relu2deriv(layer_1)
#         weights_1_2 += alpha * layer_1.T.dot(layer_2_delta)
#         weights_0_1 += alpha * layer_0.T.dot(layer_1_delta)
#         print(alpha * layer_1.T.dot(layer_2_delta))
#         print(alpha * layer_0.T.dot(layer_1_delta))
#
#     print("Error:" + str(layer_2_error))
#
# print(weights_0_1, weights_1_2)
# print(maska)
# print(rez)
# for i in range(int(input())):
#     a = list(map(int, input().split()))
#     layer_1 = relu(np.dot(a, weights_0_1))
#     layer_2 = np.dot(layer_1, weights_1_2)
#     print(round(layer_2[0]), layer_2)
# # это решение не работает, поскольку формула имеет логический вид, но при домножении на коэффиценты она не сможет измениться
import numpy as np


def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))
# ввод количества битовых симоволов от 0 до 10 включительно
n = int(input())
rez = list(map(lambda x: [int(x)], [input() for i in range(2 ** n)]))   # ввод значений при разных функциях тип при 0
# 0 одно, при 0 1 другое или тоже системе пофиг
# Пример ввода:
# 2
# 0
# 1
# 1
# 0
# тип для 0 0 -> 0; 0 1 -> 1; 1 0 -> 1; 1 1 -> 0
maska = []
for i in range(2 ** n): #
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (n - len(bet)) + bet
    maska.append(bet)
X = np.array(maska)
y = np.array(rez)
hidses = 2 ** n
vvod = n
alfa = 0.5
# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((vvod, hidses)) - 1
syn1 = 2 * np.random.random((hidses, 1)) - 1
maink = [np.array([[1000]] * hidses), 0, 0]

for j in range(60000):

    # проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # как сильно мы ошиблись относительно нужной величины
    l2_error = y - l2

    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l2_error))))
    if sum(l2_error) < sum(maink[0]):
        maink = [l2_error, syn0, syn1]

    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l1_error = l2_delta.dot(syn1.T)

    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn1 += l1.T.dot(l2_delta) * alfa
    syn0 += l0.T.dot(l1_delta) * alfa
maska = []

syn0 = maink[1]
syn1 = maink[2]
print(syn0)
print(syn1)
print(sum(abs(maink[0])) / 4)
# тут малясь системного вывода, а следом вывод всего и коэффициенты уверенности
for i in range(2 ** vvod):
    bet = [int(i) for i in str(bin(i))[2:]]
    bet = [0] * (vvod - len(bet)) + bet
    l0 = bet
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    print(round(l2[0]), l2[0], l0)