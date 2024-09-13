
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QSize, Qt, QCoreApplication
from PyQt5.QtWidgets import QLabel,QPushButton, QFrame, QTextEdit,QStackedWidget, QWidget,QListView,QSlider,QStatusBar,QMenuBar
from PyQt5.QtGui import QIcon, QPixmap
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 637)
        MainWindow.setFixedSize(QSize(1220, 637))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -30, 211, 631))
        self.label.setStyleSheet(u"background-color: rgb(227, 242, 253);\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 181, 41))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #E3F2FD; /* Very light blue shade */  \n"
"    color: rgb(14, 36, 51);\n"
"    border: none; /* No border */\n"
"    border-radius: 4px; /* Slightly rounded corners */\n"
"    padding: 10px 20px; /* Padding inside the button */\n"
"    font: 700 11pt \"Segoe UI\";\n"
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
"")
        icon = QIcon()
        
        icon.addFile(u"house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(270, 30, 941, 561))
        self.stackedWidget.setObjectName("stackedWidget")

        #widget one
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(270, 30, 941, 561))
        self.widget.setMinimumSize(QSize(941, 561))
        self.widget.setMaximumSize(QSize(941, 561))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"background-image: url(:njia_n6dh_161216.jpg);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-180, -20, 921, 551))
        self.label_2.setScaledContents(True)
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(90, 160, 811, 20))
        self.line.setStyleSheet(u"border-color: rgb(121, 157, 255);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(780, 40, 101, 91))
        self.label_3.setPixmap(QPixmap(u"../../../.designer/backup/freepik-export-20240703182022gjpK.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 30, 281, 51))
        self.label_4.setStyleSheet(u"font: 24px 700 italic 9pt \"Roboto\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 190, 281, 51))
        self.label_5.setStyleSheet(u"font: 18px 550 italic 7pt \"Roboto\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 190, 281, 51))
        self.label_6.setStyleSheet(u"font: 18px 550 italic 9pt \"Roboto\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(630, 190, 281, 51))
        self.label_7.setStyleSheet(u"font: 19px 550 italic 9pt \"Roboto\";")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 290, 281, 51))
        self.label_8.setStyleSheet(u"font: 18px 550 italic 7pt \"Roboto\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(350, 300, 281, 51))
        self.label_9.setStyleSheet(u"font: 18px 550 italic 7pt \"Roboto\";")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.widget)


        #widget two
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(270, 30, 941, 561))
        self.widget_2.setMaximumSize(QSize(951, 571))
        self.listView = QListView(self.widget_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(45, 51, 891, 481))
        self.listView.setStyleSheet(u"/* Basic QListView styling */\n"
"QListView {\n"
"    background: #FFFFFF; /* White background */\n"
"    border: 1px solid #DDDDDD; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px;\n"
"    font: 12pt \"Segoe UI\"; /* Font and size */\n"
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
"")
        self.verticalSlider = QSlider(self.widget_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(940, 30, 22, 581))
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_2 = QSlider(self.widget_2)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setGeometry(QRect(940, 40, 22, 521))
        self.verticalSlider_2.setStyleSheet(u"QSlider::groove:vertical {\n"
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
"")
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(110, 70, 631, 51))
        self.label_10.setStyleSheet(u"font:30px 700 9pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 215, 841, 301))
        self.label_11.setStyleSheet(u"font:16px 550 8pt \"Segoe UI\";")
        self.label_11.setScaledContents(True)
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(90, 170, 161, 20))
        self.label_12.setStyleSheet(u"font:12px italic 550 9pt \"Segoe UI\";")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(400, 170, 141, 16))
        self.label_13.setStyleSheet(u"font:12px italic 550 9pt \"Segoe UI\";")
        self.label_14 = QLabel(self.widget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(790, 70, 101, 91))
        self.label_14.setPixmap(QPixmap(u"freepik-export-202407041857042QgX.jpeg"))
        self.label_14.setScaledContents(True)
        self.label_15 = QLabel(self.widget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(660, 170, 141, 16))
        self.label_15.setStyleSheet(u"font:12px italic 550 9pt \"Segoe UI\";")
        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(794, 503, 131, 41))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
"    color: rgb(14, 36, 51); /* Text color */\n"
"    border: none; /* No border */\n"
"    border-radius: 4px; /* Slightly rounded corners */\n"
"    padding: 10px 20px; /* Padding inside the button */\n"
"    font: 700 11pt \"Segoe UI\"; /* Font settings */\n"
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
"")
        self.stackedWidget.addWidget(self.widget_2)


        #widget three
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(270, 30, 941, 561))
        self.frame = QFrame(self.widget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 30, 861, 481))
        self.frame.setStyleSheet(u"/* Basic QFrame styling */\n"
"QFrame {\n"
"    background: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */\n"
"    border: 1px solid #DDDDDD; /* Light grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 10px; /* Padding inside the frame */\n"
"    font: 12pt \"Segoe UI\"; /* Font and size */\n"
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
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(33, 410, 721, 51))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(80, 260, 151, 41))
        self.label_16.setStyleSheet(u"/* Basic QLabel styling for bubble chat */\n"
"QLabel {\n"
"    background-color: #E3F2FD; /* Light blue background */\n"
"    color: #0E2433; /* Dark text color */\n"
"    border: 1px solid #DDDDDD; /* Light grey border */\n"
"    border-radius: 15px; /* Rounded corners */\n"
"    padding: 10px 15px; /* Padding inside the label */\n"
"    font: 12pt \"Segoe UI\"; /* Font and size */\n"
"    position: relative; /* Required for positioning the tail */\n"
"}\n"
"\n"
"/* Tail styling using pseudo-element */\n"
"QLabel::before {\n"
"    content: \"\";\n"
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
"    content: \"\";\n"
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
"")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 260, 41, 41))
        self.label_17.setStyleSheet(u"/* Basic QLabel styling for circular user images */\n"
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
"    content: \" \";\n"
"    display: inline-block;\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    background-color: #BBDEFB; /* Light blue background for placeholder */\n"
"    border-radius: 50%; /* Circular frame */\n"
"}\n"
"")
        self.label_17.setPixmap(QPixmap(u"account_3033143.png"))
        self.label_17.setScaledContents(True)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(520, 310, 251, 41))
        self.label_18.setStyleSheet(u"/* Basic QLabel styling for bubble chat */\n"
"QLabel {\n"
"    background-color: #E3F2FD; /* Light blue background */\n"
"    color: #0E2433; /* Dark text color */\n"
"    border: 1px solid #DDDDDD; /* Light grey border */\n"
"    border-radius: 15px; /* Rounded corners */\n"
"    padding: 10px 15px; /* Padding inside the label */\n"
"    font: 12pt \"Segoe UI\"; /* Font and size */\n"
"    position: relative; /* Required for positioning the tail */\n"
"}\n"
"\n"
"/* Tail styling using pseudo-element */\n"
"QLabel::before {\n"
"    content: \"\";\n"
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
"    content: \"\";\n"
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
"")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(780, 310, 41, 41))
        self.label_19.setStyleSheet(u"/* Basic QLabel styling for circular user images */\n"
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
"    content: \" \";\n"
"    display: inline-block;\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    background-color: #BBDEFB; /* Light blue background for placeholder */\n"
"    border-radius: 50%; /* Circular frame */\n"
"}\n"
"")
        self.label_19.setPixmap(QPixmap(u"account_3033143.png"))
        self.label_19.setScaledContents(True)
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(770, 410, 71, 51))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
"    color: rgb(14, 36, 51); /* Text color */\n"
"    border: none; /* No border */\n"
"    border-radius: 4px; /* Slightly rounded corners */\n"
"    padding: 10px 20px; /* Padding inside the button */\n"
"    font: 700 11pt \"Segoe UI\"; /* Font settings */\n"
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
"")
        icon1 = QIcon()
        icon1.addFile(u"send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(50, 420, 51, 31))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
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
"")
        icon2 = QIcon()
        icon2.addFile(u"keyboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon2)
        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(650, 420, 41, 31))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
"    color: rgb(14, 36, 51); /* Text color */\n"
"    border: none; /* No border */\n"
"    border-radius: 4px; /* Slightly rounded corners */\n"
"    padding: 10px 20px; /* Padding inside the button */\n"
"    font: 700 11pt \"Segoe UI\"; /* Font settings */\n"
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
"")
        icon3 = QIcon()
        icon3.addFile(u"attachment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(700, 420, 41, 31))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    background: rgba(227, 242, 253, 0.8); /* Semi-transparent light blue with slight opacity */  \n"
"    color: rgb(14, 36, 51); /* Text color */\n"
"    border: none; /* No border */\n"
"    border-radius: 4px; /* Slightly rounded corners */\n"
"    padding: 10px 20px; /* Padding inside the button */\n"
"    font: 700 11pt \"Segoe UI\"; /* Font settings */\n"
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
"")
        icon4 = QIcon()
        icon4.addFile(u"camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1220, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"John Doe", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Faculty:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Level:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"eMail", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blog Heading ", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">jjkj</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
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
"", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Reading Time: 2 hour", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Created at: ", None))
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Created By: ", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Read More", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Abeg class dey?", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Go and Ask your grand father", None))
        self.label_19.setText("")
        self.pushButton_9.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"  Blogs", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"  Forums", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Profile", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"  GPT", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u" Support", None))
    # retranslateUi

    def setupConnections(self):
        self.pushButton_3.clicked.connect(self.show_widget_1)
        self.pushButton_2.clicked.connect(self.show_widget_2)
        self.pushButton_6.clicked.connect(self.show_widget_3)
    def show_widget_1(self):
        self.clear_stacked_widget()
        self.stackedWidget.setCurrentIndex(0)

    def show_widget_2(self):
        self.clear_stacked_widget()
        self.stackedWidget.setCurrentIndex(1)

    def show_widget_3(self):
        self.clear_stacked_widget()
        self.stackedWidget.setCurrentIndex(2)

    def clear_stacked_widget(self):
        current_widget = self.stackedWidget.currentWidget()
        for child in current_widget.children():
            if isinstance(child, QLabel):
                child.clear()