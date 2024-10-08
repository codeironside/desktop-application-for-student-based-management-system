from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
import os

from dash import Ui_MainWindow
from login_widget import LoginWidget  # Import the custom login widget

from login import Ui_Form


TOKEN_FILE = "token.txt"
VERIFY_URL = "http://localhost:1030"  # Replace with your actual token verification URL


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.check_credentials()

    def check_credentials(self):
        if not os.path.exists(TOKEN_FILE):
            self.open_login()
            return

        token = self.read_token()
        if token and self.verify_token(token):
            self.open_dashboard()
        else:
            self.open_login()

    def read_token(self):
        if not os.path.exists(TOKEN_FILE):
            return None

        with open(TOKEN_FILE, "r") as file:
            return file.read().strip()

    def verify_token(self, token):
        try:
            response = requests.post(
                VERIFY_URL, headers={"Authorization": f"Bearer {token}"}
            )
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return False

    def open_dashboard(self):
        self.dashboard = Ui_MainWindow()
        self.setCentralWidget(self.dashboard)

    def open_login(self):
        self.login = LoginWidget()
        self.login.login_successful.connect(self.open_dashboard)
        self.setCentralWidget(self.login)


if __name__ == "__main__":
    app = QApplication([])
    login_widget = LoginWidget()
    ui = Ui_Form()
    ui.setupUi(login_widget,login_widget)
    login_widget.show()
    main_window = MainWindow()
    main_window.show()
    app.exec_()
