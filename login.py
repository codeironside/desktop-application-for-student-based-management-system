from PyQt5.QtCore import (QCoreApplication, QMetaObject, Qt, pyqtSignal, QRect, QSize)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                             QPushButton, QWidget)
import requests

TOKEN_FILE = "token.txt"
LOGIN_URL = "https://yourapi.com/login"  # Replace with your actual login URL

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(734, 505)
        Form.setFixedSize(QSize(734, 505))
        Form.setMinimumSize(QSize(734, 505))
        Form.setMaximumSize(QSize(734, 505))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(248, 248, 248);")
        
        self.login = QPushButton(Form)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(530, 300, 71, 31))
        self.login.setStyleSheet(u"QPushButton { border: none; background-color: transparent; }\n"
                                 "QPushButton:pressed { background-color: #d0d0d0; }\n"
                                 "QPushButton:flat { border: none; color: rgb(0, 0, 0); }")
        icon = QIcon()
        icon.addFile(u"icons8-login-rounded-up-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login.setIcon(icon)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 350, 101, 31))
        self.pushButton_2.setStyleSheet(u"QPushButton { border: none; background-color: transparent; }\n"
                                        "QPushButton:pressed { background-color: #d0d0d0; }\n"
                                        "QPushButton:flat { border: none; }")
        icon1 = QIcon()
        icon1.addFile(u"user-avatar_6380179.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 350, 121, 31))
        self.pushButton_3.setStyleSheet(u"QPushButton { border: none; background-color: transparent; }\n"
                                        "QPushButton:pressed { background-color: #d0d0d0; }\n"
                                        "QPushButton:flat { border: none; }")
        icon2 = QIcon()
        icon2.addFile(u"icons8-forgot-password-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(480, 181, 171, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit { border: none; border-bottom: 2.5px solid; padding-top: 5px; }\n"
                                    "QLineEdit::placeholder { color: #A52A2A; opacity: 1; }\n"
                                    "QLineEdit::before { content: attr(placeholder); position: absolute; top: 1; left: 5px; font-size: 0.8em; color: #C0C0C0; transition: opacity 0.7s ease-in-out; }\n"
                                    "QLineEdit:not([placeholderText=\"\"])::before { opacity: 0; }")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(480, 251, 171, 31))
        self.lineEdit_2.setStyleSheet(u"QLineEdit { border: none; border-bottom: 2.5px solid #A52A2A; }")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 351, 231))
        self.label.setPixmap(QPixmap(u"college students-bro.svg"))
        self.label.setScaledContents(True)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 70, 101, 91))
        self.label_2.setPixmap(QPixmap(u"account_3033143.png"))
        self.label_2.setScaledContents(True)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 320, 381, 41))
        self.label_3.setStyleSheet(u"font: 700 italic 9pt \"Segoe UI\";")
        self.label_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(430, 60, 16, 351))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Register", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username or Matric Number", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"...stay informed, stay connected, your one step student management system...", None))
