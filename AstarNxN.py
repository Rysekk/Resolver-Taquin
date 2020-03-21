import random
import math

trou = 9

taquin = [5,2,9,
          7,1,3,
          4,8,6]

frontiere = []
explorer = []

goal_state = [0,1,2,3,4,5,6,7,8]
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

def afficherTaquin(list):
    tab1 = []
    tab2 = []
    tab3 = []
    tab1.append(list[0])
    tab1.append(list[1])
    tab1.append(list[2])
    tab2.append(list[3])
    tab2.append(list[4])
    tab2.append(list[5])
    tab3.append(list[6])
    tab3.append(list[7])
    tab3.append(list[8])
    print(tab1)
    print(tab2)
    print(tab3)
    print()

def calculateManhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict

class noeud:
    mouvement = []
    def __init__(self, list , mouv, pere, generation):
        self.tab = list
        self.pere = pere
        self.mouvement = mouv
        self.generation = generation+1
        self.heuristic = desordre(self.tab) + self.generation + inversion(self.tab) + calculateManhattan(self.tab)
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
        explorer.append(self)

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

while frontiere[0].etatBut() != True:
    frontiere[0].expend()

mouvements = []
noeud = frontiere[0]
while noeud.getGeneration() != 1:
    mouvements.append(noeud.getPere().getMouv())
    afficherTaquin(noeud.getTaquin())
    noeud = noeud.getPere()

mouvements.reverse()
print(mouvements, " taille : ", len(mouvements))
print("Taille de la frontière : ", len(frontiere))
print("Nombre de noeuds visité : ", len(explorer))
