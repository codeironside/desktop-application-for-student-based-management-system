from PyQt5.QtCore import (QCoreApplication, QMetaObject, Qt, QRect, QSize)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                             QPushButton, QWidget, QMessageBox)
import requests


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(407, 250)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 201, 151))
        self.label.setPixmap(QPixmap(u"freepik-export-20240621231312VLYX.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 150, 241, 51))
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 700 16pt \"Roboto\";")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"! incorrect credentials", None))
    # retranslateUi

