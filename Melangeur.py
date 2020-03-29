import random
import math

taquin = []
n = 3
nbShuffle = 1000
trou = 0

for s in range(0,n*n):
    taquin.append(s)

def legalMoove(tab): # renvoi une liste de mouvements possible en fonction de la position du trou
    index = tab.index(trou)
    if index == 0:  # coin haut gauche
        return [1, n]
    if index == (n - 1):  # coin haut droit
        return [-1, n]
    if index == ((n * n) - 1) - (n - 1):  # coin bas gauche
        return [-n, 1]
    if index == (n * n) - 1:  # coin bas droit
        return [-n, -1]
    if 0 < index < (n - 1):  # bordure haute
        return [-1, n, 1]
    if ((n * n) - 1) - (n - 1) < index < (n * n) - 1:  # bordure basse
        return [-n, -1, 1]
    if index % n == 0:  # bordure gauche
        return [-n, 1, n]
    if index % n == (n - 1):  # bordure droite
        return [-n, -1, n]
    else:  # centre
        return [-n, -1, 1, n]

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def rand(list):
    for s in range(0,nbShuffle):
        posX = list.index(trou)
        mouvPoss = legalMoove(list)
        mouv = random.choice(mouvPoss)
        swapPositions(taquin,posX, mouv + posX)

rand(taquin)
print(taquin)
