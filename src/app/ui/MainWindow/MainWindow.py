import json
import webbrowser

from PyQt5.QtWidgets import QFileDialog, QWidget, QTableWidgetItem

from config.definitions import img_dir, txt_dir, data_dir, doc_dir
from src.app.scripts.world_map import *
from src.app.ui.AboutForm.AboutForm import UiAboutForm
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg


def redirect_to_github_repo():
    webbrowser.open('https://github.com/greg-ynx/Geopedia-regions-countries-capital_cities')


def save_fig():
    options = QFileDialog.Options()
    saved_file, ext = QFileDialog.getSaveFileName(QWidget(), "Save figure", doc_dir,
                                                  "PNG Image (*.png) ",
                                                  options=options)
    cairosvg.svg2png(url=os.path.join(map_dir, file_name), write_to=saved_file)


class MainWindow(object):

    def __init__(self, main_window):

        with open(os.path.join(data_dir, 'countries.json'), encoding='utf-8') as json_file:
            self.json_array = json.load(json_file)

        main_window.setObjectName("MainWindow")
        main_window.resize(900, 640)
        main_window.setMinimumSize(QtCore.QSize(900, 640))
        main_window.setBaseSize(QtCore.QSize(900, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(img_dir, "geopedia_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)

        self.help_geopedia_widget = QtWidgets.QWidget()
        self.help_geopedia_form = UiAboutForm(self.help_geopedia_widget,
                                              "Geopedia help",
                                              os.path.join(img_dir, 'QuestionMark.png'),
                                              os.path.join(txt_dir, 'help_geopedia.txt'))

        self.about_greg_ynx_widget = QtWidgets.QWidget()
        self.about_greg_ynx_form = UiAboutForm(self.about_greg_ynx_widget,
                                               "About greg-ynx",
                                               os.path.join(img_dir, 'ynx_logo_800px.png'),
                                               os.path.join(txt_dir, 'about_greg-ynx.txt'))

        self.main_window_centralWidget = QtWidgets.QWidget(main_window)
        self.main_window_centralWidget.setObjectName("main_window_centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.main_window_centralWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.tab_widget = QtWidgets.QTabWidget(self.main_window_centralWidget)
        self.tab_widget.setObjectName("tab_widget")

        self.tab_location_browser = QtWidgets.QWidget()
        self.tab_location_browser.setObjectName("tab_location_browser")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_location_browser)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.capital_city_comboBox = QtWidgets.QComboBox(self.tab_location_browser)
        self.capital_city_comboBox.setObjectName("capital_city_comboBox")
        self.capital_city_comboBox.addItem('<None>')
        self.capital_city_comboBox.activated.connect(lambda:
                                                     self.on_change_capital(
                                                         self.capital_city_comboBox.currentText()
                                                     ))

        self.gridLayout_2.addWidget(self.capital_city_comboBox, 2, 2, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.capital_city_label = QtWidgets.QLabel(self.tab_location_browser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.capital_city_label.sizePolicy().hasHeightForWidth())
        self.capital_city_label.setSizePolicy(sizePolicy)
        self.capital_city_label.setAlignment(QtCore.Qt.AlignCenter)
        self.capital_city_label.setObjectName("capital_city_label")
        self.gridLayout_2.addWidget(self.capital_city_label, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)

        self.country_comboBox = QtWidgets.QComboBox(self.tab_location_browser)
        self.country_comboBox.setObjectName("country_comboBox")
        self.country_comboBox.addItem('<None>')
        self.country_comboBox.activated.connect(lambda:
                                                self.on_change_country(
                                                    self.country_comboBox.currentText()
                                                ))

        self.gridLayout_2.addWidget(self.country_comboBox, 2, 1, 1, 1)
        self.region_label = QtWidgets.QLabel(self.tab_location_browser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.region_label.sizePolicy().hasHeightForWidth())
        self.region_label.setSizePolicy(sizePolicy)
        self.region_label.setAlignment(QtCore.Qt.AlignCenter)
        self.region_label.setObjectName("region_label")
        self.gridLayout_2.addWidget(self.region_label, 1, 0, 1, 1)
        self.country_label = QtWidgets.QLabel(self.tab_location_browser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_label.sizePolicy().hasHeightForWidth())
        self.country_label.setSizePolicy(sizePolicy)
        self.country_label.setAlignment(QtCore.Qt.AlignCenter)
        self.country_label.setObjectName("country_label")
        self.gridLayout_2.addWidget(self.country_label, 1, 1, 1, 1)

        self.region_comboBox = QtWidgets.QComboBox(self.tab_location_browser)
        self.region_comboBox.setObjectName("region_comboBox")
        self.region_comboBox.addItem('<None>')
        self.region_comboBox.activated.connect(lambda:
                                               self.on_change_region(
                                                   self.region_comboBox.currentText()
                                               ))

        for country in self.json_array:

            self.country_comboBox.addItem(country['name'])

            if not (country['region'] in
                    [self.region_comboBox.itemText(i) for i in range(self.region_comboBox.count())]) and \
                    (country['region'] != ''):
                self.region_comboBox.addItem(country['region'])

            if not (country['capital'] in
                    [self.region_comboBox.itemText(i) for i in range(self.region_comboBox.count())]) and \
                    (country['capital'] != ''):
                self.capital_city_comboBox.addItem(country['capital'])

        self.gridLayout_2.addWidget(self.region_comboBox, 2, 0, 1, 1)

        self.svg_widget = QtSvg.QSvgWidget(self.tab_location_browser)
        self.svg_widget.setObjectName("svg_widget")
        map_init()
        self.svg_widget.load(map_path)

        self.gridLayout_2.addWidget(self.svg_widget, 4, 0, 1, 3)
        self.tab_widget.addTab(self.tab_location_browser, "")
        self.tab_countries_list = QtWidgets.QWidget()
        self.tab_countries_list.setObjectName("tab_countries_list")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_countries_list)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.countries_list_scrollArea = QtWidgets.QScrollArea(self.tab_countries_list)
        self.countries_list_scrollArea.setWidgetResizable(True)
        self.countries_list_scrollArea.setObjectName("countries_list_scrollArea")
        self.countries_list_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.countries_list_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 856, 504))
        self.countries_list_scrollAreaWidgetContents.setObjectName("countries_list_scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.countries_list_scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.countries_list_tableWidget = QtWidgets.QTableWidget(self.countries_list_scrollAreaWidgetContents)
        self.countries_list_tableWidget.setObjectName("countries_list_tableWidget")
        self.countries_list_tableWidget.setColumnCount(4)
        self.countries_list_tableWidget.setHorizontalHeaderLabels(['ID', 'Country', 'Continent', 'Capital'])
        header = self.countries_list_tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.countries_list_tableWidget.setRowCount(len(self.json_array))
        self.countries_list_tableWidget.setVerticalHeaderLabels([country['name'] for country in self.json_array])
        index = 0
        for obj in self.json_array:
            self.countries_list_tableWidget.setItem(index, 0, QTableWidgetItem(str(obj.get('id'))))
            self.countries_list_tableWidget.setItem(index, 1, QTableWidgetItem(obj.get('name')))
            self.countries_list_tableWidget.setItem(index, 2, QTableWidgetItem(obj.get('region')))
            self.countries_list_tableWidget.setItem(index, 3, QTableWidgetItem(obj.get('capital')))
            if index < len(self.json_array):
                index += 1
        self.countries_list_tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.gridLayout_4.addWidget(self.countries_list_tableWidget, 0, 0, 1, 1)
        self.countries_list_scrollArea.setWidget(self.countries_list_scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.countries_list_scrollArea, 0, 0, 1, 1)
        self.tab_widget.addTab(self.tab_countries_list, "")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        self.bottom_horizontalLayout = QtWidgets.QHBoxLayout()
        self.bottom_horizontalLayout.setObjectName("bottom_horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_horizontalLayout.addItem(spacerItem2)

        self.save_button = QtWidgets.QPushButton(self.main_window_centralWidget)
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(save_fig)

        self.bottom_horizontalLayout.addWidget(self.save_button)
        self.gridLayout.addLayout(self.bottom_horizontalLayout, 1, 0, 1, 1)
        main_window.setCentralWidget(self.main_window_centralWidget)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.action_Help_Geopedia = QtWidgets.QAction(main_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(os.path.join(img_dir, "QuestionMark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Help_Geopedia.setIcon(icon1)
        self.action_Help_Geopedia.setObjectName("action_Help_Geopedia")
        self.action_Help_Geopedia.triggered.connect(self.help_geopedia_widget.show)

        self.action_About_greg_ynx = QtWidgets.QAction(main_window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(os.path.join(img_dir, "ynx_logo_800px.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_About_greg_ynx.setIcon(icon2)
        self.action_About_greg_ynx.setObjectName("action_About_greg_ynx")
        self.action_About_greg_ynx.triggered.connect(self.about_greg_ynx_widget.show)

        self.action_Join_us_on_GitHub = QtWidgets.QAction(main_window)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(img_dir, "GitHub.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Join_us_on_GitHub.setIcon(icon3)
        self.action_Join_us_on_GitHub.setObjectName("action_Join_us_on_GitHub")
        self.action_Join_us_on_GitHub.triggered.connect(redirect_to_github_repo)

        self.menuHelp.addAction(self.action_Help_Geopedia)
        self.menuHelp.addAction(self.action_About_greg_ynx)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_Join_us_on_GitHub)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def on_change_region(self, value: str):
        self.country_comboBox.clear()
        self.capital_city_comboBox.clear()
        for obj in self.json_array:
            if obj.get('region') == value:
                items = [country['name'] for country in self.json_array if country['region'] == value]
                items.insert(0, '<None>')
                self.country_comboBox.addItems(items)
                items = [country['capital'] for country in self.json_array if country['region'] == value]
                items.insert(0, '<None>')
                self.capital_city_comboBox.addItems(items)
                select_continent(self.region_comboBox.currentText())
                break
            elif value == '<None>':
                items = [country['name'] for country in self.json_array]
                items.insert(0, '<None>')
                self.country_comboBox.addItems(items)
                items = [country['capital'] for country in self.json_array]
                items.insert(0, '<None>')
                self.capital_city_comboBox.addItems(items)
                map_init()
                break
        self.svg_widget.load(os.path.join(map_dir, file_name))

    def on_change_country(self, value: str):
        self.capital_city_comboBox.clear()
        for obj in self.json_array:
            if obj.get('name') == value:
                self.capital_city_comboBox.addItem(obj.get('capital'))
                self.region_comboBox.setCurrentText(obj.get('region'))
                tld = obj.get('tld')[-2:]
                select_country(tld)
                break
            elif value == '<None>':
                items = [country['capital'] for country in self.json_array]
                items.insert(0, '<None>')
                self.capital_city_comboBox.addItems(items)
                map_init()
                break
        self.svg_widget.load(os.path.join(map_dir, file_name))

    def on_change_capital(self, value: str):
        for obj in self.json_array:
            if obj.get('capital') == value:
                self.region_comboBox.setCurrentText(obj.get('region'))
                self.country_comboBox.clear()
                self.country_comboBox.addItems(['<None>', obj.get('name')])
                self.country_comboBox.setCurrentText(obj.get('name'))
                self.capital_city_comboBox.clear()
                self.capital_city_comboBox.addItems(['<None>', obj.get('capital')])
                self.capital_city_comboBox.setCurrentText(obj.get('capital'))
                tld = obj.get('tld')[-2:]
                select_country(tld)
                break
            elif value == '<None>':
                items = [capital['capital'] for capital in self.json_array if capital['capital'] != '']
                items.insert(0, '<None>')
                self.capital_city_comboBox.clear()
                self.capital_city_comboBox.addItems(items)
                self.region_comboBox.setCurrentText('<None>')
                self.country_comboBox.clear()
                items = [country['name'] for country in self.json_array]
                items.insert(0, '<None>')
                self.country_comboBox.addItems(items)
                map_init()
                break
        self.svg_widget.load(os.path.join(map_dir, file_name))

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Geopedia"))
        self.capital_city_label.setText(_translate("MainWindow", "Capital city"))
        self.region_label.setText(_translate("MainWindow", "Region"))
        self.country_label.setText(_translate("MainWindow", "Country"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_location_browser),
                                   _translate("MainWindow", "Location browser"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_countries_list),
                                   _translate("MainWindow", "Data base"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_Help_Geopedia.setText(_translate("MainWindow", "Geopedia help"))
        self.action_About_greg_ynx.setText(_translate("MainWindow", "About greg-ynx"))
        self.action_Join_us_on_GitHub.setText(_translate("MainWindow", "Join us on GitHub!"))
