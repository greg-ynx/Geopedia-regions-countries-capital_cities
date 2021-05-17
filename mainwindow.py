# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_main = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")

# Tab "List of countries"################################################################################################
        self.tab_LOC = QtWidgets.QWidget()
        self.tab_LOC.setObjectName("tab_LOC")

        # Vertical Layout Widget LOC 1
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_LOC)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(220, 50, 311, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_LOC = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_LOC.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_LOC.setObjectName("verticalLayout_LOC")

        self.label_LOC_01 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_LOC_01.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LOC_01.setObjectName("label_LOC_01")
        self.verticalLayout_LOC.addWidget(self.label_LOC_01)

        self.comboBox_LOC = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_LOC.setObjectName("comboBox_LOC")
        self.verticalLayout_LOC.addWidget(self.comboBox_LOC)
        # END Vertical Layout Widget LOC 1

        # Scroll Area Widget LOC
        self.scrollArea_LOC = QtWidgets.QScrollArea(self.tab_LOC)
        self.scrollArea_LOC.setGeometry(QtCore.QRect(10, 160, 751, 341))
        self.scrollArea_LOC.setWidgetResizable(True)
        self.scrollArea_LOC.setObjectName("scrollArea_LOC")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 749, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 9, 731, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_LOC = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_LOC.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_LOC.setObjectName("gridLayout_LOC")
        self.tableView_LOC = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.tableView_LOC.setObjectName("tableView_LOC")
        self.gridLayout_LOC.addWidget(self.tableView_LOC, 0, 0, 1, 1)
        self.scrollArea_LOC.setWidget(self.scrollAreaWidgetContents)
        #END Scroll Area Widget LOC

        # Search button LOC
        self.search_button_LOC = QtWidgets.QPushButton(self.tab_LOC)
        self.search_button_LOC.setGeometry(QtCore.QRect(560, 70, 75, 23))
        self.search_button_LOC.setObjectName("search_button_LOC")
        #END search button LOC

        self.tabWidget.addTab(self.tab_LOC, "")
#END Tab "List of countries"#############################################################################################

# Tab "Search Location"##################################################################################################
        self.tab_SO = QtWidgets.QWidget()
        self.tab_SO.setObjectName("tab_SO")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_SO)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(211, 91, 361, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_SO_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_SO_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_SO_1.setObjectName("verticalLayout_SO_1")

        self.label_SO = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_SO.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SO.setObjectName("label_SO")
        self.verticalLayout_SO_1.addWidget(self.label_SO)

        self.comboBox_SO_Continent = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_SO_Continent.setObjectName("comboBox_SO_Continent")
        self.verticalLayout_SO_1.addWidget(self.comboBox_SO_Continent)

        self.comboBox_SO_Country = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_SO_Country.setObjectName("comboBox_SO_Country")
        self.verticalLayout_SO_1.addWidget(self.comboBox_SO_Country)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_SO)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 150, 61, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_SO_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_SO_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_SO_2.setObjectName("verticalLayout_SO_2")

        self.label_SO_Continent = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_SO_Continent.setObjectName("label_SO_Continent")
        self.verticalLayout_SO_2.addWidget(self.label_SO_Continent)
        self.label_SO_Country = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_SO_Country.setObjectName("label_SO_Country")
        self.verticalLayout_SO_2.addWidget(self.label_SO_Country)

        self.search_button_SO = QtWidgets.QPushButton(self.tab_SO)
        self.search_button_SO.setGeometry(QtCore.QRect(570, 230, 75, 23))
        self.search_button_SO.setObjectName("search_button_SO")
        self.label_SO_research_return = QtWidgets.QLabel(self.tab_SO)
        self.label_SO_research_return.setGeometry(QtCore.QRect(130, 290, 511, 131))
        self.label_SO_research_return.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SO_research_return.setObjectName("label_SO_research_return")

        self.tabWidget.addTab(self.tab_SO, "")
#END Tab "Search Location"###############################################################################################

        self.gridLayout_main.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Location Data browser"))
        self.label_LOC_01.setText(_translate("MainWindow", "Select continent :"))
        self.search_button_LOC.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_LOC), _translate("MainWindow", "List of countries"))
        self.label_SO.setText(_translate("MainWindow", "Select location :"))
        self.label_SO_Continent.setText(_translate("MainWindow", "Continent"))
        self.label_SO_Country.setText(_translate("MainWindow", "Country"))
        self.search_button_SO.setText(_translate("MainWindow", "Search"))
        self.label_SO_research_return.setText(_translate("MainWindow", "Waiting for research return..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SO), _translate("MainWindow", "Search Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
