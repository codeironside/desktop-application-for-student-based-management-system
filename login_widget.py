from PyQt5.QtCore import pyqtSignal, QSize, Qt, QRect
from PyQt5.QtWidgets import QWidget, QDialog
from login import Ui_Form
from ui_wrong_details import Ui_Dialog
import requests
from PyQt5 import QtWidgets

TOKEN_FILE = "token.txt"
LOGIN_URL = "http://localhost:1030/api/v1/student/login"  # Replace with your actual login URL

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

        self.ui.login.clicked.connect(self.handle_login)

    def handle_login(self):
        matricNumber = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        response = self.authenticate(matricNumber, password)
        
        if response and "token" in response:
            with open(TOKEN_FILE, "w") as file:
                file.write(response["token"])
            #self.login_successful.emit()
        else:
            # Show the error message in a dialog box
            error_message = response["Message"] if response and "Message" in response else "Login failed"
            self.show_error_dialog(error_message)
    def authenticate(self, matricNumber, password):
        try:
            payload = {
                "matricNumber": matricNumber,
                "password": password
            }
            
            # Use the `data` parameter for URL-encoded data
            response = requests.post(LOGIN_URL, data=payload)
            response.raise_for_status()  
            print(response.json())  
            return response.json()
        except :
            
            error_message = response.json()['Message']
            print(f"HTTP error occurred: {error_message}")
            return {"Message": error_message}

    def show_error_dialog(self, message):
        dialog = QDialog(self)
        ui = Ui_Dialog()
        ui.setupUi(dialog)
        ui.label_2.setText(message) 
        dialog.exec()
