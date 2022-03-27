# This script is the main executable script for Geopedia project.
#
# Author : greg-ynx

import sys

from PyQt5 import QtWidgets
from src.app.ui import MainWindow


def main():

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
