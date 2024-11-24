from PyQt6.QtWidgets import (QApplication, QMainWindow)
from ui import Ui_MainWindow
import json

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)
#----------------------------------------------------------------

NOTES = {
    "нотатка №1": {
        "текст": "Люди я не діма",
        "теги": ["покупка", "хліб"]
    },

    "нотатка №2": {
        "текст": "на треню",
        "теги": ["Діма", "треня"]
    },
}








#----------------------------------------------------------------
win.show()
app.exec()