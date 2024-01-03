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
        self.a = alerts()
        self.data = self.a.getActualData()
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        alerts()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    a = alerts()
    data = a.getActualData()

    town = {3:"khmelnytskyi", 4:"vinnytsia", 5:"rivne", 8: "volyn", 9:"dnipropetrovsk", 10:"zhytomyr", 11: "zakarpattia", 12: "zaporizha", 13: "ivanoFrankivsk", 14: "kyivRegion", 15: "kirovohrad", 16:"luhansk", 17: "mykolaiv", 18: "odesa", 19: "poltava", 20: "sumy", 21: "ternopil" , 22: "kharkiv", 23: "kherson", 24: "cherkasy", 25: "chernihiv", 26: "chernivtsi", 27: "lviv", 28: "donetsk", 29:"crimea", 31: "kyiv"}
    for item in data:
        if item in town:
            new_town = f"{town[item]}"
            # print(new_town)
            label_town = widget.findChild(QLabel, new_town)
            label_town.show()
            print(f"Data {item} exists in town with value {town[item]}")
        else:
            print(f"Data {item} does not exist in town")

    widget.show()
    sys.exit(app.exec())
