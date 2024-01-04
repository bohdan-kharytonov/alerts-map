# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QTimer
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
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.start_timer()
        self.unique_element = {}
        self.showMaximized()
    def start_timer(self):
           self.timer.start(10000)

    def update_data(self):
        town = {3:"khmelnytskyi", 4:"vinnytsia", 5:"rivne", 8: "volyn", 9:"dnipropetrovsk", 10:"zhytomyr", 11: "zakarpattia", 12: "zaporizha", 13: "ivanoFrankivsk", 14: "kyivRegion", 15: "kirovohrad", 16:"luhansk", 17: "mykolaiv", 18: "odesa", 19: "poltava", 20: "sumy", 21: "ternopil" , 22: "kharkiv", 23: "kherson", 24: "cherkasy", 25: "chernihiv", 26: "chernivtsi", 27: "lviv", 28: "donetsk", 29:"crimea", 31: "kyiv"}

        a = alerts()
        data = a.getActualData()

        if data != self.unique_element:
            self.differences = data.symmetric_difference(self.unique_element)
            # print(self.differences)
            for item in self.unique_element:
                if item in town:
                    new_town = f"{town[item]}"
                    label_town = widget.findChild(QLabel, new_town)
                    label_town.hide()
                    # print(new_town)
            self.unique_element = data.copy()
            self.update_data()
        for item in data:
            if item in town:
                new_town = f"{town[item]}"
                label_town = widget.findChild(QLabel, new_town)
                label_town.show()
                # print(f"Data {item} exists in town with value {town[item]}")
            else:
                print(f"Data {item} does not exist in town")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.update_data()
    widget.show()
    sys.exit(app.exec())
