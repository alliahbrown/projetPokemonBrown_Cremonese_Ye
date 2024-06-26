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

#import les images des pokémons
Bulbasaur = os.path.join(os.path.dirname(__file__), 'image', 'Bullbizarre.png')
Squirtle = os.path.join(os.path.dirname(__file__), 'image', 'Carapuce.png')
Charmander = os.path.join(os.path.dirname(__file__), 'image', 'Salameche.png')


texte_Bullbizarre, texte_Salameche, texte_Carapuce = statPoke_init()

class Ui_FormPokemon(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1112, 708)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 40, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.labelBulbasaur = QtWidgets.QLabel(Form)
        self.labelBulbasaur.setGeometry(QtCore.QRect(100, 200, 261, 261))
        self.labelBulbasaur.setText("")
        self.labelBulbasaur.setPixmap(QtGui.QPixmap(Bulbasaur))
        self.labelBulbasaur.setScaledContents(True)
        self.labelBulbasaur.setObjectName("labelBulbasaur")
        self.labelSquirtle = QtWidgets.QLabel(Form)
        self.labelSquirtle.setGeometry(QtCore.QRect(440, 220, 281, 221))
        self.labelSquirtle.setText("")
        self.labelSquirtle.setPixmap(QtGui.QPixmap(Squirtle))
        self.labelSquirtle.setScaledContents(True)
        self.labelSquirtle.setObjectName("labelSquirtle")
        self.labelCharmander = QtWidgets.QLabel(Form)
        self.labelCharmander.setGeometry(QtCore.QRect(790, 210, 241, 231))
        self.labelCharmander.setText("")
        self.labelCharmander.setPixmap(QtGui.QPixmap(Charmander))
        self.labelCharmander.setScaledContents(True)
        self.labelCharmander.setObjectName("labelCharmander")
        self.pushButtonBulbasaur = QtWidgets.QPushButton(Form)
        self.pushButtonBulbasaur.setGeometry(QtCore.QRect(170, 480, 131, 41))
        self.pushButtonBulbasaur.setObjectName("pushButtonBulbasaur")
        #Pointeur d'information sur le pokémon
        self.pushButtonBulbasaur.setToolTip(texte_Bullbizarre)
        
        self.pushButtonSquirtle = QtWidgets.QPushButton(Form)
        self.pushButtonSquirtle.setGeometry(QtCore.QRect(490, 480, 151, 41))
        self.pushButtonSquirtle.setObjectName("pushButtonSquirtle")
        self.pushButtonSquirtle.setToolTip(texte_Carapuce)
        self.pushButtonCharmander = QtWidgets.QPushButton(Form)
        self.pushButtonCharmander.setGeometry(QtCore.QRect(810, 480, 151, 41))
        self.pushButtonCharmander.setObjectName("pushButtonCharmander")
        self.pushButtonCharmander.setToolTip(texte_Salameche)

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
