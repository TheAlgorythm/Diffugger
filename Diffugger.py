import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from MainWindow import MainWindow


class App:

    @staticmethod
    def run(arg):
        app = QApplication(arg)
        app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

        mainWindow = MainWindow()
        mainWindow.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
        App.run(sys.argv)
