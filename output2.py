# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'category_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_category_add(object):
    def setupUi(self, category_add):
        category_add.setObjectName("category_add")
        category_add.resize(400, 300)

        self.retranslateUi(category_add)
        QtCore.QMetaObject.connectSlotsByName(category_add)

    def retranslateUi(self, category_add):
        _translate = QtCore.QCoreApplication.translate
        category_add.setWindowTitle(_translate("category_add", "category_add"))


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    category_add = QtWidgets.QWidget()
    ui = Ui_category_add()
    ui.setupUi(category_add)
    category_add.show()
    sys.exit(app.exec_())
