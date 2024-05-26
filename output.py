# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        self.input = QtWidgets.QGroupBox(Dialog)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(10, 510, 372, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input.setObjectName("input")
        self.input_button = QtWidgets.QPushButton(self.input)
        self.input_button.setEnabled(True)
        self.input_button.setGeometry(QtCore.QRect(110, 140, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_button.sizePolicy().hasHeightForWidth())
        self.input_button.setSizePolicy(sizePolicy)
        self.input_button.setObjectName("input_button")
        self.input_textbox = QtWidgets.QLineEdit(self.input)
        self.input_textbox.setGeometry(QtCore.QRect(70, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_textbox.setFont(font)
        self.input_textbox.setObjectName("input_textbox")
        self.label = QtWidgets.QLabel(self.input)
        self.label.setGeometry(QtCore.QRect(310, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.input)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 331, 81))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.output = QtWidgets.QGroupBox(Dialog)
        self.output.setGeometry(QtCore.QRect(390, 510, 372, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.output.setObjectName("output")
        self.output_button = QtWidgets.QPushButton(self.output)
        self.output_button.setGeometry(QtCore.QRect(110, 140, 151, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_button.sizePolicy().hasHeightForWidth())
        self.output_button.setSizePolicy(sizePolicy)
        self.output_button.setObjectName("output_button")
        self.output_textbox = QtWidgets.QLineEdit(self.output)
        self.output_textbox.setGeometry(QtCore.QRect(70, 80, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output_textbox.setFont(font)
        self.output_textbox.setObjectName("output_textbox")
        self.label_3 = QtWidgets.QLabel(self.output)
        self.label_3.setGeometry(QtCore.QRect(310, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.output)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 331, 81))
        font = QtGui.QFont()
        font.setFamily("함초롬돋움")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.recv_list = QtWidgets.QComboBox(Dialog)
        self.recv_list.setGeometry(QtCore.QRect(870, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.recv_list.setFont(font)
        self.recv_list.setObjectName("recv_list")
        self.recv_list.addItem("")
        self.recv_list.addItem("")
        self.recv_list.addItem("")
        self.recv_list.addItem("")
        self.recv_list.addItem("")
        self.print_all = QtWidgets.QGroupBox(Dialog)
        self.print_all.setGeometry(QtCore.QRect(0, 10, 851, 571))
        self.print_all.setToolTipDuration(-1)
        self.print_all.setObjectName("print_all")
        self.scroll_print_all = QtWidgets.QListView(self.print_all)
        self.scroll_print_all.setGeometry(QtCore.QRect(10, 20, 831, 541))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scroll_print_all.setFont(font)
        self.scroll_print_all.setObjectName("scroll_print_all")

        self.retranslateUi(Dialog)
        self.output_button.clicked.connect(Dialog.on_clicked_output) # type: ignore
        self.input_button.clicked.connect(Dialog.on_clicked_input) # type: ignore
        self.recv_list.currentIndexChanged['int'].connect(Dialog.on_dialog_changed) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.input.setTitle(_translate("Dialog", "입금 그룹"))
        self.input_button.setText(_translate("Dialog", "버튼을 눌러 입금"))
        self.label.setText(_translate("Dialog", "원"))
        self.label_2.setText(_translate("Dialog", "금액을 입력해주세요"))
        self.output.setTitle(_translate("Dialog", "출금 그룹"))
        self.output_button.setText(_translate("Dialog", "버튼을 눌러 출금"))
        self.label_3.setText(_translate("Dialog", "원"))
        self.label_4.setText(_translate("Dialog", "금액을 입력해주세요"))
        self.recv_list.setItemText(0, _translate("Dialog", "메인"))
        self.recv_list.setItemText(1, _translate("Dialog", "내역 출력"))
        self.recv_list.setItemText(2, _translate("Dialog", "입금"))
        self.recv_list.setItemText(3, _translate("Dialog", "출금"))
        self.recv_list.setItemText(4, _translate("Dialog", "수정"))
        self.print_all.setTitle(_translate("Dialog", "내역 출력 그룹"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
