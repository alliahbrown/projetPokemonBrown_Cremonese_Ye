# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'premier_pokemon.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from statPokemon import statPoke_init
import os
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from pokedex import Ui_FormPokedex

#import les images des pokémons
Bulbasaur = os.path.join(os.path.dirname(__file__), 'image', 'bulbasaur.gif')
Squirtle = os.path.join(os.path.dirname(__file__), 'image', 'squirtle.gif')
Charmander = os.path.join(os.path.dirname(__file__), 'image', 'charmander2.gif')

#import des descriptions de ces pokémons
texte_Bullbizarre, texte_Salameche, texte_Carapuce = statPoke_init() 

fond_ecran =  os.path.join(os.path.dirname(__file__),'image', 'ecran3.jpg')



class Ui_FormPokemon(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1112, 708)
        
        #Ajouter une image de fond
        self.labelpokedex = QtWidgets.QLabel(Form)
        self.labelpokedex.setGeometry(QtCore.QRect(0, 0, 1112, 708))
        self.labelpokedex.setText("")
        self.labelpokedex.setPixmap(QtGui.QPixmap(fond_ecran))
        self.labelpokedex.setScaledContents(True) # redimensionnez l'image à la taille de l'écran
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 40, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-weight: bold;") # mettre en gras

        
        self.labelBulbasaur = QtWidgets.QLabel(Form)
        self.labelBulbasaur.setGeometry(QtCore.QRect(100, 200, 261, 261))
        self.labelBulbasaur.setText("")
        self.movie = QMovie(Bulbasaur) #pour faire animer le gif
        self.labelBulbasaur.setMovie(self.movie) 
        self.movie.start() # démarrer le gif
        self.labelBulbasaur.setObjectName("labelBulbasaur")
        # Redimensionnez le GIF à la taille du QLabel
        self.movie.setScaledSize(QSize().scaled(200, 200, Qt.KeepAspectRatio))
        
        
        self.labelSquirtle = QtWidgets.QLabel(Form)
        self.labelSquirtle.setGeometry(QtCore.QRect(440, 220, 281, 221))
        self.labelSquirtle.setText("")
        self.movie = QMovie(Squirtle) #pour faire animer le gif
        self.labelSquirtle.setMovie(self.movie)
        self.movie.start() # démarrer le gif
        # Redimensionnez le GIF à la taille du QLabel
        self.movie.setScaledSize(QSize().scaled(200, 200, Qt.KeepAspectRatio))
        
        self.labelCharmander = QtWidgets.QLabel(Form)
        self.labelCharmander.setGeometry(QtCore.QRect(790, 210, 241, 231))
        self.labelCharmander.setText("")
        self.movie = QMovie(Charmander) #pour faire animer le gif
        self.labelCharmander.setMovie(self.movie)
        self.movie.start() # démarrer le gif
        self.labelCharmander.setObjectName("labelCharmander")
        # Redimensionnez le GIF à la taille du QLabel
        self.movie.setScaledSize(QSize().scaled(200, 200, Qt.KeepAspectRatio))
        
        self.pushButtonBulbasaur = QtWidgets.QPushButton(Form)
        self.pushButtonBulbasaur.setGeometry(QtCore.QRect(170, 480, 131, 41))
        self.pushButtonBulbasaur.setObjectName("pushButtonBulbasaur")
        #Pointeur d'information sur le pokémon
        self.pushButtonBulbasaur.setToolTip(texte_Bullbizarre)
        # Définir la couleur de fond du QPushButton
        self.pushButtonBulbasaur.setStyleSheet("background-color: rgb(144, 238, 144);")

        
        self.pushButtonSquirtle = QtWidgets.QPushButton(Form)
        self.pushButtonSquirtle.setGeometry(QtCore.QRect(490, 480, 151, 41))
        self.pushButtonSquirtle.setObjectName("pushButtonSquirtle")
        self.pushButtonSquirtle.setToolTip(texte_Carapuce)
        self.pushButtonSquirtle.setStyleSheet("background-color: rgb(144, 238, 144);")


        self.pushButtonCharmander = QtWidgets.QPushButton(Form)
        self.pushButtonCharmander.setGeometry(QtCore.QRect(810, 480, 151, 41))
        self.pushButtonCharmander.setObjectName("pushButtonCharmander")
        self.pushButtonCharmander.setToolTip(texte_Salameche)
        self.pushButtonCharmander.setStyleSheet("background-color: rgb(144, 238, 144);")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "First_Pokemon"))
        self.label.setText(_translate("Form", "Choose your pokemon :"))
        self.pushButtonBulbasaur.setText(_translate("Form", "BULBASAUR"))
        self.pushButtonSquirtle.setText(_translate("Form", "SQUIRTLE"))
        self.pushButtonCharmander.setText(_translate("Form", "CHARMANDER"))
        






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    ui = Ui_FormPokemon()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    



