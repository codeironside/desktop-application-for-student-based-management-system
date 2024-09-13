from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, QRect, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QMessageBox,
)

import requests
from ui_register import registration_window
from registeration import registerationWidget

TOKEN_FILE = "token.txt"
LOGIN_URL = (
    "http://localhost:1030/api/v1/student/login"  # Replace with your actual login URL
)


class Ui_Form(object):
    def setupUi(self, Form,login_widget):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(734, 505)
        Form.setFixedSize(QSize(734, 505))
        Form.setMinimumSize(QSize(734, 505))
        Form.setMaximumSize(QSize(734, 505))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(248, 248, 248);")

        self.login = QPushButton(Form)
        self.login.setObjectName("login")
        self.login.setGeometry(QRect(530, 300, 71, 31))
        self.login.setStyleSheet(
            "QPushButton { border: none; background-color: transparent; }\n"
            "QPushButton:pressed { background-color: #d0d0d0; }\n"
            "QPushButton:flat { border: none; color: rgb(0, 0, 0); }"
        )
        icon = QIcon()
        icon.addFile("icons8-login-rounded-up-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.login.setIcon(icon)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 350, 101, 31))
        self.pushButton_2.setStyleSheet(
            "QPushButton { border: none; background-color: transparent; }\n"
            "QPushButton:pressed { background-color: #d0d0d0; }\n"
            "QPushButton:flat { border: none; }"
        )
        icon1 = QIcon()
        icon1.addFile("user-avatar_6380179.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(570, 350, 121, 31))
        self.pushButton_3.setStyleSheet(
            "QPushButton { border: none; background-color: transparent; }\n"
            "QPushButton:pressed { background-color: #d0d0d0; }\n"
            "QPushButton:flat { border: none; }"
        )
        icon2 = QIcon()
        icon2.addFile("icons8-forgot-password-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QRect(480, 181, 171, 31))
        self.lineEdit.setStyleSheet(
            "QLineEdit { border: none; border-bottom: 2.5px solid; padding-top: 5px; }\n"
            "QLineEdit::placeholder { color: #A52A2A; opacity: 1; }\n"
            "QLineEdit::before { content: attr(placeholder); position: absolute; top: 1; left: 5px; font-size: 0.8em; color: #C0C0C0; transition: opacity 0.7s ease-in-out; }\n"
            'QLineEdit:not([placeholderText=""])::before { opacity: 0; }'
        )
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(480, 251, 171, 31))
        self.lineEdit_2.setStyleSheet(
            "QLineEdit { border: none; border-bottom: 2.5px solid #A52A2A; }"
        )
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(40, 70, 351, 231))
        self.label.setPixmap(QPixmap("college students-bro.svg"))
        self.label.setScaledContents(True)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(510, 70, 101, 91))
        self.label_2.setPixmap(QPixmap("account_3033143.png"))
        self.label_2.setScaledContents(True)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(30, 320, 381, 41))
        self.label_3.setStyleSheet('font: 700 italic 9pt "Segoe UI";')
        self.label_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)

        self.line = QFrame(Form)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(430, 60, 16, 351))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # Connect the login button click to the login function
        self.login.clicked.connect(self.login_request)
        self.pushButton_2.clicked.connect(
            lambda: self.registeration_page(Form, login_widget)
        )

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.login.setText(QCoreApplication.translate("Form", "Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", "Register", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("Form", "Forgot Password", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "Username or Matric Number", None)
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", "Password", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Form",
                "...stay informed, stay connected, your one step student management system...",
                None,
            )
        )

    def login_request(self):
        # Get the username and password from the input fields
        matricNumber = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Prepare the payload
        payload = {"matricNumber": matricNumber, "password": password}

        try:
            # Send a POST request to the login URL
            response = requests.post(LOGIN_URL, data=payload)

            if response.status_code == 202:
                print(response)
                self.show_message(
                    "Incorrect Details",
                    "The username or password you entered is incorrect.",
                )
            else:
                # Handle successful login or other status codes
                # self.show_message("Login Successful", "You have logged in successfully.")
                # Save the token or proceed with other logic
                with open(TOKEN_FILE, "w") as token_file:
                    token_file.write(response.text)
        except requests.RequestException as e:
            self.show_message(
                "Connection Error",
                f"Failed to connect to the server. Please try again.\nError: {e}",
            )

    def registeration_page(self, Form, login_widget):
        # registration_window = QWidget()
        # registration_form = Ui_Form()
        # registration_form.setupUi(registration_window)
        self.registration_window = registerationWidget()
        # Create an instance of registerationWidget
        self.registration_window.show()
        Form.close()
        login_widget.close()
