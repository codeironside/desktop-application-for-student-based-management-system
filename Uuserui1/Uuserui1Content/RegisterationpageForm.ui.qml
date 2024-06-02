

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15
import Uuserui1 1.0

Item {
    width: Constants.width
    height: Constants.height
    visible: true

    property alias button: button

    Button {
        id: button
        x: 676
        y: 416
        text: qsTr("Button")
    }

    TextField {
        id: textField
        x: 130
        y: 192
        placeholderText: qsTr("Text Field")
    }

    TextField {
        id: textField1
        x: 138
        y: 102
        placeholderText: qsTr("first Name")
    }

    TextField {
        id: textField2
        x: 130
        y: 192
        placeholderText: qsTr("level")
    }

    TextField {
        id: textField3
        x: 618
        y: 318
        placeholderText: qsTr("Text Field")
    }

    TextField {
        id: textField4
        x: 138
        y: 310
        placeholderText: qsTr("Text Field")
    }

    TextField {
        id: textField5
        x: 618
        y: 192
        placeholderText: qsTr("Text Field")
    }

    TextField {
        id: textField6
        x: 618
        y: 102
        width: 120
        height: 52
        placeholderText: qsTr("Last Name")
    }

    Text {
        id: text1
        x: 348
        y: 84
        text: qsTr("Basic information")
        font.pixelSize: 12
    }
}
