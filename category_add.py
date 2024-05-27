import sys
from output2 import Ui_category_add
from PyQt5.QtWidgets import *

class Ui_categoty_add_subform(QDialog,Ui_category_add):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def showModal(self):
        return super().exec_()
    