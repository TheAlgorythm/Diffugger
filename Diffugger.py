import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow


class App:

    @staticmethod
    def run(arg):
        app = QApplication(arg)

        mainWindow = MainWindow()
        mainWindow.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
        App.run(sys.argv)
