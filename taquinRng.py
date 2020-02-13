import random
x = 9
taquin = [7,3,4,
          5,x,1,
          8,2,6]

nb = 0
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

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


while check(taquin) == False:
    posX = taquin.index(9)
    moovPossible = random.choice(legalMoove(taquin))
    swapPositions(taquin, posX, posX + moovPossible)
    nb += 1

print(nb)

