# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_accueil.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')
from pokedex import Ui_FormPokedex

fond_ecran =  os.path.join(os.path.dirname(__file__),'image', 'ecran.png')


class MainWindow(object):
    

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 502)
        
        #Ajouter une image de fond
        self.labelpokedex = QtWidgets.QLabel(MainWindow)
        self.labelpokedex.setGeometry(QtCore.QRect(0, 0, 690, 502))
        self.labelpokedex.setText("")
        self.labelpokedex.setPixmap(QtGui.QPixmap(fond_ecran))
        self.labelpokedex.setScaledContents(True)
        
        
        
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
        self.labelTitre.setGeometry(QtCore.QRect(200, 40, 280, 102))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelTitre.setFont(font)
        self.labelTitre.setObjectName("labelTitre")
        self.labelPassword = QtWidgets.QLabel(self.frame)
        self.labelPassword.setGeometry(QtCore.QRect(100, 260, 111, 25))
        self.labelTitre.setStyleSheet("font-weight: bold;") # mettre en gras
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Connection"))
        self.labelID.setText(_translate("MainWindow", "ID"))
        self.labelTitre.setText(_translate("MainWindow", "CONNECTION"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.pushButtonValider.setText(_translate("MainWindow", "Ok"))
        self.pushButton_2.setText(_translate("MainWindow", "First connection"))
        
        
    
    def verifyLogin(self):
        """
        la fonction vérifie le login

        """
        # Récupérer le nom d'utilisateur et le mot de passe entrés par l'utilisateur
        ID = self.lineEditID.text()
        password = self.lineEditPassword.text()
        
        
        #Vérifier le Login
        if self.checkCredentials(ID, password):
            print("Login successful")
            
            return "Login successful", ID

            
        else:
            print("Login failed. Please try again.")
            return  "Login failed. Please try again.", ID

    def checkCredentials(self, ID, password):
        """
        La fonction vérifie les informations d'identification à partir du fichier JSON

        """
        
        with open(data, "r") as file:
            users = json.load(file)
            if ID in users:
                
                # Vérifier si le mot de passe correspond au nom d'utilisateur
                if users[str(ID)]['password'] == password:
                    return True
        return False



class Ui_erreur_login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(187, 116)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "erreur"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Login failed. Please try again.</span></p></body></html>"))





               

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    app.setQuitOnLastWindowClosed(True)
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    

    
    sys.exit(app.exec_())

    #message d'erreur si le login ou mot de passe incorrect
    mess_err = QtWidgets.QWidget()
    ui_erreur_log = Ui_erreur_login()
    ui_erreur_log.setupUi(mess_err)
    mess_err.show()

