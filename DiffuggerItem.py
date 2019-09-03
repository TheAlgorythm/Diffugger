from PyQt5.QtWidgets import QWidget, QLineEdit
from UI.DiffuggerItem import ui_DiffuggerItemWidget
from ItemParent import ItemParent


class DiffuggerItem(QWidget):

    def __init__(self, parent):
        super().__init__()
        if not isinstance(parent, ItemParent):
            raise TypeError("Parent is no ItemParent")
        self.parent = parent
        self.ui = ui_DiffuggerItemWidget()
        self.ui.setupUi(self)
        self.ui.closeButton.clicked.connect(self.closeItem)
        self.ui.value1LineEdit.textChanged.connect(self.textChanged)
        self.ui.value2LineEdit.textChanged.connect(self.textChanged)
        self.ui.passwordAction.changed.connect(self.pwdActionChanged)
        self.ui.value1ShowAction.changed.connect(self.value1ShowActionChanged)
        self.ui.value2ShowAction.changed.connect(self.value2ShowActionChanged)
        self.textChanged()
    
    def closeItem(self):
        self.parent.closeItem(self)

    def compare(self, value1, value2):
        return value1 == value2

    def textChanged(self):
        diff = self.compare(self.ui.value1LineEdit.text(), self.ui.value2LineEdit.text())
        if diff:
            self.ui.diffButton.setStyleSheet("QPushButton {background-color: #03d903; border: 1px solid black; border-radius: 5px;}")
        else:
            self.ui.diffButton.setStyleSheet("QPushButton {background-color: #d90303; border: 1px solid black; border-radius: 5px;}")

    def pwdActionChanged(self):
        value = self.ui.passwordAction.isChecked()
        echoMode = QLineEdit.EchoMode.Normal
        if value:
            echoMode = QLineEdit.EchoMode.Password
        self.ui.value1ShowAction.setVisible(value)
        self.ui.value2ShowAction.setVisible(value)
        self.ui.value1LineEdit.setEchoMode(echoMode)
        self.ui.value2LineEdit.setEchoMode(echoMode)

    def value1ShowActionChanged(self):
        value = self.ui.value1ShowAction.isChecked()
        echoMode = QLineEdit.EchoMode.Normal
        if not value:
            echoMode = QLineEdit.EchoMode.Password
        self.ui.value1LineEdit.setEchoMode(echoMode)

    def value2ShowActionChanged(self):
        value = self.ui.value2ShowAction.isChecked()
        echoMode = QLineEdit.EchoMode.Normal
        if not value:
            echoMode = QLineEdit.EchoMode.Password
        self.ui.value2LineEdit.setEchoMode(echoMode)
