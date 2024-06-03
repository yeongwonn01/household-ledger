import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from output import Ui_Dialog
from category_add import Ui_categoty_add_subform
from basic_updated import *
from PyQt5.QtCore import QStringListModel
#_translate = QtCore.QCoreApplication.translate

class MainApp(QMainWindow,Ui_Dialog):
    def __init__(self): #초기 설정
        super().__init__() 
        self.setupUi(self)
        self.on_dialog_changed(0)
        io_x = int((self.geometry().width()-self.input.geometry().width())/2)
        io_y = int((self.geometry().height()-self.input.geometry().height())/2)
        self.input.move(io_x,io_y)
        self.output.move(io_x,io_y)
        self.print_all.move(int((self.geometry().width()-self.print_all.geometry().width())/2),int((self.geometry().height()-self.print_all.geometry().height())/2))
        self.total_money_print.move(io_x,io_y-self.total_money_print.geometry().height()-10)
        self.category.move(io_x+self.input.geometry().width()+10,io_y)
        self.category_index = 0
        self.category_list = []
        self.total_money = 0
    #ui 이벤트 함수
    def on_clicked_input(self): #입금
        text = self.input_textbox.text()
        self.input_textbox.setText("")
        text = int(text)
        self.total_money = money_io(text,True,self.category_list[self.category_index])
        self.total_money_update()
        return
    def on_clicked_output(self): #출금
        text = self.output_textbox.text()
        self.output_textbox.setText("")
        text = int(text)
        self.total_money = money_io(text,False,self.category_list[self.category_index])
        self.total_money_update()
        return
    def on_dialog_changed(self,num): #다이얼로그 바꼈을때
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
        if num == 2 or num == 3:
            self.category.show()
            self.total_money_print.show()
            self.category_combo_box_fx()
            self.total_money = total_money_check()
            self.total_money_update()
        else:
            self.category.hide()
            self.total_money_print.hide()
    def on_category_add_button_clicked(self): #카테고리 추가 버튼 클릭
        self.category_add_window_start()
        self.category_combo_box_fx()
        return
    def on_category_changed(self,num): #카테고리 바꼈을때
        self.category_index = num
        return
    
    #추가한 함수
    def print_all_fx(self): #내역 출력 함수
        new_line=[]#print_all_basic_fx()
        self.model = QStringListModel()
        for i in range(len(new_line)):
            new_line[i] = new_line[i][:-1]
        self.model.setStringList(new_line)
        self.scroll_print_all.setModel(self.model)
        return
    def category_combo_box_fx(self): #카테고리 콤보박스 업데이트
        new_line:list = return_all_category_basic_fx()
        self.category_list = new_line
        for i in range(len(new_line)):
            new_line[i] = new_line[i].replace("\n","")
        self.category_combo_box.clear()
        self.category_combo_box.addItems(new_line)
        return
    def category_add_window_start(self): #카테고리 추가 폼 실행
        win = Ui_categoty_add_subform()
        win.showModal()
        
        return
    def total_money_update(self):
        self.total_money_label.setText(str(self.total_money))
        return
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

#pyuic5 -x untitled.ui -o output.py
#pyuic5 -x category_add.ui -o output2.py