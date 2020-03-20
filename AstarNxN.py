import random
import math

trou = 9

taquin = [2,9,6,
          3,7,8,
          1,4,5]

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

def sommeDist(list): #h1
    somme = 0
    for s in range(0,len(list)):
        somme += distOrigine(list[s])
    return somme

frontiere = []
explorer = []

class noeud:
    mouvement = []
    def __init__(self, list , mouv, pere, generation):
        self.tab = list
        self.pere = pere
        self.mouvement = mouv
        self.generation = generation+1
        self.heuristic = desordre(self.tab) + self.generation + inversion(self.tab)
    def __repr__(self):
        print(str(self.h()))
    def getH(self):
        return self.heuristic
    def getTaquin(self):
        return self.tab
    def getPere(self):
        return  self.pere
    def getMouv(self):
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
            nouveauNoeud = noeud(tab, mouv, self, self.generation)
            if frontiere == []:
                frontiere.append(nouveauNoeud)
            else:
                x = False
                for s in range(0,len(frontiere)):
                    if frontiere[s].getH() >= nouveauNoeud.getH():
                        frontiere.insert(s,nouveauNoeud)
                        x = True
                        break
                if x == False:
                    frontiere.append(nouveauNoeud)



        if self.getGeneration() >= 1:
            frontiere.remove(self)

    def etatBut(self):
        if desordre(self.tab) == 0:
            return True
        else:
            False
    def getPere(self):
        return self.pere

root = noeud(taquin,[], None, -1)
root.expend()

print("root : ",root.getTaquin())

while frontiere[0].etatBut() != True:
    frontiere[0].expend()

mouvements = []
noeud = frontiere[0]
while noeud.getGeneration() != 1:
    mouvements.append(noeud.getPere().getMouv())
    noeud = noeud.getPere()

print()
mouvements.reverse()
print(mouvements)
