# Main file
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from continent import Continent
from country import Country
from mainwindow import Ui_MainWindow

"""    
    connection = sqlite3.connect("bdd.db")
    africa = Continent(connection, 'Africa')
    africa.get_id()
    africa.get_countries()
"""

if __name__ == '__main__':
    import sys
    #connection = sqlite3.connect("bdd.db")
    #cursor = connection.cursor()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())