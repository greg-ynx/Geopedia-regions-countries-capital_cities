import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from continent import Continent
from country import Country

class Ui_MainWindow(object):
    def loadData(self):
        """
        Connect program with "bdd.db" file
        """
        self.connection = sqlite3.connect("bdd.db")
        self.cursor = self.connection.cursor()

    def get_continents(self):
        """
        SQL query selecting every continents
        :return: list of continent_name from data base "bdd.db"
        """
        query = self.cursor.execute("SELECT continent_name FROM Continents")
        answer = query.fetchall()
        return answer

    def get_countries(self):
        """
        SQL query selecting every countries
        :return: list of country_name from data base "bdd.db"
        """
        query = self.cursor.execute("SELECT country_name FROM Countries")
        answer = query.fetchall()
        return answer

    def setupUi(self, MainWindow):
        self.loadData()
        self.africa = Continent('Africa')
        self.asia = Continent('Asia')
        self.europe = Continent('Europe')
        self.north_america = Continent('North-America')
        self.oceania = Continent('Oceania')
        self.south_america = Continent('South-America')
        self.antarctica = Continent('Antarctica')
        self.sql_continents = self.get_continents()
        self.sql_countries = self.get_countries()
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

        # Vertical Layout Widget LOC
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
        self.init_combo_Box(self.comboBox_LOC, "continent")
        self.verticalLayout_LOC.addWidget(self.comboBox_LOC)
        #self.comboBox_LOC.currentTextChanged.connect(self.combo_LOC_changed)
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

        self.tableWidget_LOC = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.tableWidget_LOC.setObjectName("tableView_LOC")
        self.tableWidget_LOC.setFont(QtGui.QFont('Arial',8))
        self.gridLayout_LOC.addWidget(self.tableWidget_LOC, 0, 0, 1, 1)

        self.scrollArea_LOC.setWidget(self.scrollAreaWidgetContents)
        #END Scroll Area Widget LOC

        # Search button LOC
        self.search_button_LOC = QtWidgets.QPushButton(self.tab_LOC)
        self.search_button_LOC.setGeometry(QtCore.QRect(560, 70, 75, 23))
        self.search_button_LOC.setObjectName("search_button_LOC")
        self.search_button_LOC.clicked.connect(self.comboBox_LOC_changed)
        #END search button LOC

        self.tabWidget.addTab(self.tab_LOC, "")
#END Tab "List of countries"#############################################################################################

# Tab "Search Location"##################################################################################################
        self.tab_SO = QtWidgets.QWidget()
        self.tab_SO.setObjectName("tab_SO")

        # Vertical Layout Widget SO 1
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
        self.init_combo_Box(self.comboBox_SO_Continent, "continent")
        self.verticalLayout_SO_1.addWidget(self.comboBox_SO_Continent)
        self.comboBox_SO_Continent.currentTextChanged.connect(self.comboBox_SO_Continent_changed)

        self.comboBox_SO_Country = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_SO_Country.setObjectName("comboBox_SO_Country")
        self.init_combo_Box(self.comboBox_SO_Country, "country")
        self.verticalLayout_SO_1.addWidget(self.comboBox_SO_Country)
        # END Vertical Layout Widget SO 1

        # Vertical Layout Widget SO 2
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
        # END Vertical Layout Widget SO 2

        self.search_button_SO = QtWidgets.QPushButton(self.tab_SO)
        self.search_button_SO.setGeometry(QtCore.QRect(570, 230, 75, 23))
        self.search_button_SO.setObjectName("search_button_SO")


        self.label_SO_research_return = QtWidgets.QLabel(self.tab_SO)
        self.label_SO_research_return.setGeometry(QtCore.QRect(130, 290, 511, 131))
        self.label_SO_research_return.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SO_research_return.setObjectName("label_SO_research_return")

        self.search_button_SO.clicked.connect(self.search_button_SO_search)

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
        self.label_LOC_01.setText(_translate("MainWindow", "Select a continent :"))
        self.search_button_LOC.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_LOC), _translate("MainWindow", "List of countries"))
        self.label_SO.setText(_translate("MainWindow", "Select location :"))
        self.label_SO_Continent.setText(_translate("MainWindow", "Continent"))
        self.label_SO_Country.setText(_translate("MainWindow", "Country"))
        self.search_button_SO.setText(_translate("MainWindow", "Search"))
        self.label_SO_research_return.setText(_translate("MainWindow", "Waiting for research return..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SO), _translate("MainWindow", "Search Location"))

    def init_combo_Box(self, comboBox, Item_type):
        """
        Initializing combo box
        :param comboBox: combo box variable
        :param Item_type: Please input "continent" or "country"
        :return: nothing
        """
        comboBox.addItem(None)
        if Item_type == "continent":
            for i in range(len(self.sql_continents)):
                comboBox.addItem(self.sql_continents[i][0])
        elif Item_type == "country":
            for i in range(len(self.sql_countries)):
                comboBox.addItem(self.sql_countries[i][0])
        else :
            index = comboBox.findText(None)
            comboBox.removeItem(index)
            print("Item_type is not 'continent' or 'country' please check your input")

    def n_rows(self, continent):
        """
        Define how many rows are needed for the TableWidget
        :param continent: Continent() object
        :return: rows : int
            Rows count needed
        """
        print("{} countries count is : {}".format(continent.name, continent.get_countries_count()))
        rows = continent.get_countries_count()/4
        if (rows*4)%4 == 0 :
            return int(rows)
        elif (rows*4)%4 != 0 :
            rows = int(rows+1)
            return rows
        else :
            print("n_columns input type should be 'int' type")

    def comboBox_LOC_changed(self):
        """
        Generate TableWidget_LOC items for any selected continent
        """
        text = self.comboBox_LOC.currentText()
        if (text == "") or (text == "Antarctica") :
            self.tableWidget_LOC.setColumnCount(0)
            self.tableWidget_LOC.setRowCount(0)
            print("Nothing shown")
            return
        elif text == "Africa" :
            print("African countries Table shown")
            self.tableWidget_LOC_built(self.africa)
        elif text == "Asia" :
            print("Asian countries Table shown")
            self.tableWidget_LOC_built(self.asia)
        elif text == "Europe" :
            print("European countries Table shown")
            self.tableWidget_LOC_built(self.europe)
        elif text == "North-America" :
            print("North american countries Table shown")
            self.tableWidget_LOC_built(self.north_america)
        elif text == "Oceania" :
            print("Oceanian countries Table shown")
            self.tableWidget_LOC_built(self.oceania)
        elif text == "South-America" :
            print("South american countries Table shown")
            self.tableWidget_LOC_built(self.south_america)

    def tableWidget_LOC_built(self, continent):
        """
        Generate rows, columns and item of TableWidget_LOC
        :param continent: Continent() object
        """
        index = 0
        index_max = continent.get_countries_count() - 1
        columnsCount = 4
        rowsCount = self.n_rows(continent)
        print(rowsCount)
        self.tableWidget_LOC.setColumnCount(columnsCount)
        for column in range(columnsCount):
            self.tableWidget_LOC.setColumnWidth(column, 182.25)
        self.tableWidget_LOC.setRowCount(rowsCount)
        for row in range(rowsCount):
            for column in range(columnsCount):
                if index <= index_max :
                    item = QtWidgets.QTableWidgetItem(continent.get_countries()[index][0])
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget_LOC.setItem(row, column, item)
                else :
                    item = QtWidgets.QTableWidgetItem("")
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget_LOC.setItem(row, column, item)
                index +=1
        self.tableWidget_LOC.horizontalHeader().hide()
        self.tableWidget_LOC.verticalHeader().hide()

    def comboBox_SO_Continent_changed(self):
        """
        Select countries that are within the selected continent
        """
        text = self.comboBox_SO_Continent.currentText()
        if text == "":
            print("Select a continent")
            self.comboBox_SO_Continent_select_countries("")
            return
        elif text == "Africa":
            print("Select africans countries")
            self.comboBox_SO_Continent_select_countries(self.africa)
        elif text == "Asia":
            print("Select asians countries")
            self.comboBox_SO_Continent_select_countries(self.asia)
        elif text == "Europe":
            print("Select europeans countries")
            self.comboBox_SO_Continent_select_countries(self.europe)
        elif text == "North-America":
            print("Select north americans countries")
            self.comboBox_SO_Continent_select_countries(self.north_america)
        elif text == "Oceania":
            print("Select oceanians countries")
            self.comboBox_SO_Continent_select_countries(self.oceania)
        elif text == "South-America":
            print("Select south americans countries")
            self.comboBox_SO_Continent_select_countries(self.south_america)
        elif text == "Antarctica":
            print("Select africans countries")
            self.comboBox_SO_Continent_select_countries(self.antarctica)

    def comboBox_SO_Continent_select_countries(self, continent):
        """
        Modify comboBox_SO_Country in order to show the new list of selectable countries
        :param continent: Continent() object
        """
        self.comboBox_SO_Country.clear()
        self.comboBox_SO_Country.addItem("")
        if continent == "":
            for i in range(len(self.sql_countries)):
                self.comboBox_SO_Country.addItem(self.sql_countries[i][0])
        else :
            for i in range(continent.get_countries_count()):
                self.comboBox_SO_Country.addItem(continent.get_countries()[i][0])

    def search_button_SO_search(self):
        """
        Write research results for 'Search Location'
        """
        continent = self.comboBox_SO_Continent.currentText()
        country = self.comboBox_SO_Country.currentText()
        if (continent == "") and (country == ""):
            print("Please select a continent or a country")
            self.label_SO_research_return.setText("Please select a continent or a country")
        elif continent == "Antarctica":
            self.label_SO_research_return.setText("Continent : {}, There is no native country in Antarctica".format(continent))
        else :
            if country == "":
                print("Please select a country")
                self.label_SO_research_return.setText("Please select a country")
            else:
                self.label_SO_research_return.setText("Continent : {}, Country : {}, Capital city : {}".format(Country(country).get_continent(), country, Country(country).get_capital_city()))