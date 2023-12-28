from PyQt5.Qt import *
from Registration import Dialog
import sqlite3
from PyQt5 import QtCore
from shifr import *
from Kurs_Shashki import *



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(596, 365)
        self.u_name_label = QLabel(Dialog)
        self.u_name_label.setGeometry(QRect(150, 110, 71, 20))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QLabel(Dialog)
        self.pass_label.setGeometry(QRect(150, 150, 71, 21))
        font = QFont()
        font.setPointSize(9)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QRect(230, 150, 113, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setGeometry(QRect(230, 200, 51, 23))
        self.login_btn.setObjectName("login_btn")
        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(290, 200, 81, 23))
        self.signup_btn.setObjectName("signup_btn")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 211, 51))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.u_name_label.setText(_translate("Dialog", "Логин"))
        self.pass_label.setText(_translate("Dialog", "Пароль"))
        self.login_btn.setText(_translate("Dialog", "Войти"))
        self.signup_btn.setText(_translate("Dialog", "Регистрация"))
        self.label.setText(_translate("Dialog", "Авторизация"))




class LoginDatabase():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def is_table(self, table_name):
        query = "SELECT name from sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        cursor = self.conn.execute(query)
        result = cursor.fetchone()
        if result == None:
            return False
        else:
            return True


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

       

        self.login_btn.clicked.connect(self.loginCheck)
        self.signup_btn.clicked.connect(self.signUpCheck)


    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    @QtCore.pyqtSlot()
    def loginCheck(self):
        

        username = trippledesencrypt(self.uname_lineEdit.text())
        password = trippledesencrypt(self.pass_lineEdit.text())
        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return


        file = open('login.txt', 'r', encoding='utf-8')
        text = file.readlines()
        file.close()

        for i in range(len(text)):
            if i < (len(text) - 1):
                text[i] = text[i][:-1]
            row = text[i].split(" ")
            flag = True
            if username == row[0] and password == row[2]:
                self.close()
                flag = False
                run()
                break

        if flag:
            self.showMessageBox('Внимание!', 'Неправильное имя пользователя или пароль.')


    def signUpCheck(self):
        self.signUpShow()




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = MainDialog()
    w.show()
    sys.exit(app.exec_())
