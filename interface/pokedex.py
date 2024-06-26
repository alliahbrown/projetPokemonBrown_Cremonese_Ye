# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pokedex.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pokemon import dico_poke
from statPokemon import statPoke

#importer l'image du pokedex
pokedex = os.path.join(os.path.dirname(__file__), 'image', 'pokedex.jpg')


class Ui_FormPokedex(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 636)
        self.labelpokedex = QtWidgets.QLabel(Form)
        self.labelpokedex.setGeometry(QtCore.QRect(10, 10, 421, 611))
        self.labelpokedex.setText("")
        self.labelpokedex.setPixmap(QtGui.QPixmap(pokedex))
        self.labelpokedex.setScaledContents(True)
        self.labelpokedex.setObjectName("labelpokedex")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(50, 120, 335, 320))
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.listWidgetPokemon = QtWidgets.QListWidget(self.widget)
        self.listWidgetPokemon.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.listWidgetPokemon.setObjectName("listWidgetPokemon")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidgetMesPokemons = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetMesPokemons.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.listWidgetMesPokemons.setObjectName("listWidgetMesPokemons")
        self.tabWidget.addTab(self.tab_2, "")
        self.NomPoke = QtWidgets.QLabel(Form)
        self.NomPoke.setGeometry(QtCore.QRect(50, 470, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NomPoke.setFont(font)
        self.NomPoke.setScaledContents(False)
        self.NomPoke.setObjectName("NomPoke")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(140, 510, 191, 81))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 79))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.infoPoke = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.infoPoke.setGeometry(QtCore.QRect(0, 0, 191, 81))
        self.infoPoke.setObjectName("infoPoke")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.pushButtonTop = QtWidgets.QPushButton(Form)
        self.pushButtonTop.setGeometry(QtCore.QRect(70, 512, 31, 21))
        self.pushButtonTop.setText("")
        self.pushButtonTop.setCheckable(False)
        self.pushButtonTop.setDefault(False)
        self.pushButtonTop.setFlat(True)
        self.pushButtonTop.setObjectName("pushButtonTop")
        self.pushButtonTop.clicked.connect(self.up)
        
        self.pushButtonRight = QtWidgets.QPushButton(Form)
        self.pushButtonRight.setGeometry(QtCore.QRect(100, 540, 21, 21))
        self.pushButtonRight.setText("")
        self.pushButtonRight.setCheckable(False)
        self.pushButtonRight.setDefault(False)
        self.pushButtonRight.setFlat(True)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.pushButtonRight.clicked.connect(self.right)
        
        self.pushButtonDown = QtWidgets.QPushButton(Form)
        self.pushButtonDown.setGeometry(QtCore.QRect(70, 560, 21, 21))
        self.pushButtonDown.setText("")
        self.pushButtonDown.setCheckable(False)
        self.pushButtonDown.setDefault(False)
        self.pushButtonDown.setFlat(True)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.pushButtonDown.clicked.connect(self.down)
        
        self.pushButtonLeft = QtWidgets.QPushButton(Form)
        self.pushButtonLeft.setGeometry(QtCore.QRect(50, 540, 21, 21))
        self.pushButtonLeft.setText("")
        self.pushButtonLeft.setCheckable(False)
        self.pushButtonLeft.setDefault(False)
        self.pushButtonLeft.setFlat(True)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.pushButtonLeft.clicked.connect(self.left)
        
        self.Delete = QtWidgets.QPushButton(Form)
        self.Delete.setGeometry(QtCore.QRect(350, 510, 21, 21))
        self.Delete.setText("")
        self.Delete.setCheckable(False)
        self.Delete.setDefault(False)
        self.Delete.setFlat(True)
        self.Delete.setObjectName("Delete")
        self.Delete.clicked.connect(self.remove)
        
        self.Check = QtWidgets.QPushButton(Form)
        self.Check.setGeometry(QtCore.QRect(370, 550, 31, 31))
        self.Check.setText("")
        self.Check.setCheckable(False)
        self.Check.setDefault(False)
        self.Check.setFlat(True)
        self.Check.setObjectName("Check")
        self.Check.clicked.connect(self.getItem)
        
        #ajouter le nom de tous les pokémons dans le pokédex
        nom_poke = list(dico_poke.keys())
        for k in range(len(nom_poke)):
            nomPoke = list(dico_poke.keys())[k]
            self.listWidgetPokemon.addItem(QtWidgets.QListWidgetItem(nomPoke))
        self.listWidgetPokemon.itemClicked.connect(self.getItem)
        self.listWidgetMesPokemons.itemClicked.connect(self.getItem)
        
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pokedex"))
        __sortingEnabled = self.listWidgetPokemon.isSortingEnabled()
        self.listWidgetPokemon.setSortingEnabled(False)
        self.listWidgetPokemon.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "Pokemon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "My Pokemons"))
        self.NomPoke.setText(_translate("Form", ""))
    
    def getItem(self):
        """
        La fonction affiche les caractéristiques des pokémons sélectionnés dans le pokédex

        Returns
        -------
        None.

        """
        fenetre = self.tabWidget.currentIndex()
        #Pour savoir sur quel table Widget je suis
        
        if fenetre == 0:
        #Fenêtre de Pokemon
            item = self.listWidgetPokemon.currentItem()

        else:
        #Fenêtre my Pokemons
            item = self.listWidgetMesPokemons.currentItem()
        
        self.NomPoke.setText(str(item.text()))
        #Récupéraration du nom des pokémons clickés
            
        text = statPoke(str(item.text()))
        #Récupération des données des pokémons
        
        self.infoPoke.setText(text)
        
    def remove(self):
        """
        La fonction fait un retour en arrière du pokédex

        Returns
        -------
        None.

        """
        self.NomPoke.clear()
        self.infoPoke.clear()
        
    def up(self):
        """
        La fonction permet au curseur de se déplacer vers le haut dans la listWidget

        Returns
        -------
        None.

        """
        fenetre = self.tabWidget.currentIndex()
        if fenetre == 0:
            item = self.listWidgetPokemon.currentRow()
            self.listWidgetPokemon.setCurrentRow(item - 1)
        else:
            item = self.listWidgetMesPokemons.currentRow()
            self.listWidgetMesPokemons.setCurrentRow(item - 1)
        
    def down(self):
        fenetre = self.tabWidget.currentIndex()
    
        if fenetre == 0:
            item = self.listWidgetPokemon.currentRow()
            self.listWidgetPokemon.setCurrentRow(item + 1)
        else:
            item = self.listWidgetMesPokemons.currentRow()
            self.listWidgetMesPokemons.setCurrentRow(item + 1)
    
    def left(self):
        """
        La fonction ouvre ma fenêtre de Pokémon

        Returns
        -------
        None.

        """
        self.tabWidget.setCurrentIndex(0)
    
    def right(self):
        """
        La fonction ouvre ma fenêtre de droite (Mon Pokémon)

        Returns
        -------
        None.

        """
        self.tabWidget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    ui_Pokedex = Ui_FormPokedex()
    ui_Pokedex.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
