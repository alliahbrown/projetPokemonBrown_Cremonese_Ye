# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_MainWindow(object):
    

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 502)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelID = QtWidgets.QLabel(self.frame)
        self.labelID.setGeometry(QtCore.QRect(100, 180, 68, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelID.setFont(font)
        self.labelID.setTextFormat(QtCore.Qt.AutoText)
        self.labelID.setScaledContents(False)
        self.labelID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelID.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelID.setObjectName("labelID")
        self.labelTitre = QtWidgets.QLabel(self.frame)
        self.labelTitre.setGeometry(QtCore.QRect(230, 80, 214, 42))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelTitre.setFont(font)
        self.labelTitre.setObjectName("labelTitre")
        self.labelPassword = QtWidgets.QLabel(self.frame)
        self.labelPassword.setGeometry(QtCore.QRect(100, 260, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelPassword.setFont(font)
        self.labelPassword.setTextFormat(QtCore.Qt.AutoText)
        self.labelPassword.setScaledContents(False)
        self.labelPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPassword.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditID = QtWidgets.QLineEdit(self.frame)
        self.lineEditID.setGeometry(QtCore.QRect(230, 170, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditID.setFont(font)
        self.lineEditID.setText("")
        self.lineEditID.setObjectName("lineEditID")
        self.lineEditPassword = QtWidgets.QLineEdit(self.frame)
        self.lineEditPassword.setGeometry(QtCore.QRect(230, 260, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonValider = QtWidgets.QPushButton(self.frame)
        self.pushButtonValider.setGeometry(QtCore.QRect(230, 330, 75, 23))
        self.pushButtonValider.setObjectName("pushButtonValider")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 330, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelID.setText(_translate("MainWindow", "ID"))
        self.labelTitre.setText(_translate("MainWindow", "CONNECTION"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.pushButtonValider.setText(_translate("MainWindow", "Ok"))
        self.pushButton_2.setText(_translate("MainWindow", "First connection"))
        
        

        


class MainWindow( Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(parent)
        
        # Connecter le bouton de connexion à la fonction de vérification
        self.pushButtonValider.clicked.connect(self.verifyLogin)

    #vérifier le login
    def verifyLogin(self):
        
        # Récupérer le nom d'utilisateur et le mot de passe entrés par l'utilisateur
        ID = self.lineEditID.text()
        password = self.lineEditPassword.text()
        
        
        #Vérifier le Login
        if self.checkCredentials(ID, password):
            print("Login successful")
            # Vous pouvez ouvrir une nouvelle fenêtre ou effectuer d'autres actions ici
            
            
            
        else:
            print("Login failed. Please try again.")
            # Vous pouvez afficher un message d'erreur à l'utilisateur ou effectuer d'autres actions ici

    def checkCredentials(self, ID, password):
        # Vérifier les informations d'identification à partir du fichier JSON
        with open(r"F:\Pokemon\projetPokemonBrown_Cremonese_Ye\interface\data\data_user.json", "r") as file:
            users = json.load(file)
            if ID in users:
                
                # Vérifier si le mot de passe correspond au nom d'utilisateur
                if users[ID] == password:
                    return True
        return False
               
               

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    app.setQuitOnLastWindowClosed(True)
    ui = MainWindow(Window)
    Window.show()
    sys.exit(app.exec_())
