import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from output import Ui_Dialog

class MainApp(QMainWindow,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())