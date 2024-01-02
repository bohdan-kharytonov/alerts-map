# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QPixmap, QColor, QPalette
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from alerts import *

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    a = alerts()
    data = a.getActualData()
    if '19' in str(data):
        label_poltava = widget.findChild(QLabel, "poltava")
        label_poltava.show()
        pm = label_poltava.pixmap()
        pm.fill(QColor('#FFFFFF'))
        label_poltava.setPixmap(pm)
        label_poltava.setMask(pm.mask())
        label_poltava.hide()
        label_poltava.show()
    else:
        label_poltava = widget.findChild(QLabel, "poltava")
        label_poltava.hide()
        # hui = pixmap->fromFile
        # label_poltava.setPixma
        pm = label_poltava.pixmap()
        pm.fill(QColor('#FFFFFF'))
        label_poltava.setPixmap(pm)
        label_poltava.setMask(pm.mask())
        label_poltava.hide()

    label_sumy = widget.findChild(QLabel, "sumy")
    label_sumy.hide()

    widget.show()
    sys.exit(app.exec())
