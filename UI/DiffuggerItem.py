from PyQt5 import QtWidgets, QtGui
from Icons import Icons
from IconButton import IconButton


class ui_DiffuggerItemWidget:

    def setupUi(self, widget):
        # widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)

        self.mainLayout = QtWidgets.QHBoxLayout(widget)

        self.nameLineEdit = QtWidgets.QLineEdit()
        self.passwordAction = self.nameLineEdit.addAction(QtGui.QIcon(Icons.getPwdField()), QtWidgets.QLineEdit.ActionPosition.TrailingPosition)
        self.passwordAction.setCheckable(True)
        self.mainLayout.addWidget(self.nameLineEdit)

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
