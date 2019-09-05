from PyQt5 import QtWidgets, QtGui
from Icons import Icons
from IconButton import IconButton


class ui_DiffuggerItemWidget:

    def setupUi(self, widget):
        self.mainLayout = QtWidgets.QHBoxLayout(widget)

        # TODO min/max of QLineEdits

        self.nameLineEdit = QtWidgets.QLineEdit()
        self.nameLineEdit.setMinimumWidth(60)
        self.passwordAction = self.nameLineEdit.addAction(QtGui.QIcon(Icons.getPwdField()), QtWidgets.QLineEdit.ActionPosition.TrailingPosition)
        self.passwordAction.setCheckable(True)
        self.mainLayout.addWidget(self.nameLineEdit)

        self.nameSpacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.mainLayout.addSpacerItem(self.nameSpacer)

        self.value1LineEdit = QtWidgets.QLineEdit()
        self.value1ShowAction = self.value1LineEdit.addAction(QtGui.QIcon(Icons.getEye()), QtWidgets.QLineEdit.ActionPosition.TrailingPosition)
        self.value1ShowAction.setCheckable(True)
        self.value1ShowAction.setVisible(False)
        self.mainLayout.addWidget(self.value1LineEdit)

        self.value2LineEdit = QtWidgets.QLineEdit()
        self.value2ShowAction = self.value2LineEdit.addAction(QtGui.QIcon(Icons.getEye()), QtWidgets.QLineEdit.ActionPosition.TrailingPosition)
        self.value2ShowAction.setCheckable(True)
        self.value2ShowAction.setVisible(False)
        self.mainLayout.addWidget(self.value2LineEdit)

        self.diffButton = QtWidgets.QPushButton()
        self.mainLayout.addWidget(self.diffButton)

        self.closeButton = IconButton(Icons.getCloseOutline())
        self.closeButton.setHoverIcon(Icons.getColorClose())
        self.mainLayout.addWidget(self.closeButton)
