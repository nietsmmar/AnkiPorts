# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/findreplace.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 209)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.find = QtWidgets.QLineEdit(Dialog)
        self.find.setObjectName("find")
        self.gridLayout.addWidget(self.find, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replace = QtWidgets.QLineEdit(Dialog)
        self.replace.setObjectName("replace")
        self.gridLayout.addWidget(self.replace, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.field = QtWidgets.QComboBox(Dialog)
        self.field.setObjectName("field")
        self.gridLayout.addWidget(self.field, 2, 1, 1, 1)
        self.re = QtWidgets.QCheckBox(Dialog)
        self.re.setObjectName("re")
        self.gridLayout.addWidget(self.re, 4, 1, 1, 1)
        self.ignoreCase = QtWidgets.QCheckBox(Dialog)
        self.ignoreCase.setChecked(True)
        self.ignoreCase.setObjectName("ignoreCase")
        self.gridLayout.addWidget(self.ignoreCase, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.find, self.replace)
        Dialog.setTabOrder(self.replace, self.field)
        Dialog.setTabOrder(self.field, self.ignoreCase)
        Dialog.setTabOrder(self.ignoreCase, self.re)
        Dialog.setTabOrder(self.re, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Find and Replace"))
        self.label.setText(_("<b>Find</b>:"))
        self.label_2.setText(_("<b>Replace With</b>:"))
        self.label_3.setText(_("<b>In</b>:"))
        self.re.setText(_("Treat input as regular expression"))
        self.ignoreCase.setText(_("Ignore case"))
