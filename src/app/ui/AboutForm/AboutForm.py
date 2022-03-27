from PyQt5 import QtCore, QtGui, QtWidgets


class UiAboutForm(object):

    def __init__(self, about_form, title, icon_path, txt_file_path):

        about_form.setObjectName("About_Form")
        about_form.resize(650, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(about_form.sizePolicy().hasHeightForWidth())
        about_form.setSizePolicy(sizePolicy)
        about_form.setMinimumSize(QtCore.QSize(650, 600))
        about_form.setMaximumSize(QtCore.QSize(650, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_form.setWindowIcon(icon)
        about_form.setWindowTitle(title)
        self.about_form = about_form

        self.gridLayout = QtWidgets.QGridLayout(about_form)
        self.gridLayout.setObjectName("gridLayout")

        self.textArea_grid_layout = QtWidgets.QGridLayout()
        self.textArea_grid_layout.setObjectName("textArea_grid_layout")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(about_form)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textArea_grid_layout.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.gridLayout.addLayout(self.textArea_grid_layout, 0, 0, 1, 1)

        self.bottom_horizontal_layout = QtWidgets.QHBoxLayout()
        self.bottom_horizontal_layout.setObjectName("bottom_horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_horizontal_layout.addItem(spacerItem)

        self.close_button = QtWidgets.QPushButton(about_form)
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(self.about_form.close)
        self.bottom_horizontal_layout.addWidget(self.close_button)

        self.gridLayout.addLayout(self.bottom_horizontal_layout, 1, 0, 1, 1)

        self.retranslateUi(about_form)
        self.set_text(txt_file_path)
        QtCore.QMetaObject.connectSlotsByName(about_form)

    def set_text(self, txt_file_path):
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.plainTextEdit.setPlainText(content)

    def retranslateUi(self, about_form):
        _translate = QtCore.QCoreApplication.translate
        self.close_button.setText(_translate("About_Form", "Close"))
