/********************************************************************************
** Form generated from reading UI file 'main windowHbusZD.ui'
**
** Created by: Qt User Interface Compiler version 6.7.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAIN_20_WINDOWHBUSZD_H
#define MAIN_20_WINDOWHBUSZD_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *label;
    QPushButton *pushButton;
    QWidget *widget;
    QLabel *label_2;
    QFrame *line;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QWidget *widget_2;
    QListView *listView;
    QSlider *verticalSlider;
    QSlider *verticalSlider_2;
    QLabel *label_10;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QPushButton *pushButton_10;
    QWidget *widget_3;
    QFrame *frame;
    QTextEdit *textEdit;
    QLabel *label_16;
    QLabel *label_17;
    QLabel *label_18;
    QLabel *label_19;
    QPushButton *pushButton_9;
    QPushButton *pushButton_11;
    QPushButton *pushButton_12;
    QPushButton *pushButton_13;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QPushButton *pushButton_8;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1220, 637);
        MainWindow->setMaximumSize(QSize(1220, 637));
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(241, 241, 241);"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(0, -30, 211, 631));
        label->setStyleSheet(QString::fromUtf8("background-color: rgb(227, 242, 253);\n"
""));
        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName("pushButton");
        pushButton->setGeometry(QRect(10, 20, 181, 41));
        pushButton->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon;
        icon.addFile(QString::fromUtf8("house.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon);
        widget = new QWidget(centralwidget);
        widget->setObjectName("widget");
        widget->setGeometry(QRect(270, 30, 941, 561));
        widget->setMinimumSize(QSize(941, 561));
        widget->setMaximumSize(QSize(941, 561));
        widget->setAutoFillBackground(false);
        widget->setStyleSheet(QString::fromUtf8("background-image: url(:/newPrefix/njia_n6dh_161216.jpg);"));
        label_2 = new QLabel(widget);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(-180, -20, 921, 551));
        label_2->setScaledContents(true);
        line = new QFrame(widget);
        line->setObjectName("line");
        line->setGeometry(QRect(90, 160, 811, 20));
        line->setStyleSheet(QString::fromUtf8("border-color: rgb(121, 157, 255);"));
        line->setFrameShape(QFrame::Shape::HLine);
        line->setFrameShadow(QFrame::Shadow::Sunken);
        label_3 = new QLabel(widget);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(780, 40, 101, 91));
        label_3->setPixmap(QPixmap(QString::fromUtf8("../../../.designer/backup/freepik-export-20240703182022gjpK.jpeg")));
        label_3->setScaledContents(true);
        label_4 = new QLabel(widget);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(70, 30, 281, 51));
        label_4->setStyleSheet(QString::fromUtf8("font: 24px 700 italic 9pt \"Roboto\";"));
        label_4->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_5 = new QLabel(widget);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(70, 190, 281, 51));
        label_5->setStyleSheet(QString::fromUtf8("font: 18px 550 italic 7pt \"Roboto\";"));
        label_5->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_6 = new QLabel(widget);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(360, 190, 281, 51));
        label_6->setStyleSheet(QString::fromUtf8("font: 18px 550 italic 9pt \"Roboto\";"));
        label_6->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_7 = new QLabel(widget);
        label_7->setObjectName("label_7");
        label_7->setGeometry(QRect(630, 190, 281, 51));
        label_7->setStyleSheet(QString::fromUtf8("font: 19px 550 italic 9pt \"Roboto\";"));
        label_7->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_8 = new QLabel(widget);
        label_8->setObjectName("label_8");
        label_8->setGeometry(QRect(70, 290, 281, 51));
        label_8->setStyleSheet(QString::fromUtf8("font: 18px 550 italic 7pt \"Roboto\";"));
        label_8->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_9 = new QLabel(widget);
        label_9->setObjectName("label_9");
        label_9->setGeometry(QRect(350, 300, 281, 51));
        label_9->setStyleSheet(QString::fromUtf8("font: 18px 550 italic 7pt \"Roboto\";"));
        label_9->setAlignment(Qt::AlignmentFlag::AlignCenter);
        widget_2 = new QWidget(widget);
        widget_2->setObjectName("widget_2");
        widget_2->setGeometry(QRect(-10, -30, 951, 571));
        widget_2->setMaximumSize(QSize(951, 571));
        listView = new QListView(widget_2);
        listView->setObjectName("listView");
        listView->setGeometry(QRect(45, 51, 891, 481));
        listView->setStyleSheet(QString::fromUtf8("/* Basic QListView styling */\n"
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
""));
        verticalSlider = new QSlider(widget_2);
        verticalSlider->setObjectName("verticalSlider");
        verticalSlider->setGeometry(QRect(940, 30, 22, 581));
        verticalSlider->setOrientation(Qt::Orientation::Vertical);
        verticalSlider_2 = new QSlider(widget_2);
        verticalSlider_2->setObjectName("verticalSlider_2");
        verticalSlider_2->setGeometry(QRect(940, 40, 22, 521));
        verticalSlider_2->setStyleSheet(QString::fromUtf8("QSlider::groove:vertical {\n"
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
""));
        verticalSlider_2->setOrientation(Qt::Orientation::Vertical);
        label_10 = new QLabel(widget_2);
        label_10->setObjectName("label_10");
        label_10->setGeometry(QRect(110, 70, 631, 51));
        label_10->setStyleSheet(QString::fromUtf8("font:30px 700 9pt \"Segoe UI\";"));
        label_10->setAlignment(Qt::AlignmentFlag::AlignCenter);
        label_11 = new QLabel(widget_2);
        label_11->setObjectName("label_11");
        label_11->setGeometry(QRect(80, 215, 841, 301));
        label_11->setStyleSheet(QString::fromUtf8("font:16px 550 8pt \"Segoe UI\";"));
        label_11->setScaledContents(true);
        label_12 = new QLabel(widget_2);
        label_12->setObjectName("label_12");
        label_12->setGeometry(QRect(90, 170, 161, 20));
        label_12->setStyleSheet(QString::fromUtf8("font:12px italic 550 9pt \"Segoe UI\";"));
        label_13 = new QLabel(widget_2);
        label_13->setObjectName("label_13");
        label_13->setGeometry(QRect(400, 170, 141, 16));
        label_13->setStyleSheet(QString::fromUtf8("font:12px italic 550 9pt \"Segoe UI\";"));
        label_14 = new QLabel(widget_2);
        label_14->setObjectName("label_14");
        label_14->setGeometry(QRect(790, 70, 101, 91));
        label_14->setPixmap(QPixmap(QString::fromUtf8("freepik-export-202407041857042QgX.jpeg")));
        label_14->setScaledContents(true);
        label_15 = new QLabel(widget_2);
        label_15->setObjectName("label_15");
        label_15->setGeometry(QRect(660, 170, 141, 16));
        label_15->setStyleSheet(QString::fromUtf8("font:12px italic 550 9pt \"Segoe UI\";"));
        pushButton_10 = new QPushButton(widget_2);
        pushButton_10->setObjectName("pushButton_10");
        pushButton_10->setGeometry(QRect(794, 503, 131, 41));
        pushButton_10->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        widget_3 = new QWidget(widget_2);
        widget_3->setObjectName("widget_3");
        widget_3->setGeometry(QRect(20, 40, 921, 541));
        frame = new QFrame(widget_3);
        frame->setObjectName("frame");
        frame->setGeometry(QRect(30, 30, 861, 481));
        frame->setStyleSheet(QString::fromUtf8("/* Basic QFrame styling */\n"
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
""));
        frame->setFrameShape(QFrame::Shape::StyledPanel);
        frame->setFrameShadow(QFrame::Shadow::Raised);
        textEdit = new QTextEdit(frame);
        textEdit->setObjectName("textEdit");
        textEdit->setGeometry(QRect(33, 410, 721, 51));
        label_16 = new QLabel(frame);
        label_16->setObjectName("label_16");
        label_16->setGeometry(QRect(80, 260, 151, 41));
        label_16->setStyleSheet(QString::fromUtf8("/* Basic QLabel styling for bubble chat */\n"
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
""));
        label_17 = new QLabel(frame);
        label_17->setObjectName("label_17");
        label_17->setGeometry(QRect(30, 260, 41, 41));
        label_17->setStyleSheet(QString::fromUtf8("/* Basic QLabel styling for circular user images */\n"
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
""));
        label_17->setPixmap(QPixmap(QString::fromUtf8("account_3033143.png")));
        label_17->setScaledContents(true);
        label_18 = new QLabel(frame);
        label_18->setObjectName("label_18");
        label_18->setGeometry(QRect(520, 310, 251, 41));
        label_18->setStyleSheet(QString::fromUtf8("/* Basic QLabel styling for bubble chat */\n"
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
""));
        label_19 = new QLabel(frame);
        label_19->setObjectName("label_19");
        label_19->setGeometry(QRect(780, 310, 41, 41));
        label_19->setStyleSheet(QString::fromUtf8("/* Basic QLabel styling for circular user images */\n"
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
""));
        label_19->setPixmap(QPixmap(QString::fromUtf8("account_3033143.png")));
        label_19->setScaledContents(true);
        pushButton_9 = new QPushButton(frame);
        pushButton_9->setObjectName("pushButton_9");
        pushButton_9->setGeometry(QRect(770, 410, 71, 51));
        pushButton_9->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8("send.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_9->setIcon(icon1);
        pushButton_11 = new QPushButton(frame);
        pushButton_11->setObjectName("pushButton_11");
        pushButton_11->setGeometry(QRect(50, 420, 51, 31));
        pushButton_11->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8("keyboard.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_11->setIcon(icon2);
        pushButton_12 = new QPushButton(frame);
        pushButton_12->setObjectName("pushButton_12");
        pushButton_12->setGeometry(QRect(650, 420, 41, 31));
        pushButton_12->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8("attachment.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_12->setIcon(icon3);
        pushButton_13 = new QPushButton(frame);
        pushButton_13->setObjectName("pushButton_13");
        pushButton_13->setGeometry(QRect(700, 420, 41, 31));
        pushButton_13->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8("camera.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_13->setIcon(icon4);
        pushButton_2 = new QPushButton(centralwidget);
        pushButton_2->setObjectName("pushButton_2");
        pushButton_2->setGeometry(QRect(10, 70, 181, 41));
        pushButton_2->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8("blogging.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_2->setIcon(icon5);
        pushButton_3 = new QPushButton(centralwidget);
        pushButton_3->setObjectName("pushButton_3");
        pushButton_3->setGeometry(QRect(10, 120, 181, 41));
        pushButton_3->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8("group.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_3->setIcon(icon6);
        pushButton_4 = new QPushButton(centralwidget);
        pushButton_4->setObjectName("pushButton_4");
        pushButton_4->setGeometry(QRect(0, 530, 211, 71));
        pushButton_4->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon7;
        icon7.addFile(QString::fromUtf8("logout.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_4->setIcon(icon7);
        pushButton_5 = new QPushButton(centralwidget);
        pushButton_5->setObjectName("pushButton_5");
        pushButton_5->setGeometry(QRect(10, 220, 181, 41));
        pushButton_5->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon8;
        icon8.addFile(QString::fromUtf8("settings.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_5->setIcon(icon8);
        pushButton_6 = new QPushButton(centralwidget);
        pushButton_6->setObjectName("pushButton_6");
        pushButton_6->setGeometry(QRect(10, 170, 181, 41));
        pushButton_6->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon9;
        icon9.addFile(QString::fromUtf8("user.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_6->setIcon(icon9);
        pushButton_7 = new QPushButton(centralwidget);
        pushButton_7->setObjectName("pushButton_7");
        pushButton_7->setGeometry(QRect(10, 270, 181, 41));
        pushButton_7->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon10;
        icon10.addFile(QString::fromUtf8("chat-gpt.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_7->setIcon(icon10);
        pushButton_8 = new QPushButton(centralwidget);
        pushButton_8->setObjectName("pushButton_8");
        pushButton_8->setGeometry(QRect(10, 320, 181, 41));
        pushButton_8->setStyleSheet(QString::fromUtf8("QPushButton {\n"
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
""));
        QIcon icon11;
        icon11.addFile(QString::fromUtf8("technical-support.png"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton_8->setIcon(icon11);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 1220, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QString());
        pushButton->setText(QCoreApplication::translate("MainWindow", " Home", nullptr));
        label_2->setText(QString());
        label_3->setText(QString());
        label_4->setText(QCoreApplication::translate("MainWindow", "John Doe", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Faculty:", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Department:", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Level:", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "eMail", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Phone Number", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "Blog Heading ", nullptr));
#if QT_CONFIG(tooltip)
        label_11->setToolTip(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"justify\">jjkj</p></body></html>", nullptr));
#endif // QT_CONFIG(tooltip)
        label_11->setText(QCoreApplication::translate("MainWindow", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
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
"", nullptr));
        label_12->setText(QCoreApplication::translate("MainWindow", "Reading Time: 2 hour", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "Created at: ", nullptr));
        label_14->setText(QString());
        label_15->setText(QCoreApplication::translate("MainWindow", "Created By: ", nullptr));
        pushButton_10->setText(QCoreApplication::translate("MainWindow", "Read More", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "Abeg class dey?", nullptr));
        label_17->setText(QString());
        label_18->setText(QCoreApplication::translate("MainWindow", "Go and Ask your grand father", nullptr));
        label_19->setText(QString());
        pushButton_9->setText(QString());
        pushButton_11->setText(QString());
        pushButton_12->setText(QString());
        pushButton_13->setText(QString());
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "  Blogs", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "  Forums", nullptr));
        pushButton_4->setText(QCoreApplication::translate("MainWindow", "Sign out", nullptr));
        pushButton_5->setText(QCoreApplication::translate("MainWindow", " Settings", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", " Profile", nullptr));
        pushButton_7->setText(QCoreApplication::translate("MainWindow", "  GPT", nullptr));
        pushButton_8->setText(QCoreApplication::translate("MainWindow", " Support", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAIN_20_WINDOWHBUSZD_H
