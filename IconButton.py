from PyQt5.QtWidgets import QToolButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class IconButton(QToolButton):

    defaultIcon = None
    hoverIcon = None

    def __init__(self, icon=None):
        super().__init__()
        self.setStyleSheet('background: transparent; border: none; margin: 0px; padding: 0px;')
        self.setIconSize(QSize(20, 20))
        if icon:
            self.setIcon(icon)

    def iconStringToIcon(self, icon):
        if isinstance(icon, str):
            icon = QIcon(icon)
        return icon

    def setIcon(self, icon, isDefault=True):
        icon = self.iconStringToIcon(icon)
        super().setIcon(icon)
        if isDefault:
            self.defaultIcon = icon

    def setHoverIcon(self, icon, isDefault=True):
        icon = self.iconStringToIcon(icon)
        self.hoverIcon = icon

    def setClickIcon(self, icon, isDefault=True):
        icon = self.iconStringToIcon(icon)
        self.clickIcon = icon

    def enterEvent(self, event):
        super().enterEvent(event)
        if self.hoverIcon:
            self.setIcon(self.hoverIcon, False)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        if self.hoverIcon:
            self.setIcon(self.defaultIcon, False)