

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import Userui

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    TextField {
        id: textField
        x: 241
        y: 328
        width: 258
        height: 56
        text: qsTr("")
        placeholderTextColor: "#4c120101"
        placeholderText: qsTr("password")

        background: Rectangle {
            color: "transparent" // Make the background transparent

            // Bottom border
            Rectangle {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                height: 2 // Change to desired border width
                color: "black" // Change to desired border color
            }
        }
    }

    TextField {
        id: textField1
        x: 241
        y: 266
        width: 251
        height: 56
        visible: true
        clip: true
        placeholderText: qsTr("user name or matric number")
    }

    Button {
        id: button
        x: 313
        y: 404
        width: 135
        height: 52
        text: qsTr("login")
        flat: true
        checkable: true
    }

    Image {
        id: image
        x: 300
        y: 106
        width: 100
        height: 100
        source: "qrc:/qtquickplugin/images/template_image.png"
        fillMode: Image.PreserveAspectFit
    }
}
