import sys
from output2 import Ui_category_add
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel,Qt
filename_category = "category_file.txt"
class Ui_categoty_add_subform(QDialog,Ui_category_add):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.on_changed_list_view()
    def showModal(self):
        return super().exec_()
    def on_clicked_add(self):
        Text = self.category_add_text_box.text()
        Text = Text + "\n"
        self.category_add_text_box.setText("")
        with open(filename_category,'a',encoding="Utf-8") as file:
            file.writelines(Text)
        self.on_changed_list_view()
        return
    def on_clicked_quit(self):
        self.close()
        return
    def on_clicked_delete(self):
        if self.on_picked != 0:
            with open(filename_category,'r',encoding="Utf-8") as file:
                line = file.readlines()
            new_line = []
            for i in range(len(line)):
                if i != self.on_picked:
                    new_line.append(line[i])
            with open(filename_category, 'w',encoding="Utf-8") as file:
                file.writelines(new_line)
            self.on_changed_list_view()
        return
    def on_clicked_list_view_index(self,idx):
        self.on_picked= idx.row()
        return
    
    def on_changed_list_view(self):
        with open(filename_category,'r',encoding="Utf-8") as file:
            new_line = file.readlines()
        self.model = QStringListModel()
        for i in range(len(new_line)):
            new_line[i] = new_line[i][:-1]
        self.model.setStringList(new_line)
        self.category_add_list_view.setModel(self.model)
        return
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Ui_categoty_add_subform()
    window.show()
    sys.exit(app.exec_())