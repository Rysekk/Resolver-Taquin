# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fenetretaquingraphique.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import math 
import time
choix = 0
trou = 0
delta = 1
taquin = []
frontiere = []
explorer = []
goal_state = []
n = 3 
nbShuffle = 1000

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frameButt = QtWidgets.QFrame(self.centralwidget)
        self.frameButt.setGeometry(QtCore.QRect(10, 480, 771, 71))
        self.frameButt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frameButt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButt.setObjectName("frameButt")

        self.pushButtonMel = QtWidgets.QPushButton(self.frameButt)
        self.pushButtonMel.setGeometry(QtCore.QRect(200, 20, 131, 31))
        self.pushButtonMel.setObjectName("pushButtonMel")
        self.pushButtonMel.clicked.connect(self.melange)
        
        self.pushButtonRes = QtWidgets.QPushButton(self.frameButt)
        self.pushButtonRes.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.pushButtonRes.setObjectName("pushButtonRes")
        self.pushButtonRes.clicked.connect(self.resolution)

        self.labelChoix = QtWidgets.QLabel(self.frameButt)
        self.labelChoix.setGeometry(QtCore.QRect(380, 10, 400, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelChoix.setFont(font)
        self.labelChoix.setObjectName("labelChoix")

        self.horizontalSliderPoid = QtWidgets.QSlider(self.frameButt)
        self.horizontalSliderPoid.setEnabled(True)
        self.horizontalSliderPoid.setGeometry(QtCore.QRect(430, 40, 160, 22))
        self.horizontalSliderPoid.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSliderPoid.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalSliderPoid.setMaximum(20)
        self.horizontalSliderPoid.setProperty("value", 10)
        self.horizontalSliderPoid.setSliderPosition(10)
        self.horizontalSliderPoid.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderPoid.setInvertedAppearance(False)
        self.horizontalSliderPoid.setInvertedControls(False)
        self.horizontalSliderPoid.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSliderPoid.setObjectName("horizontalSliderPoid")
        self.horizontalSliderPoid.valueChanged.connect(self.changeDelta)

        self.label_Poid = QtWidgets.QLabel(self.frameButt)
        self.label_Poid.setGeometry(QtCore.QRect(616, 40, 40, 21))
        font = QtGui.QFont()
        font.setFamily("LemonMilk")
        font.setPointSize(12)
        self.label_Poid.setFont(font)
        self.label_Poid.setObjectName("label_Poid")

        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(10, 10, 771, 461))
        self.frame_1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")

        #Creation du taquin graphique
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 10, 261, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.Taquin = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Taquin.setContentsMargins(1, 1, 1, 1)
        self.Taquin.setSpacing(1)
        self.Taquin.setObjectName("Taquin")

        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.Taquin.addWidget(self.label_1, 0, 0, 1, 1)

        
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Taquin.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.Taquin.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Taquin.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Taquin.addWidget(self.label_5, 1, 1, 1, 1)

        
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Taquin.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Taquin.addWidget(self.label_7, 2, 0, 1, 1)

        
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.Taquin.addWidget(self.label_8, 2, 1, 1, 1)
    
        
        self.label_trou = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(20)
        self.label_trou.setFont(font)
        self.label_trou.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_trou.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trou.setObjectName("label_trou")
        self.Taquin.addWidget(self.label_trou, 2, 2, 1, 1)

        

        self.labelTemps = QtWidgets.QLabel(self.frame_1)
        self.labelTemps.setGeometry(QtCore.QRect(20, 273, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(12)
        self.labelTemps.setFont(font)
        self.labelTemps.setObjectName("labelTemps")

        self.labelNbTD = QtWidgets.QLabel(self.frame_1)
        self.labelNbTD.setGeometry(QtCore.QRect(20, 310, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(12)
        self.labelNbTD.setFont(font)
        self.labelNbTD.setObjectName("labelNbTD")

        self.labelVisite = QtWidgets.QLabel(self.frame_1)
        self.labelVisite.setGeometry(QtCore.QRect(20, 347, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(12)
        self.labelVisite.setFont(font)
        self.labelVisite.setObjectName("labelVisite")

        self.labelNbDeplacement = QtWidgets.QLabel(self.frame_1)
        self.labelNbDeplacement.setGeometry(QtCore.QRect(20, 380, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(12)
        self.labelNbDeplacement.setFont(font)
        self.labelNbDeplacement.setObjectName("labelNbDeplacement")

        self.labelDeplacement = QtWidgets.QLabel(self.frame_1)
        self.labelDeplacement.setGeometry(QtCore.QRect(20, 420, 800, 31))
        font = QtGui.QFont()
        font.setFamily("Bree Serif")
        font.setPointSize(13)
        self.labelDeplacement.setFont(font)
        self.labelDeplacement.setObjectName("labelDeplacement")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resolveur de Taquin"))
        self.pushButtonRes.setText(_translate("MainWindow", "Resolution du Taquin"))
        self.pushButtonMel.setText(_translate("MainWindow", "Melanger le Taquin"))
        self.labelChoix.setText(_translate("MainWindow", "Choisir le poid que vous voulez associer à Manhattan"))
        self.label_Poid.setText(_translate("MainWindow", "1"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.label_6.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_trou.setText(_translate("MainWindow", " "))
        self.labelTemps.setText(_translate("MainWindow", "Temps :"))
        self.labelNbTD.setText(_translate("MainWindow", "Tuile déplacé :"))
        self.labelVisite.setText(_translate("MainWindow", "Noeuds visité : "))
        self.labelNbDeplacement.setText(_translate("MainWindow", "Nombre de deplacement :"))
        self.labelDeplacement.setText(_translate("MainWindow", "Deplacement :"))
    

    
    def changeDelta(self):
        delta = self.horizontalSliderPoid.value()/10
        noeud.changeDelta(self,delta)
        self.label_Poid.setText(QtCore.QCoreApplication.translate("MainWindow", str(delta)))


    def melange(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelTemps.setText(_translate("MainWindow", "Temps :"))
        self.labelNbTD.setText(_translate("MainWindow", "Tuile déplacé :"))
        self.labelVisite.setText(_translate("MainWindow", "Noeuds visité : "))
        self.labelNbDeplacement.setText(_translate("MainWindow", "Nombre de deplacement :"))
        self.labelDeplacement.setText(_translate("MainWindow", "Deplacement :"))
        rand(taquin)
        if taquin[0] == 0 : 
            self.label_1.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_1.setText(QtCore.QCoreApplication.translate("MainWindow",str(taquin[0])))
        if taquin[1] == 0 : 
            self.label_2.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_2.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[1])))

        if taquin[2] == 0 : 
            self.label_3.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_3.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[2])))

        if taquin[3] == 0 : 
            self.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_4.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[3])))

        if taquin[4] == 0 : 
            self.label_5.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_5.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[4])))

        if taquin[5] == 0 : 
            self.label_6.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_6.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[5])))

        if taquin[6] == 0 : 
            self.label_7.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_7.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[6])))

        if taquin[7] == 0 : 
            self.label_8.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_8.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[7])))

        if taquin[8] == 0 : 
            self.label_trou.setText(QtCore.QCoreApplication.translate("MainWindow", " "))
        else:
            self.label_trou.setText(QtCore.QCoreApplication.translate("MainWindow", str(taquin[8])))
            
    def resolution(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelTemps.setText(_translate("MainWindow", "Temps :"))
        self.labelNbTD.setText(_translate("MainWindow", "Tuile déplacé :"))
        self.labelVisite.setText(_translate("MainWindow", "Noeuds visité : "))
        self.labelNbDeplacement.setText(_translate("MainWindow", "Nombre de deplacement :"))
        self.labelDeplacement.setText(_translate("MainWindow", "Deplacement :"))
        a = time.time()
        root.expend()
        while frontiere[0].etatBut() != True:
            best = frontiere[0].getH()
            count = []
            for s in range(0, len(frontiere)):
                if frontiere[s].getH() == best:
                    count.append(s)
                else:
                    break
            RNGESUS = random.choice(count)
            ### PRAY FROR RNGESUS ###
            frontiere[RNGESUS].expend()
        b = time.time()
        temps = b-a
        mouvements = []
        noeud = frontiere[0]
        while noeud.getGeneration() != 0:
            mouvements.append(noeud.getMouv())
            noeud = noeud.getPere()
        mouvements.reverse()
        Ui_MainWindow.affichage(self,mouvements,temps)
        frontiere.clear()
        frontiere.clear()
        explorer.clear()
        mouvements.clear()
        

    def affichage(self,mouvement,temps):
        _translate = QtCore.QCoreApplication.translate
        self.labelTemps.setText(_translate("MainWindow", "Temps : " + str(float(temps)) + " secondes"))
        self.labelNbDeplacement.setText(_translate("MainWindow", "Nombre de deplacement : " + str(len(mouvement))))
        self.labelVisite.setText(_translate("MainWindow", "Noeuds visité : " + str(len(explorer))))
        self.labelNbTD.setText(_translate("MainWindow", "Tuile déplacé : " + str(len(frontiere) + len(explorer))))
        for s in range(0,len(mouvement)):
            if mouvement[s] == 1 and s+1 != len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ← " ))
            elif mouvement[s] == -1 and s+1 != len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" → "))  
            elif mouvement[s] == 3 and s+1 != len(mouvement):
                  self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ↑ "))
            elif mouvement[s] == -3 and s+1 != len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ↓ "))
            elif mouvement[s] == 1 and s+1 == len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ←"))
            elif mouvement[s] == -1 and s+1 == len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" →"))
            elif mouvement[s] == 3 and s+1 == len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ↑"))
            elif mouvement[s] == -3 and s+1 == len(mouvement):
                self.labelDeplacement.setText(_translate("MainWindow", self.labelDeplacement.text()+" ↓"))
    
for s in range(0,n*n):
    taquin.append(s)

def rand(list):
        for s in range(0,nbShuffle):
            posX = list.index(trou)
            mouvPoss = legalMoove(list)
            mouv = random.choice(mouvPoss)
            swapPositions(taquin,posX, mouv + posX)

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

def desordre(list): #h2
    count = len(list)
    for s in range(0, len(list)):
        if s == list[s]:
            count -= 1
    return count

def manhattan(initial_state):
    initial_config = initial_state
    manDict = 0
    for i,item in enumerate(initial_config):
        prev_row,prev_col = int(i/ n) , i % n
        goal_row,goal_col = int(item /n),item % n
        manDict += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return manDict

class noeud:
    def __init__(self, list , mouv, prec, pere, generation,delta):
        self.tab = list
        self.pere = pere
        self.prec = prec
        self.delta = delta 
        self.mouvement = mouv
        self.generation = generation+1
        self.des = desordre(self.tab)
        self.man = manhattan(self.tab)
        self.heuristic = self.generation + self.man*self.delta
    def changeDelta(self,delta):
        self.delta = delta
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
    def getDelta(self):
        return self.delta
    def etatBut(self):
        if self.des == 0:
            return True
        else:
            return False
    def getPere(self):
        return self.pere
    def expend(self):
        mouvementPossible = legalMoove(self.tab)
        
        try :
            mouvementPossible.remove(self.mouvement * -1)
        except :
            pass

        for s in range(0, len(mouvementPossible)):
            tab = self.tab.copy()
            posX = tab.index(trou)
            mouv = mouvementPossible[s]
            swapPositions(tab, posX, mouv + posX)
            nouveauNoeud = noeud(tab, mouv, self.mouvement, self, self.generation,self.delta)
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
root = noeud(taquin,[], None, None, -1,delta)

        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
