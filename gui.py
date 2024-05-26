import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from output import Ui_Dialog
from basic_main import *
from PyQt5.QtCore import QStringListModel
#_translate = QtCore.QCoreApplication.translate

class MainApp(QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on_dialog_changed(0)
        self.input.move(364,264)
        self.output.move(364,264)
        self.print_all.move((self.geometry().width()-self.print_all.geometry().width())/2,(self.geometry().height()-self.print_all.geometry().height())/2)
    
    def on_clicked_input(self):
        text = self.input_textbox.text()
        self.input_textbox.setText("")
        text = str(text) + "원"#basic_main 코드를 사용하기 위해 형식 지키기 -> 나중에 수정 필요
        input_money(text)
        return
    def on_clicked_output(self):
        text = self.output_textbox.text()
        self.output_textbox.setText("")
        text = str(text) + "원"#basic_main 코드를 사용하기 위해 형식 지키기 -> 나중에 수정 필요
        output_money(text)
        return
    def on_dialog_changed(self,num):
        if num == 2:
            self.input.show()
        else:
            self.input.hide()
        if num == 3:
            self.output.show()
        else:
            self.output.hide()
        if num == 1:
            self.print_all.show()
            self.print_all_fx()
        else:
            self.print_all.hide()
        return
    def print_all_fx(self):
        new_line=print_all_basic_fx()
        self.model = QStringListModel()
        for i in range(len(new_line)):
            new_line[i] = new_line[i][:-1]
        self.model.setStringList(new_line)
        self.scroll_print_all.setModel(self.model)
        return
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

#pyuic5 -x untitled.ui -o output.py