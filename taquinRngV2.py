import random
x = 9
taquin = [7,3,4,
          5,x,1,
          8,2,6]

nb = 0
mouvementPrecedent = 0

def legalMoove(tab):
     index = tab.index(9)
     if index == 0:
         return [1,3]
     if index == 1:
         return [-1,3,1]
     if index == 2:
         return [-1,3]
     if index == 3:
         return [-3,1,3]
     if index == 4:
         return  [-3,-1,1,3]
     if index == 5:
         return [-3,-1,3]
     if index == 6:
         return [-3,1]
     if index == 7:
         return [-3,-1,1]
     if index == 8:
         return [-3,-1]

def check(list):
    if (list == sorted(list)):
        return True
    else:
        return False


def choixMouvement(list):
    moov = random.choice(list)
    return moov

def afficherTaquin():
    tab1 = []
    tab2 = []
    tab3 = []
    tab1.append(taquin[0])
    tab1.append(taquin[1])
    tab1.append(taquin[2])
    tab2.append(taquin[3])
    tab2.append(taquin[4])
    tab2.append(taquin[5])
    tab3.append(taquin[6])
    tab3.append(taquin[7])
    tab3.append(taquin[8])
    print(tab1)
    print(tab2)
    print(tab3)
    print("nombre bien placé :", etatTaquin(taquin))
    print("liste de mouvements possible :", mouvementPossible)
    print("mouvement choisi :", mouvementChoisi)
    print()

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def etatTaquin(list):
    count = 0
    for s in range(0,len(list)):
        if s+1 == list[s]:
            count += 1
    return count

while check(taquin) == False:
    posX = taquin.index(9)
    mouvementPossible = legalMoove(taquin)

    if nb == 0:
        mouvementChoisi = choixMouvement(mouvementPossible)
    elif nb > 0:
        mouvementPossible.remove(mouvementPrecedent*-1)
        mouvementChoisi = choixMouvement(mouvementPossible)

    swapPositions(taquin, posX, posX + mouvementChoisi)
    mouvementPrecedent = mouvementChoisi
    nb += 1
    afficherTaquin()

print()
print(nb)