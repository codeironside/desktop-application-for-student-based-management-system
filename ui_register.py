from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, QRect, QSize
from PyQt5.QtGui import QIcon, QPixmap, QCursor, QIcon, QPixmap
from PyQt5.QtQuickWidgets import QQuickWidget
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QComboBox,
    QTextEdit,
    QPushButton,
    QWidget,
    QMessageBox,
)


class registration_window(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1196, 637)
        Form.setMaximumSize(QSize(1196, 637))
        self.quickWidget = QQuickWidget(Form)
        self.quickWidget.setObjectName("quickWidget")
        self.quickWidget.setGeometry(QRect(400, 60, 781, 511))
        self.quickWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.quickWidget.setStyleSheet(
            "background-color:#A52A2A; \n" "border-left-color: 3px solid rgb(85, 0, 0);"
        )
        self.quickWidget.setResizeMode(QQuickWidget.ResizeMode.SizeRootObjectToView)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(450, 100, 171, 31))
        self.lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(30, 145, 291, 291))
        self.label.setPixmap(QPixmap("Tablet login-pana.svg"))
        self.label.setScaledContents(True)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(960, 100, 171, 31))
        self.lineEdit_2.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(450, 170, 171, 31))
        self.lineEdit_3.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(450, 240, 171, 31))
        self.lineEdit_4.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(960, 170, 171, 31))
        self.lineEdit_5.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(950, 310, 181, 31))
        self.lineEdit_6.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: 2px solid #795548; /* Primary brown shade for border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 5px 10px; /* Padding inside the input */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(680, 240, 171, 31))
        self.lineEdit_7.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(680, 170, 171, 31))
        self.lineEdit_8.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_9 = QLineEdit(Form)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(680, 100, 171, 31))
        self.lineEdit_9.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: none; /* No border */\n"
            "    border-bottom: 2px solid #795548; /* Primary brown shade for bottom border */\n"
            "    padding: 5px 0; /* Padding inside the input, adjusted for bottom border */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-bottom-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-bottom-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_13 = QLineEdit(Form)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(450, 310, 171, 31))
        self.lineEdit_13.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_13.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF; /* White background */\n"
            "    border: 2px solid #795548; /* Primary brown shade for border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 5px 10px; /* Padding inside the input */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "    border-color: #6D4C41; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #5D4037; /* Even darker brown when focused */\n"
            "}"
        )
        self.lineEdit_13.setEchoMode(QLineEdit.EchoMode.Password)
        self.line = QFrame(Form)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(340, 70, 20, 461))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(460, 370, 571, 141))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.textEdit.setStyleSheet(
            "QTextEdit{\n" "\n" "border:none;\n" "border-bottom: 2px solid;\n" "}"
        )
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(80, 440, 171, 16))
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setStyleSheet('font: 14px 700 italic 9pt "Roboto";')
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(1000, 580, 161, 41))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #72360F; /* Primary brown shade */\n"
            "    color: white; /* White text */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '	font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #8B4513; /* Darker brown shade on hover */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #59260B; /* Even darker brown when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #D7CCC8; /* Light brown background for disabled state */\n"
            "    color: #BCAAA4; /* Light brown text for disabled state */\n"
            "}"
        )
        icon = QIcon()
        icon.addFile("upload-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(950, 231, 191, 41))
        self.comboBox.setCursor(QCursor(Qt.ClosedHandCursor))
        self.comboBox.setStyleSheet(
            "\n"
            "QComboBox {\n"
            "    border: none; /* Light gray border */\n"
            "  ; /* Rounded corners */\n"
            "border-bottom: 2px solid #795548;\n"
            "    padding: 5px; /* Padding inside the combo box */\n"
            "    background-color: #FFFFFF; /* White background */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "color:#795548;\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "    border-color: #795548; /* Light blue border on hover */\n"
            "}\n"
            "\n"
            "QComboBox::drop-down {\n"
            "    border: none; /* Remove border of drop-down button */\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 30px; /* Width of drop-down button */\n"
            "    background-color: #FFFFFF; /* White background for drop-down button */\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "    image: url(down_arrow_icon.png); /* Path to your down arrow icon */\n"
            "    width: 14px; /* Width of down arrow icon */\n"
            "    height: 14px; /* Height of down arrow icon */\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: 1px solid #B"
            "DBDBD; /* Border of the drop-down list */\n"
            "    selection-background-color: #8C9EFF; /* Background color of selected item */\n"
            "    selection-color: #FFFFFF; /* Text color of selected item */\n"
            "    background-color: #FFFFFF; /* Background color of the drop-down list */\n"
            "    padding: 5px; /* Padding inside the drop-down list */\n"
            "    outline: none; /* Remove outline */\n"
            '    font: 14px "Roboto", sans-serif; /* Font of items in drop-down list */\n'
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item {\n"
            "    padding: 5px; /* Padding for each item */\n"
            "    background-color: #FFFFFF; /* Background color for each item */\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item:hover {\n"
            "    background-color: #DE9967; /* Light gray background on hover */\n"
            "}"
        )
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(1020, 10, 161, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "  /*  background-color: #D7CCC8;  Light brown background */\n"
            "    color: #795548; /* Primary brown shade for text */\n"
            "    border: none; /* No border */\n"
            "    /*  border-radius: 4px;Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 14px "Roboto", sans-serif; /* Modern font */\n'
            "    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.2); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #C3B091; /* Darker shade on hover */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #BCAAA4; /* Even darker when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            ""
        )
        icon1 = QIcon()
        icon1.addFile("left-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setFlat(True)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(700, 260, 231, 151))
        self.label_3.setPixmap(QPixmap("3232487_43916.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.raise_()
        self.quickWidget.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_13.raise_()
        self.line.raise_()
        self.textEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.comboBox.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "fIrst Name", None)
        )
        self.label.setText("")
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", "Last name", None)
        )
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("Form", "Email", None)
        )
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("Form", "Faculty", None)
        )
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("Form", "Phone Number", None)
        )
        self.lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("Form", "Confirm Password", None)
        )
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("Form", "Department", None)
        )
        self.lineEdit_8.setPlaceholderText(
            QCoreApplication.translate("Form", "User Name", None)
        )
        self.lineEdit_9.setPlaceholderText(
            QCoreApplication.translate("Form", "Middle Name", None)
        )
        self.lineEdit_13.setPlaceholderText(
            QCoreApplication.translate("Form", "Password", None)
        )
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "Tell us About Yourself", None)
        )
        self.label_2.setText(QCoreApplication.translate("Form", "...Welcome...", None))
        self.pushButton.setText(QCoreApplication.translate("Form", " Submit", None))
        self.comboBox.setItemText(
            0, QCoreApplication.translate("Form", "100 Level", None)
        )
        self.comboBox.setItemText(
            1, QCoreApplication.translate("Form", "200 Level", None)
        )
        self.comboBox.setItemText(
            2, QCoreApplication.translate("Form", "300 Level", None)
        )
        self.comboBox.setItemText(
            3, QCoreApplication.translate("Form", "400 Level", None)
        )
        self.comboBox.setItemText(
            4, QCoreApplication.translate("Form", "500 Level", None)
        )

        self.comboBox.setPlaceholderText(
            QCoreApplication.translate("Form", "Level", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", "Back to Login", None)
        )
        self.label_3.setText("")

    # retranslateUi
