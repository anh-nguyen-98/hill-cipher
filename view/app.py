import sys

from PyQt5.QtWidgets import QApplication

from controller.controller import Controller
from model.main import Model

import sys
from PyQt5.QtWidgets import *

# from view.MainWindow import MainWindow
from view.MainWindow import MainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = MainWindow()
    view.show()

    controller = Controller(model=Model(), view = view)
    sys.exit(app.exec_())