from PyQt5.QtWidgets import QWidget, QLineEdit
from UI.DiffuggerItem import ui_DiffuggerItemWidget
from ItemParent import ItemParent
from DataItem import DataItem


class DiffuggerItem(QWidget):

    def __init__(self, parent):
        super().__init__()
        if not isinstance(parent, ItemParent):
            raise TypeError("Parent is no ItemParent")
        self.parent = parent
        self.data = DataItem()
        self.setupUi()

    def setupUi(self):
        if hasattr(self, 'ui'):
            return
        self.ui = ui_DiffuggerItemWidget()
        self.ui.setupUi(self)
        self.ui.closeButton.clicked.connect(self.closeItem)
        self.ui.value1LineEdit.textChanged.connect(self.textChanged)
        self.ui.value2LineEdit.textChanged.connect(self.textChanged)
        self.ui.passwordAction.changed.connect(self.pwdActionChanged)
        self.ui.value1ShowAction.changed.connect(self.value1ShowActionChanged)
        self.ui.value2ShowAction.changed.connect(self.value2ShowActionChanged)
        self.ui.nameLineEdit.textChanged.connect(self.nameChanged)
        self.ui.diffButton.clicked.connect(self.diffButtonClicked)
        self.textChanged()

    def closeItem(self):
        self.parent.closeItem(self)

    def compare(self, value1, value2):
        return value1 == value2

    def textChanged(self):
        self.data.value1 = self.ui.value1LineEdit.text()
        self.data.value2 = self.ui.value2LineEdit.text()
        diff = self.compare(self.data.value1, self.data.value2)
        if diff:
            self.ui.diffButton.setStyleSheet("QPushButton {background-color: #03d903; border: 1px solid black; border-radius: 5px;}")
        else:
            self.ui.diffButton.setStyleSheet("QPushButton {background-color: #d90303; border: 1px solid black; border-radius: 5px;}")

    def nameChanged(self):
        self.data.name = self.ui.nameLineEdit.text()

    def pwdActionChanged(self):
        value = self.ui.passwordAction.isChecked()
        echoMode = QLineEdit.EchoMode.Normal
        self.data.type &= ~DataItem.ValueType.PASSWORD
        if value:
            echoMode = QLineEdit.EchoMode.Password
            self.data.type |= DataItem.ValueType.PASSWORD
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

    def diffButtonClicked(self):
        # TODO show Diff-Dialog
        pass
