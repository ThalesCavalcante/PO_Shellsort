import timeit
from random import randint
import matplotlib.pyplot as plt
import sys
from random import shuffle

sys.setrecursionlimit(10 ** 6)


def desenhaGrafico(x, y, xl="Entradas", yl="Saidas", name="out"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)


def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


size = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for s in size:
    lista = geraLista(s)
    time.append(timeit.timeit("shellSort({})".format(lista),
                              setup="from __main__ import shellSort", number=1))
    print(s)

desenhaGrafico(size, time, "Tamanho", "Tempo",
               "ShellSort.png")