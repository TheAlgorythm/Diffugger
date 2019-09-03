from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Icons import Icons
from IconButton import IconButton


class ui_MainWindow:

    def setupUi(self, window):
        window.setObjectName('Diffugger')
        window.setWindowTitle('Diffugger')
        window.resize(600, 400)
        self.widget = QtWidgets.QWidget()
        self.mainLayout = QtWidgets.QVBoxLayout(self.widget)

        self.diffuggerItemScrollArea = QtWidgets.QScrollArea()
        self.diffuggerItemScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.diffuggerItemScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diffuggerItemScrollArea.setWidgetResizable(True)
        self.diffuggerItemScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollWidget = QtWidgets.QWidget(self.diffuggerItemScrollArea)
        self.scrollWidget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.diffuggerItemLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.diffuggerItemLayout.setAlignment(Qt.AlignTop)
        self.diffuggerItemLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.mainLayout.addWidget(self.diffuggerItemScrollArea)

        self.toolLayout = QtWidgets.QHBoxLayout()
        self.toolLayout.setAlignment(Qt.AlignLeft)
        self.addButton = IconButton(Icons.getAdd())
        self.addButton.setHoverIcon(Icons.getColorAdd())
        self.toolLayout.addWidget(self.addButton)
        self.mainLayout.addLayout(self.toolLayout)
        window.setCentralWidget(self.widget)
