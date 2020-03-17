import random
import math

trou = 9

taquin = [1,2,3,
          4,5,6,
          9,7,8]

taquinTampon = taquin.copy()

nbSwap = 0
mouvementPrecedent = 0
taillePlusCourt = 10000000

cheminActuel = []
meilleurChemin = []

n = math.sqrt(len(taquin))
profondeurRecherche = 30



def legalMoove(tab):
    index = tab.index(trou)
    if index == 0:  # coin haut gauche
        return [1, 3]
    if index == (n - 1):  # coin haut droit
        return [-1, 3]
    if index == ((n * n) - 1) - (n - 1):  # coin bas gauche
        return [-3, 1]
    if index == (n * n) - 1:  # coin bas droit
        return [-3, -1]
    if 0 < index < (n - 1):  # bordure haute
        return [-1, 3, 1]
    if ((n * n) - 1) - (n - 1) < index < (n * n) - 1:  # bordure basse
        return [-3, -1, 1]
    if index % n == 0:  # bordure gauche
        return [-3, 1, 3]
    if index % n == (n - 1):  # bordure droite
        return [-3, -1, 3]
    else:  # centre
        return [-3, -1, 1, 3]

def choixMouvement(list):
    return random.choice(list)

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def nombreElemOk(list):
    count = 0
    for s in range(0, len(list)):
        if s+1 == list[s]:
            count += 1
    return count

def SommeDist(list):
    somme = 0
    for s in range(0,len(list)):
        somme += distOrigine(list[s])
    return somme

def testSucc(list, mouv):
    tab = list.copy()
    posX = tab.index(trou)
    print(tab)
    swapPositions(tab, posX, mouv + posX)
    print(tab)
    return SommeDist(tab)

def distOrigine(nb):
    target = (nb - 1)
    pos = taquin.index(nb)
    dist = 0
    if pos == target:
        return dist
    elif pos < target:
        while target - 3 > pos:
            dist += 1
            target -= 3
        dist += abs(pos - target)
        return dist
    elif pos > target:
        while pos - 3 > target:
            dist += 1
            pos -= 3
        dist += abs(pos - target)
        return dist

print("taquin : ",taquin)
print("nombre elem ok : ",nombreElemOk(taquin))
print("trou : ", trou)
print("position trou : ", taquin.index(trou))
print("taille : ", n)
print("taille max recherche : ",profondeurRecherche)
print(legalMoove(taquin))

print(testSucc(taquin,legalMoove(taquin)[0]))
print(testSucc(taquin,legalMoove(taquin)[1]))



for s in range(0, 700000):

    while nombreElemOk(taquin) != len(taquin):

        posX = taquin.index(trou)
        mouvementPossible = legalMoove(taquin)

        if nbSwap == 0:
            mouvementChoisi = choixMouvement(mouvementPossible)
        elif nbSwap > 0:
            mouvementPossible.remove(mouvementPrecedent * -1)
            mouvementChoisi = choixMouvement(mouvementPossible)

        mouvementPrecedent = mouvementChoisi
        cheminActuel.append(mouvementChoisi)
        posElementChoisi = posX + mouvementChoisi
        swapPositions(taquin, posX, posElementChoisi)
        nbSwap += 1

        if nbSwap > taillePlusCourt:
            break
        if nbSwap > profondeurRecherche:
            break

    if (nbSwap < taillePlusCourt) & (nbSwap != profondeurRecherche + 1):
        print(cheminActuel)
        print("taille :", nbSwap)
        print("nombre d'essai pour solution : ", s)
        taillePlusCourt = nbSwap
        meilleurChemin = []
        meilleurChemin = cheminActuel.copy()
    else:
        cheminActuel = []

    nbSwap = 0
    taquin = taquinTampon.copy()

