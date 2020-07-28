# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/fields.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 352)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fieldList = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setMinimumSize(QtCore.QSize(50, 60))
        self.fieldList.setObjectName("fieldList")
        self.horizontalLayout.addWidget(self.fieldList)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fieldAdd = QtWidgets.QPushButton(Dialog)
        self.fieldAdd.setObjectName("fieldAdd")
        self.verticalLayout_3.addWidget(self.fieldAdd)
        self.fieldDelete = QtWidgets.QPushButton(Dialog)
        self.fieldDelete.setObjectName("fieldDelete")
        self.verticalLayout_3.addWidget(self.fieldDelete)
        self.fieldRename = QtWidgets.QPushButton(Dialog)
        self.fieldRename.setObjectName("fieldRename")
        self.verticalLayout_3.addWidget(self.fieldRename)
        self.fieldPosition = QtWidgets.QPushButton(Dialog)
        self.fieldPosition.setObjectName("fieldPosition")
        self.verticalLayout_3.addWidget(self.fieldPosition)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._2 = QtWidgets.QGridLayout()
        self._2.setObjectName("_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self._2.addWidget(self.label_5, 0, 0, 1, 1)
        self.fontFamily = QtWidgets.QFontComboBox(Dialog)
        self.fontFamily.setMinimumSize(QtCore.QSize(0, 25))
        self.fontFamily.setObjectName("fontFamily")
        self._2.addWidget(self.fontFamily, 0, 1, 1, 1)
        self.rtl = QtWidgets.QCheckBox(Dialog)
        self.rtl.setObjectName("rtl")
        self._2.addWidget(self.rtl, 3, 1, 1, 1)
        self.fontSize = QtWidgets.QSpinBox(Dialog)
        self.fontSize.setMinimum(5)
        self.fontSize.setMaximum(300)
        self.fontSize.setObjectName("fontSize")
        self._2.addWidget(self.fontSize, 0, 2, 1, 1)
        self.sticky = QtWidgets.QCheckBox(Dialog)
        self.sticky.setObjectName("sticky")
        self._2.addWidget(self.sticky, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self._2.addWidget(self.label_18, 1, 0, 1, 1)
        self.sortField = QtWidgets.QRadioButton(Dialog)
        self.sortField.setObjectName("sortField")
        self._2.addWidget(self.sortField, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self._2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.fieldList, self.fieldAdd)
        Dialog.setTabOrder(self.fieldAdd, self.fieldDelete)
        Dialog.setTabOrder(self.fieldDelete, self.fieldRename)
        Dialog.setTabOrder(self.fieldRename, self.fieldPosition)
        Dialog.setTabOrder(self.fieldPosition, self.fontFamily)
        Dialog.setTabOrder(self.fontFamily, self.fontSize)
        Dialog.setTabOrder(self.fontSize, self.sortField)
        Dialog.setTabOrder(self.sortField, self.sticky)
        Dialog.setTabOrder(self.sticky, self.rtl)
        Dialog.setTabOrder(self.rtl, self.buttonBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_("Fields"))
        self.fieldAdd.setText(_("Add"))
        self.fieldDelete.setText(_("Delete"))
        self.fieldRename.setText(_("Rename"))
        self.fieldPosition.setText(_("Reposition"))
        self.label_5.setText(_("Editing Font"))
        self.rtl.setText(_("Reverse text direction (RTL)"))
        self.sticky.setText(_("Remember last input when adding"))
        self.label_18.setText(_("Options"))
        self.sortField.setText(_("Sort by this field in the browser"))

from . import icons_rc
