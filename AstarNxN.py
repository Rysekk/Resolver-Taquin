import math
import random
import time
import bisect


### UN DELTA DE 1 DONNE LE MEILLEUR CHEMIN ###
### UN DELTA DE 2 RETOURNE UN CHEMIN MOINS OPTI MAIS BIEN PLUS RAPIDEMENT ###
weight = 1
trou = 0
taquin = [8,5,1,7,0,3,2,4,6]
frontiere = []
explorer = []
goal_state = []
n = math.sqrt(len(taquin))
n = int(n)
for s in range(0, n * n):
    goal_state.append(s)

def legalMoove(tab):  # renvoi une liste de mouvements possible en fonction de la position du trou
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

def desordre(list):  # h2
    count = len(list)
    for s in range(0, len(list)):
        if s == list[s]:
            count -= 1
    return count

def manhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i, item in enumerate(initial_config):
        prev_row, prev_col = int(i / n), i % n
        goal_row, goal_col = int(item / n), item % n
        manDict += abs(prev_row - goal_row) + abs(prev_col - goal_col)
    return manDict

class noeud:
    mouvement = []
    def __init__(self, list, mouv, prec, pere, generation):
        self.tab = list
        self.pere = pere
        self.prec = prec
        self.mouvement = mouv
        self.generation = generation + 1
        self.des = desordre(self.tab)
        self.man = manhattan(self.tab)
        self.heuristic = self.generation + (self.man * (1 + weight))

    def __lt__(self, other):
        return self.getH() < other.getH()

    def getH(self):
        return self.heuristic

    def getTaquin(self):
        return self.tab

    def getPere(self):
        return self.pere

    def getMouv(self):
        return self.mouvement

    def getGeneration(self):
        return self.generation

    def etatBut(self):
        if self.des == 0:
            return True
        else:
            return False

    def getPere(self):
        return self.pere

    def expend(self):
        mouvementPossible = legalMoove(self.tab)
        try:
            mouvementPossible.remove(self.mouvement * -1)
        except:
            pass
        for s in range(0, len(mouvementPossible)):
            tab = self.tab.copy()
            posX = tab.index(trou)
            mouv = mouvementPossible[s]
            swapPositions(tab, posX, mouv + posX)
            nouveauNoeud = noeud(tab, mouv, self.mouvement, self, self.generation)
            if frontiere == []:
                frontiere.append(nouveauNoeud)
            else:
                idx = bisect.bisect(frontiere,nouveauNoeud)
                frontiere.insert(idx, nouveauNoeud)
        ## AJOUTER A LA LISTE DES EXPLORER ET RETIRE DE LA FRONTIERE ##
        explorer.append(self)
        if self.getGeneration() >= 1:
            frontiere.remove(self)

a = time.time()
root = noeud(taquin, [], None, None, -1)
root.expend()
while frontiere[0].etatBut() != True:
    frontiere[0].expend()
b = time.time()

### AFFICHAGE SOLUTION ###
mouvements = []
noeud = frontiere[0]
while noeud.getGeneration() != 0:
    mouvements.append(noeud.getMouv())
    noeud = noeud.getPere()
mouvements.reverse()

print("root : ", taquin)
print("but : ", goal_state)
print("Nombre de tuiles mal placé : ", desordre(noeud.getTaquin()))
print("Distance de manhattan initial : ", manhattan(noeud.getTaquin()))
print("taille : ", n, "x", n)
print("Delta : ", weight)
print("Chemin : ", mouvements)
print("Taille solution : ", len(mouvements))
print("Taille de la frontière : ", len(frontiere))
print("Nombre de noeuds visité : ", len(explorer))
print("Nombre de tuile déplacé : ", len(frontiere) + len(explorer))
print("Temps de resolution du taquin : ", b - a)
