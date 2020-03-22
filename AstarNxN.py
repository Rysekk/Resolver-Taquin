import math
import random

trou = 0
taquin = [2,5,7,1,4,6,0,3,8]

frontiere = []
explorer = []
goal_state = [0,1,2,3,4,5,6,7,8]
n = 3

def legalMoove(tab):
    index = tab.index(0)
    if index == 0:
        return [1, 3]
    if index == 1:
        return [-1, 3, 1]
    if index == 2:
        return [-1, 3]
    if index == 3:
        return [-3, 1, 3]
    if index == 4:
        return [-3, -1, 1, 3]
    if index == 5:
        return [-3, -1, 3]
    if index == 6:
        return [-3, 1]
    if index == 7:
        return [-3, -1, 1]
    if index == 8:
        return [-3, -1]

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def desordre(list): #h2
    count = len(taquin)
    for s in range(0, len(list)):
        if s == list[s]:
            count -= 1
    return count

def inversion(list):
    sum = 0
    for s in range(0,len(list)):
        for i in range(s+1,len(list)):
            if list[s] > list[i]:
                if list[s] != 9:
                    sum += 1
    return sum

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

def manhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ 3) , i % 3
        goal_row,goal_col = int(item /3),item % 3
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict

class noeud:
    mouvement = []
    def __init__(self, list , mouv, prec, pere, generation):
        self.tab = list
        self.pere = pere
        self.prec = prec
        self.mouvement = mouv
        self.inv = inversion(self.tab)
        self.generation = generation+1
        self.des = desordre(self.tab)
        self.man = manhattan(self.tab)
        self.heuristic = self.generation + self.man + self.inv
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
    def etatBut(self):
        if self.des == 0:
            return True
        else:
            False
    def getPere(self):
        return self.pere
    def expend(self):
        mouvementPossible = legalMoove(self.tab)
        for s in range(0, len(mouvementPossible)):

            tab = self.tab.copy()
            posX = tab.index(trou)
            mouv = mouvementPossible[s]

            swapPositions(tab, posX, mouv + posX)
            nouveauNoeud = noeud(tab, mouv, self.mouvement, self, self.generation)

            if frontiere == []:
                frontiere.append(nouveauNoeud)
            else:
                x = False
                y = False

                 ### CHECK SI TAQUIN EXISTE DANS LA FRONTIERE ###
                for s in range(0,len(frontiere)):
                    if nouveauNoeud.getTaquin() == frontiere[s].getTaquin():
                        x = True
                        y = True
                        break

                ### PLACER TAQUIN DANS LA FRONTIERE AU BON ENDROIT ###
                for s in range(0, len(frontiere)):
                    if (frontiere[s].getH() >= nouveauNoeud.getH()) & (y == False):
                        frontiere.insert(s,nouveauNoeud)
                        x = True
                        break

                ### AJOUTER A LA FIN ###
                if x == False & y == False:
                    frontiere.append(nouveauNoeud)

        ## AJOUTER A LA LISTE DES EXPLORER ET RETIRE DE LA FRONTIERE ##
        explorer.append(self)
        if self.getGeneration() >= 1:
            frontiere.remove(self)


root = noeud(taquin,[], None, None, -1)
root.expend()

while frontiere[0].etatBut() != True:
    best = frontiere[0].getH()
    count = []

    for s in range(0, len(frontiere)):
        if frontiere[s].getH() == best:
            count.append(s)
    RNGESUS = random.choice(count)
    frontiere[RNGESUS].expend()

### AFFICHAGE SOLUTION ###

mouvements = []
noeud = frontiere[0]
while noeud.getGeneration() != 0:
    mouvements.append(noeud.getMouv())
    noeud = noeud.getPere()
print()
afficherTaquin(noeud.getTaquin())
mouvements.reverse()
print(mouvements, " taille : ", len(mouvements))
print("Taille de la frontière : ", len(frontiere))
print("Nombre de noeuds visité : ", len(explorer))
