
/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import Uuserui1
import QtQuick.Studio.DesignEffects

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor
    property alias buttonText: button.text

    TextField {
        id: textField
        x: 549
        y: 247
        width: 199
        height: 56
        selectionColor: "#FF725E"
        placeholderTextColor: "#110f10"
        placeholderText: "user name/matric_no"
        hoverEnabled: true
        transformOrigin: Item.Center
        property int newName: 0

        background: Rectangle {
            color: "transparent" // Make the background transparent

            // Bottom border
            Rectangle {
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                height: 2 // Change to desired border width
                color: "#f9a460ae" // Change to desired border color
            }
        }
        DesignEffect {
            visible: true
            effects: [
                DesignDropShadow {}
            ]
        }
    }

    TextField {
        id: textField1
        x: 554
        y: 324
        width: 199
        height: 56
        text: ""
        selectionColor: "FF725E"
        layer.effect: textField1
        renderType: Text.NativeRendering
        hoverEnabled: true
        placeholderTextColor: "#110f10"
        maximumLength: 30
        echoMode: TextInput.Password
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

        DesignEffect {
            visible: true
            effects: [
                DesignDropShadow {}
            ]
        }
    }

    Button {
        id: button
        x: 599
        y: 395
        visible: true
        text: "login"
        icon.source: "../Uuserui1/login_5188211.png"
        property url newName: "../Uuserui1/Exams-cuate.png"
        display: AbstractButton.TextBesideIcon
        flat: true
    }

    DesignEffect {
        effects: [
            DesignInnerShadow {}
        ]
    }

    // Modify the image1 component to have rounded borders
    Rectangle {
        id: imageContainer
        x: 599
        y: 119
        width: 100
        height: 100
        radius: 100 // Change to the desired corner radius
        clip: true

        Image {
            id: image1
            anchors.fill: parent
            source: "../Uuserui1/account_3033143.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Text {
        id: text1
        x: 8
        y: 528
        width: 884
        height: 72
        text: "copy right of group tobi 2024 @"
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.styleName: "Bold Italic"
        font.capitalization: Font.Capitalize
    }

    Text {
        id: text2
        x: 21
        y: 395
        width: 444
        height: 32
        text: qsTr("\"Stay Informed, Stay Connected: Your One-Stop Student Management System\"")
        font.pixelSize: 14
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        wrapMode: Text.WordWrap
        font.styleName: "Semibold Italic"
    }

    Button {
        id: button1
        x: 676
        y: 453
        text: qsTr("forgot password?")
        icon.source: "../Uuserui1/forgot-password_5188606.png"
        flat: true
    }

    AnimatedImage {
        id: animatedImage
        x: 42
        y: 101
        width: 423
        height: 248
        source: "../Uuserui1/college students-bro.svg"
        speed: 2
        playing: true
    }

    ToolSeparator {
        id: toolSeparator
        x: 481
        y: 101
        width: 25
        height: 404
    }

    Button {
        id: button2
        x: 517
        y: 453
        text: qsTr("New? Register")
        icon.source: "../Uuserui1/user-avatar_6380179.png"
        icon.cache: false
        flat: true
    }
}
