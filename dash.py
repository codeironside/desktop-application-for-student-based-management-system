from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QFrame,
    QTextEdit,
    QStackedWidget,
    QWidget,
    QListView,
    QSlider,
    QStatusBar,
    QMenuBar,
)
from PyQt5.QtGui import QIcon, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 637)
        MainWindow.setFixedSize(QSize(1220, 637))  # Set fixed size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, -30, 211, 631))
        self.label.setStyleSheet("background-color: rgb(227, 242, 253);\n" "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1220, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(270, 30, 941, 561))
        self.stackedWidget.setObjectName("stackedWidget")

        # Create the widgets
        self.create_widgets()

        # Set widget_2 as the default displayed widget
        self.stackedWidget.setCurrentIndex(2)

        # Buttons to switch between widgets
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 181, 41))
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon = QIcon()

        icon.addFile("house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 70, 181, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon5 = QIcon()
        icon5.addFile("blogging.png", QSize(), QIcon.Normal, QIcon.Off)

        # push buttons

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 120, 181, 41))
        self.pushButton_3.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon6 = QIcon()
        icon6.addFile("group.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 530, 211, 71))
        self.pushButton_4.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-top: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon7 = QIcon()
        icon7.addFile("logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 220, 181, 41))
        self.pushButton_5.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon8 = QIcon()
        icon8.addFile("settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 170, 181, 41))
        self.pushButton_6.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon9 = QIcon()
        icon9.addFile("user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.stackedWidget.addWidget(self.widget_2)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 270, 181, 41))
        self.pushButton_7.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon10 = QIcon()
        icon10.addFile("chat-gpt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 320, 181, 41))
        self.pushButton_8.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #E3F2FD; /* Very light blue shade */  \n"
            "    color: rgb(14, 36, 51);\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI";\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #BBDEFB; /* Darker light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #90CAF9; /* Even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background-color: #E3F2FD; /* Very light blue background for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon11 = QIcon()
        icon11.addFile("technical-support.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon11)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("campulse", "MainWindow"))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", " Home", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", "John Doe", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Faculty:", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Department:", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Level:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", "eMail", None))
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "Phone Number", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Blog Heading ", None)
        )
        # if QT_CONFIG(tooltip)
        self.label_11.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="justify">jjkj</p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibu"
                "s, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariat"
                "ur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Pra"
                "esent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod "
                "gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisqu"
                "e rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, conseq"
                "uat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cill"
                "um dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitas"
                "se platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. In"
                "teger in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla"
                " ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, a"
                "liquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehende"
                "rit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, "
                "feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
                "\n"
                "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus mag"
                "na felis sollicitudin mauris. Integer in mauris eu nibh euismod gravida. Duis ac tellus et risus vulputate vehicula. Donec lobortis risus a elit. Etiam tempor. Ut ullamcorper, ligula eu tempor congue, eros est euismod turpis, id tincidunt sapien risus a quam. Maecenas fermentum consequat mi. Donec fermentum. Pellentesque malesuada nulla a mi. Duis sapien sem, aliquet nec, commodo eget, consequat quis, neque. Aliquam faucibus, elit ut dictum aliquet, felis nisl adipiscing sapien, sed malesuada diam lacus eget erat. Cras mollis scelerisque nunc. Nullam arcu. Aliquam consequat. Curabitur augue lorem, dapibus quis, laoreet et, pretium ac, nisi. Aenean magna nisl, mollis quis, molestie eu, feugiat in, orci. In hac habitasse platea dictumst.\n"
                "\n"
                "Praesent id justo in neque elementum ultrices. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a,"
                " tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet.\n"
                "",
                None,
            )
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", "Reading Time: 2 hour", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Created at: ", None)
        )
        self.label_14.setText("")
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Created By: ", None)
        )
        self.pushButton_10.setText(
            QCoreApplication.translate("MainWindow", "Read More", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Abeg class dey?", None)
        )
        self.label_17.setText("")
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow", "Go and Ask your grand father", None
            )
        )
        self.label_19.setText("")
        self.pushButton_9.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "  Blogs", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", "  Forums", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", "Sign out", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", " Settings", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", " Profile", None)
        )
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", "  GPT", None)
        )
        self.pushButton_8.setText(
            QCoreApplication.translate("MainWindow", " Support", None)
        )

    def setupConnections(self):
        self.pushButton_2.clicked.connect(lambda: self.switch_widget(2))
        self.pushButton_3.clicked.connect(lambda: self.switch_widget(1))
        self.pushButton_5.clicked.connect(lambda: self.switch_widget(0))

    def create_widgets(self):
        # First widget
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(270, 30, 941, 561))
        self.widget.setMinimumSize(QSize(941, 561))
        self.widget.setMaximumSize(QSize(941, 561))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-image: url(:njia_n6dh_161216.jpg);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(-180, -20, 921, 551))
        self.label_2.setScaledContents(True)
        self.line = QFrame(self.widget)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(90, 160, 811, 20))
        self.line.setStyleSheet("border-color: rgb(121, 157, 255);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(780, 40, 101, 91))
        self.label_3.setPixmap(
            QPixmap("../../../.designer/backup/freepik-export-20240703182022gjpK.jpeg")
        )
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(70, 30, 281, 51))
        self.label_4.setStyleSheet('font: 24px 700 italic 9pt "Roboto";')
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(70, 190, 281, 51))
        self.label_5.setStyleSheet('font: 18px 550 italic 7pt "Roboto";')
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(360, 190, 281, 51))
        self.label_6.setStyleSheet('font: 18px 550 italic 9pt "Roboto";')
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(630, 190, 281, 51))
        self.label_7.setStyleSheet('font: 19px 550 italic 9pt "Roboto";')
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(70, 290, 281, 51))
        self.label_8.setStyleSheet('font: 18px 550 italic 7pt "Roboto";')
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(350, 300, 281, 51))
        self.label_9.setStyleSheet('font: 18px 550 italic 7pt "Roboto";')
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.widget)

        # Second widget (default)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(270, 30, 941, 561))
        self.widget_2.setMaximumSize(QSize(951, 571))
        self.listView = QListView(self.widget_2)
        self.listView.setObjectName("listView")
        self.listView.setGeometry(QRect(45, 51, 891, 481))
        self.listView.setStyleSheet(
            "/* Basic QListView styling */\n"
            "QListView {\n"
            "    background: #FFFFFF; /* White background */\n"
            "    border: 1px solid #DDDDDD; /* Light grey border */\n"
            "    border-radius: 5px; /* Rounded corners */\n"
            "    padding: 5px;\n"
            '    font: 12pt "Segoe UI"; /* Font and size */\n'
            "}\n"
            "\n"
            "/* Style for the items */\n"
            "QListView::item {\n"
            "    background: #FFFFFF; /* White background */\n"
            "    color: #0E2433; /* Dark text color */\n"
            "    padding: 10px; /* Padding for each item */\n"
            "    margin: 5px 0; /* Margin between items */\n"
            "    border: 1px solid #E0E0E0; /* Light grey border */\n"
            "    border-radius: 3px; /* Rounded corners */\n"
            "}\n"
            "\n"
            "/* Hover state for items */\n"
            "QListView::item:hover {\n"
            "    background: #F1F1F1; /* Light grey background on hover */\n"
            "    border: 1px solid #CCCCCC; /* Slightly darker grey border on hover */\n"
            "}\n"
            "\n"
            "/* Selected state for items */\n"
            "QListView::item:selected {\n"
            "    background: #BBDEFB; /* Light blue background for selected items */\n"
            ""
            "    color: white; /* White text for selected items */\n"
            "    border: 1px solid #BBDEFB; /* Border matches background */\n"
            "}\n"
            "\n"
            "/* Highlight selected text color */\n"
            "QListView::item:selected:!active {\n"
            "    color: #FFFFFF; /* White text color for inactive selected items */\n"
            "}\n"
            "\n"
            "/* Subtle shadow effect */\n"
            "QListView::item {\n"
            "    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */\n"
            "}\n"
            ""
        )
        self.verticalSlider = QSlider(self.widget_2)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setGeometry(QRect(940, 30, 22, 581))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_2 = QSlider(self.widget_2)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.setGeometry(QRect(940, 40, 22, 521))
        self.verticalSlider_2.setStyleSheet(
            "QSlider::groove:vertical {\n"
            "    background: #E0E0E0; /* Light grey */\n"
            "    width: 6px;\n"
            "    border-radius: 3px;\n"
            "}\n"
            "\n"
            "QSlider::handle:vertical {\n"
            "    background: #6200EE; /* Primary color */\n"
            "    border: 1px solid #6200EE; /* Darker primary color for border */\n"
            "    height: 20px;\n"
            "    width: 20px;\n"
            "    margin: -7px 0; /* Center the handle */\n"
            "    border-radius: 10px;\n"
            "    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QSlider::handle:vertical:hover {\n"
            "    background: #3700B3; /* Darker primary color on hover */\n"
            "}\n"
            "\n"
            "QSlider::add-page:vertical {\n"
            "    background: #E0E0E0; /* Light grey */\n"
            "}\n"
            "\n"
            "QSlider::sub-page:vertical {\n"
            "    background: #6200EE; /* Primary color */\n"
            "    border-radius: 3px;\n"
            "}\n"
            ""
        )
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(110, 70, 631, 51))
        self.label_10.setStyleSheet('font:30px 700 9pt "Segoe UI";')
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(80, 215, 841, 301))
        self.label_11.setStyleSheet('font:16px 550 8pt "Segoe UI";')
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.label_12.setGeometry(QRect(90, 170, 161, 20))
        self.label_12.setStyleSheet('font:12px italic 550 9pt "Segoe UI";')
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName("label_13")
        self.label_13.setGeometry(QRect(400, 170, 141, 16))
        self.label_13.setStyleSheet('font:12px italic 550 9pt "Segoe UI";')
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName("label_14")
        self.label_14.setGeometry(QRect(790, 70, 101, 91))
        self.label_14.setPixmap(QPixmap("freepik-export-202407041857042QgX.jpeg"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName("label_15")
        self.label_15.setGeometry(QRect(660, 170, 141, 16))
        self.label_15.setStyleSheet('font:12px italic 550 9pt "Segoe UI";')
        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setGeometry(QRect(794, 503, 131, 41))
        self.pushButton_10.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
            "    color: rgb(14, 36, 51); /* Text color */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI"; /* Font settings */\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Semi-transparent light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgba(144, 202, 249, 0.8); /* Semi-transparent even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background: rgba(227, 242, 253, 0.5); /* Semi-transparent light"
            " blue for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        self.stackedWidget.addWidget(self.widget_2)

        # Third widget
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setGeometry(QRect(270, 30, 941, 561))
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(30, 30, 861, 481))
        self.frame.setStyleSheet(
            "/* Basic QFrame styling */\n"
            "QFrame {\n"
            "    background: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */\n"
            "    border: 1px solid #DDDDDD; /* Light grey border */\n"
            "    border-radius: 5px; /* Rounded corners */\n"
            "    padding: 10px; /* Padding inside the frame */\n"
            '    font: 12pt "Segoe UI"; /* Font and size */\n'
            "    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "/* Style for the items */\n"
            "QFrame::item {\n"
            "    background: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */\n"
            "    color: #0E2433; /* Dark text color */\n"
            "    padding: 10px; /* Padding for each item */\n"
            "    margin: 5px 0; /* Margin between items */\n"
            "    border: 1px solid #E0E0E0; /* Light grey border */\n"
            "    border-radius: 3px; /* Rounded corners */\n"
            "}\n"
            "\n"
            "/* Hover state for items */\n"
            "QFrame::item:hover {\n"
            "    background: rgba(241, 241, 241, 0.8); /* Light grey background on hover */\n"
            "    border: 1px solid #CCCCCC; /* Slightly darker grey"
            " border on hover */\n"
            "}\n"
            "\n"
            "/* Selected state for items */\n"
            "QFrame::item:selected {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Light blue background for selected items */\n"
            "    color: white; /* White text for selected items */\n"
            "    border: 1px solid rgba(187, 222, 251, 0.8); /* Border matches background */\n"
            "}\n"
            "\n"
            "/* Highlight selected text color */\n"
            "QFrame::item:selected:!active {\n"
            "    color: #FFFFFF; /* White text color for inactive selected items */\n"
            "}\n"
            "\n"
            "/* Subtle shadow effect */\n"
            "QFrame::item {\n"
            "    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow */\n"
            "}\n"
            ""
        )
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setGeometry(QRect(33, 410, 721, 51))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.label_16.setGeometry(QRect(80, 260, 151, 41))
        self.label_16.setStyleSheet(
            "/* Basic QLabel styling for bubble chat */\n"
            "QLabel {\n"
            "    background-color: #E3F2FD; /* Light blue background */\n"
            "    color: #0E2433; /* Dark text color */\n"
            "    border: 1px solid #DDDDDD; /* Light grey border */\n"
            "    border-radius: 15px; /* Rounded corners */\n"
            "    padding: 10px 15px; /* Padding inside the label */\n"
            '    font: 12pt "Segoe UI"; /* Font and size */\n'
            "    position: relative; /* Required for positioning the tail */\n"
            "}\n"
            "\n"
            "/* Tail styling using pseudo-element */\n"
            "QLabel::before {\n"
            '    content: "";\n'
            "    position: absolute;\n"
            "    bottom: 10px; /* Adjust this to move the tail vertically */\n"
            "    left: -10px; /* Position the tail on the left side */\n"
            "    width: 0;\n"
            "    height: 0;\n"
            "    border: 10px solid transparent;\n"
            "    border-top-color: #E3F2FD; /* Same color as the background */\n"
            "    border-left: 0;\n"
            "    border-right: 0;\n"
            "    margin-top: -10px;\n"
            "}\n"
            "\n"
            "/* Alternative tail styling for the right side (if needed) */\n"
            "/*\n"
            "QL"
            "abel::after {\n"
            '    content: "";\n'
            "    position: absolute;\n"
            "    bottom: 10px; \n"
            "    right: -10px; \n"
            "    width: 0;\n"
            "    height: 0;\n"
            "    border: 10px solid transparent;\n"
            "    border-top-color: #E3F2FD;\n"
            "    border-left: 0;\n"
            "    border-right: 0;\n"
            "    margin-top: -10px;\n"
            "}\n"
            "*/\n"
            ""
        )
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(30, 260, 41, 41))
        self.label_17.setStyleSheet(
            "/* Basic QLabel styling for circular user images */\n"
            "QLabel {\n"
            "    border: 2px solid #BBDEFB; /* Light blue border */\n"
            "    border-radius: 50%; /* Circular frame */\n"
            "    width: 50px; /* Fixed width */\n"
            "    height: 50px; /* Fixed height */\n"
            "    background-color: #E3F2FD; /* Light blue background */\n"
            "    padding: 5px; /* Padding inside the label */\n"
            "}\n"
            "\n"
            "/* Placeholder for when there is no image */\n"
            "QLabel::before {\n"
            '    content: " ";\n'
            "    display: inline-block;\n"
            "    width: 100%;\n"
            "    height: 100%;\n"
            "    background-color: #BBDEFB; /* Light blue background for placeholder */\n"
            "    border-radius: 50%; /* Circular frame */\n"
            "}\n"
            ""
        )
        self.label_17.setPixmap(QPixmap("account_3033143.png"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName("label_18")
        self.label_18.setGeometry(QRect(520, 310, 251, 41))
        self.label_18.setStyleSheet(
            "/* Basic QLabel styling for bubble chat */\n"
            "QLabel {\n"
            "    background-color: #E3F2FD; /* Light blue background */\n"
            "    color: #0E2433; /* Dark text color */\n"
            "    border: 1px solid #DDDDDD; /* Light grey border */\n"
            "    border-radius: 15px; /* Rounded corners */\n"
            "    padding: 10px 15px; /* Padding inside the label */\n"
            '    font: 12pt "Segoe UI"; /* Font and size */\n'
            "    position: relative; /* Required for positioning the tail */\n"
            "}\n"
            "\n"
            "/* Tail styling using pseudo-element */\n"
            "QLabel::before {\n"
            '    content: "";\n'
            "    position: absolute;\n"
            "    bottom: 10px; /* Adjust this to move the tail vertically */\n"
            "    left: -10px; /* Position the tail on the left side */\n"
            "    width: 0;\n"
            "    height: 0;\n"
            "    border: 10px solid transparent;\n"
            "    border-top-color: #E3F2FD; /* Same color as the background */\n"
            "    border-left: 0;\n"
            "    border-right: 0;\n"
            "    margin-top: -10px;\n"
            "}\n"
            "\n"
            "/* Alternative tail styling for the right side (if needed) */\n"
            "/*\n"
            "QL"
            "abel::after {\n"
            '    content: "";\n'
            "    position: absolute;\n"
            "    bottom: 10px; \n"
            "    right: -10px; \n"
            "    width: 0;\n"
            "    height: 0;\n"
            "    border: 10px solid transparent;\n"
            "    border-top-color: #E3F2FD;\n"
            "    border-left: 0;\n"
            "    border-right: 0;\n"
            "    margin-top: -10px;\n"
            "}\n"
            "*/\n"
            ""
        )
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.label_19.setGeometry(QRect(780, 310, 41, 41))
        self.label_19.setStyleSheet(
            "/* Basic QLabel styling for circular user images */\n"
            "QLabel {\n"
            "    border: 2px solid #BBDEFB; /* Light blue border */\n"
            "    border-radius: 50%; /* Circular frame */\n"
            "    width: 50px; /* Fixed width */\n"
            "    height: 50px; /* Fixed height */\n"
            "    background-color: #E3F2FD; /* Light blue background */\n"
            "    padding: 5px; /* Padding inside the label */\n"
            "}\n"
            "\n"
            "/* Placeholder for when there is no image */\n"
            "QLabel::before {\n"
            '    content: " ";\n'
            "    display: inline-block;\n"
            "    width: 100%;\n"
            "    height: 100%;\n"
            "    background-color: #BBDEFB; /* Light blue background for placeholder */\n"
            "    border-radius: 50%; /* Circular frame */\n"
            "}\n"
            ""
        )
        self.label_19.setPixmap(QPixmap("account_3033143.png"))
        self.label_19.setScaledContents(True)
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setGeometry(QRect(770, 410, 71, 51))
        self.pushButton_9.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
            "    color: rgb(14, 36, 51); /* Text color */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI"; /* Font settings */\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Semi-transparent light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgba(144, 202, 249, 0.8); /* Semi-transparent even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background: rgba(227, 242, 253, 0.5); /* Semi-transparent light"
            " blue for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon1 = QIcon()
        icon1.addFile("send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setGeometry(QRect(50, 420, 51, 31))
        self.pushButton_11.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
            "    color: rgb(14, 36, 51); /* Text color */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Semi-transparent light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgba(144, 202, 249, 0.8); /* Semi-transparent even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background: rgba(227, 242, 253, 0.5); /* Semi-transparent light blue for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon2 = QIcon()
        icon2.addFile("keyboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setGeometry(QRect(650, 420, 41, 31))
        self.pushButton_12.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
            "    color: rgb(14, 36, 51); /* Text color */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI"; /* Font settings */\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Semi-transparent light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgba(144, 202, 249, 0.8); /* Semi-transparent even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background: rgba(227, 242, 253, 0.5); /* Semi-transparent light"
            " blue for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon3 = QIcon()
        icon3.addFile("attachment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setGeometry(QRect(700, 420, 41, 31))
        self.pushButton_13.setStyleSheet(
            "QPushButton {\n"
            "    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
            "    color: rgb(14, 36, 51); /* Text color */\n"
            "    border: none; /* No border */\n"
            "    border-radius: 4px; /* Slightly rounded corners */\n"
            "    padding: 10px 20px; /* Padding inside the button */\n"
            '    font: 700 11pt "Segoe UI"; /* Font settings */\n'
            "    box-shadow: 0px 2px 2px rgba(0, 2, 0, 0.5); /* Subtle shadow */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background: rgba(187, 222, 251, 0.8); /* Semi-transparent light blue shade on hover */\n"
            "    color: rgb(14, 36, 51); /* Change text color on hover */\n"
            "    border-right: 2px solid black; /* Make the right side thicker */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background: rgba(144, 202, 249, 0.8); /* Semi-transparent even darker light blue when pressed */\n"
            "    box-shadow: none; /* Remove shadow on press */\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "    background: rgba(227, 242, 253, 0.5); /* Semi-transparent light"
            " blue for disabled state */\n"
            "    color: #BCAAA4; /* Light blue text for disabled state */\n"
            "}\n"
            ""
        )
        icon4 = QIcon()
        icon4.addFile("camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.stackedWidget.addWidget(self.widget_3)

    def switch_widget(self, index):
        # Clear the current widget
        # current_widget = self.stackedWidget.currentWidget()
        # for child in current_widget.findChildren(QLabel):
        #     child.clear()

        # Switch to the new widget
        self.stackedWidget.setCurrentIndex(index)
