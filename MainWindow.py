from PyQt5.QtWidgets import QMainWindow
from UI.MainWindow import ui_MainWindow
from DiffuggerItem import DiffuggerItem
from ItemParent import ItemParent


class MainWindow(QMainWindow, ItemParent):

    def __init__(self):
        super().__init__()
        self.ui = ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.addItem)
        self.addItem()

    def addItem(self):
        self.ui.diffuggerItemLayout.addWidget(DiffuggerItem(self))

    def closeItem(self, item):
        self.ui.diffuggerItemLayout.removeWidget(item)
        item.deleteLater()
        item = None
