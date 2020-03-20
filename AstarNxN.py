import random
import math

trou = 9

taquin = [1,2,3,
          4,5,6,
          9,7,8]

n = math.sqrt(len(taquin))

def legalMoove(tab): # renvoi une liste de mouvements possible en fonction de la position du trou
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

def choixMouvement(list): # choix meilleurs mouvement
    plusCourt = testSucc(taquin,list[0])
    meilleurMouv = list[0]
    for s in range(0,len(list)):
        if testSucc(taquin,list[s]) < plusCourt:
            meilleurMouv = list[s]
            plusCourt = testSucc(taquin,list[s])
    return meilleurMouv

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def inversion(list):
    sum = 0
    for s in range(0,len(list)):
        for i in range(s+1,len(list)):
            if list[s] > list[i]:
                if list[s] != 9:
                    sum += 1
    return sum

def desordre(list): #h2
    count = len(taquin)
    for s in range(0, len(list)):
        if s+1 == list[s]:
            count -= 1
    return count

def distOrigine(nb):
    target = (nb - 1)
    pos = taquin.index(nb)
    dist = 0
    if pos == target:
        return dist
    elif pos < target:
        while target - 3 >= pos:
            dist += 1
            target -= 3
        dist += abs(pos - target)
        return dist
    elif pos > target:
        while pos - 3 >= target:
            dist += 1
            pos -= 3
        dist += abs(pos - target)
        return dist

def SommeDist(list): #h1
    somme = 0
    for s in range(0,len(list)):
        somme += distOrigine(list[s])
    return somme

def testSucc(list, mouv): #test h1 + h2
    tab = list.copy()
    posX = tab.index(trou)
    swapPositions(tab, posX, mouv + posX)
    return SommeDist(tab) + nombreElemOk(tab) + inversion(tab)

class arbre:

    def __init__(self):
        self.nbSwap = 0
        self.frontiere = []

frontiere = []
explorer = []

class noeud:
    mouvement = []
    def __init__(self, list, nbSwap , mouv, pere, generation):
        self.tab = list
        self.nb = nbSwap
        self.pere = pere
        self.mouvement = mouv
        self.generation = generation+1
        self.heuristic = desordre(self.tab) + self.nb + self.generation
    def __repr__(self):
        print(str(self.h()))
    def h(self):
        return self.heuristic
    def taquin(self):
        return self.tab
    def mouv(self):
        return self.mouvement
    def getGeneration(self):
        return self.generation
    def expend(self):
        mouvementPossible = legalMoove(self.tab)
        for s in range(0, len(mouvementPossible)):
            tab = self.tab.copy()
            posX = tab.index(trou)
            mouv = mouvementPossible[s]
            swapPositions(tab, posX, mouv + posX)
            nouveauNoeud = noeud(tab, nbSwap, mouv, self, self.generation)
            if frontiere == []:
                frontiere.append(nouveauNoeud)
            else:
                for s in range(0,len(frontiere)):
                    if frontiere[s].h() >= nouveauNoeud.h():
                        frontiere.insert(s,nouveauNoeud)
                        break
        explorer.append(self)
        if self.generation >= 1:
            frontiere.remove(self)

    def etatBut(self):
        if desordre(self.tab) == 0:
            return True
        else:
            False
    def getPere(self):
        return self.pere


nbSwap = 0
root = noeud(taquin,nbSwap,[], None, -1)
root.expend()
print("racine : ", root.taquin(), " heuristique : ", root.h(), " gen :", root.getGeneration())
print()
for s in range(0,len(frontiere)):
    print("frontière : ",frontiere[s].taquin(), " heuristique : ", frontiere[s].h(), " gen :" , frontiere[s].getGeneration())

frontiere[0].expend()

print()
for s in range(0,len(frontiere)):
    print("frontière : ", frontiere[s].taquin(), " heuristique : ", frontiere[s].h(), " gen : ", frontiere[s].getGeneration())

print()
for s in range(0,len(explorer)):
    print("explorée : ",explorer[s].taquin(), " heuristique : ", explorer[s].h(), " gen : ", explorer[s].getGeneration())
