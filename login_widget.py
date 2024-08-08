from PyQt5.QtCore import pyqtSignal, QSize, Qt,QRect
from PyQt5.QtWidgets import QWidget
from login import Ui_Form
import requests
from PyQt5 import QtWidgets

TOKEN_FILE = "token.txt"
LOGIN_URL = "https://yourapi.com/login"  # Replace with your actual login URL

class LoginWidget(QWidget):
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(734, 505)
        self.setMinimumSize(QSize(734, 505))
        self.setMaximumSize(QSize(734, 505))
        self.setGeometry(QRect(530, 300, 71, 31))
        self.resize(734,505)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.ui.login.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        response = self.authenticate(username, password)
        if response and "token" in response:
            with open(TOKEN_FILE, "w") as file:
                file.write(response["token"])
            self.login_successful.emit()
        else:
            print("Login failed")

    def authenticate(self, username, password):
        try:
            response = requests.post(LOGIN_URL, json={"username": username, "password": password})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
